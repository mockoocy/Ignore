from copy import deepcopy
from typing import Any, Dict, List, override

from src.lang.stdlib import global_env
from src.lang.utils.BuiltIn import BuiltIn
from src.lang.utils.EarlyExit import EarlyExit
from src.lang.utils.Environment import Environment
from src.lang.utils.FunctionArgument import FunctionArgument
from src.lang.utils.FunctionInfo import FunctionInfo
from src.lang.utils.VariableInfo import (Valid_Types, Valid_Types_Reversed,
                                         VariableInfo)

from .generated.ignoreParser import ignoreParser
from .generated.ignoreParserVisitor import ignoreParserVisitor
from .stdlib import global_env
from .utils.types import VarDeclDict


class Visitor(ignoreParserVisitor):

    def __init__(self, variables: VarDeclDict):
        # By quick glance at parent classes, super class does define __init__, so no need to call super() there
        self.variables = variables
        self.current_env = deepcopy(global_env)
        super().__init__()  # Call parent class constructor

    def _catch_return(self, block: ignoreParser.BlockContext):
        # return statements throw EarlyExit exception, which allows us to propagate return value through
        # the stack and ignore further instructions inside function block.
        try:
            self.visitBlock(block)
        except EarlyExit as early_exit:
            return early_exit.value

    @override
    def visitLiteral(self, ctx: ignoreParser.LiteralContext):
        literal = ctx
        if literal.LITERAL_STRING() is not None:
            raw_string = str(literal.LITERAL_STRING())
            return raw_string[1:-1]  # removes quotes

        elif literal.LITERAL_INT() is not None:
            return int(str(literal.LITERAL_INT()))

        elif literal.LITERAL_FLOAT() is not None:
            return float(str(literal.LITERAL_FLOAT()))

        elif literal.LITERAL_BOOL() is not None:
            bool_str = str(literal.LITERAL_BOOL())
            if bool_str == "True":
                return True
            elif bool_str == "False":
                return False

        else:
            raise NotImplementedError("Unsupported literal type")

    @override
    def visitBlock(self, ctx: ignoreParser.BlockContext):
        prev_env = self.current_env
        self.current_env = Environment(enclosing=prev_env, variables={})
        for child in ctx.getChildren():
            self.visit(child)
        self.current_env = prev_env

    @staticmethod
    def fill_arguments_with_values(parameters: Dict[str, str], values) -> Dict[str, FunctionArgument]:
        if (len(parameters) != len(values)):
            raise ValueError("Invalid number of arguments")
        param_data = zip(parameters.keys(), parameters.values(), values)
        return {
            param_name: FunctionArgument(param_value, param_type) 
            for (param_name, param_type, param_value) 
            in param_data
            }

    def _evaluate_builtin_call(self, builtin: BuiltIn, arguments: List[Any]):
        return builtin(*arguments)

    def _evaluate_function_call(self, function: FunctionInfo, arguments: List[Any]):
        # TODO add logic bounding function.params to argument(s).
        prev_env = self.current_env
        function_env = function.function_env
        assert function_env is not None
        params = Visitor.fill_arguments_with_values(function.params, arguments) if function.params else {}
        self.current_env = Environment(enclosing=None, variables=function_env | params)
        result = self._catch_return(function.body)
        self.current_env = prev_env
        return result

    @override
    def visitArgumentList(self, ctx: ignoreParser.ArgumentListContext) -> List[Any]:
        arguments = ctx.getChildren()
        return [self.visitExpr(argument) for argument in arguments]

    @override
    def visitFunctionCall(self, ctx: ignoreParser.FunctionCallContext):
        function_name = ctx.NAME().getText()
        arguments = []
        if argument_list := ctx.argumentList():
            arguments = self.visitArgumentList(argument_list)  # only 1-arg functions allowed for now
        
        function = self.current_env.lookup_variable(function_name)
        if not function:
            raise ValueError(
                f"Function '{function_name}' not defined in the current environment"
            )
        if isinstance(function, BuiltIn):
            return self._evaluate_builtin_call(function, arguments)
        elif isinstance(function, FunctionInfo):
            return self._evaluate_function_call(function, arguments)
        else:
            raise ValueError(f"{function_name} is not a function!")

    @override
    def visitExpr(self, ctx: ignoreParser.ExprContext):
        if ctx is None:
            return None

        expr = ctx
        current_env = self.current_env
        if expr.OPEN_PAREN() and expr.CLOSE_PAREN():
            return self.visitExpr(expr.expr(0))
        if expr.literal() is not None:
            return self.visitLiteral(expr.literal())
        if expr.NAME() is not None:
            var_name = expr.NAME().getText()
            var_info = current_env.lookup_variable(var_name)
            if not var_info:
                raise ValueError(f"No such variable declared {var_name}")
            if isinstance(var_info, FunctionArgument):
                return var_info.value
            assert isinstance(var_info, VariableInfo)
            if not var_info.was_evaluated:
                raise ReferenceError(f"Attempted to use undeclared variable {var_name}")
            return var_info.value 

        if expr.functionCall() is not None:
            return self.visitFunctionCall(expr.functionCall())
        if expr.NOT():
            return not self.visitExpr(expr.expr(0))
        # Now we surely deal with a binary operation
        left = self.visitExpr(expr.expr(0))
        right = self.visitExpr(expr.expr(1))

        if expr.ADD() is not None:
            return left + right
        elif expr.SUB() is not None:
            return left - right
        elif expr.MUL() is not None:
            return left * right
        elif expr.DIV() is not None:
            return left / right  # division by zero?!
        elif expr.MOD() is not None:
            return left % right
        elif expr.INT_DIV() is not None:
            return left // right
        # case of comparision, maybe should switch these to be EQ, NEQ, LT, etc. instead of this check
        elif str(expr.OPERATOR_COMPARE()) == "==":
            return left == right
        elif str(expr.OPERATOR_COMPARE()) == "!=":
            return left != right
        elif str(expr.OPERATOR_COMPARE()) == ">":
            return left > right
        elif str(expr.OPERATOR_COMPARE()) == "<":
            return left < right
        elif str(expr.OPERATOR_COMPARE()) == ">=":
            return left >= right
        elif str(expr.OPERATOR_COMPARE()) == "<=":
            return left <= right
        elif expr.OPERATOR_LOGIC() is not None:
            if str(expr.OPERATOR_LOGIC()) == "&&":
                return left and right
            elif str(expr.OPERATOR_LOGIC()) == "||":
                return left or right
        else:
            raise NotImplementedError("Unsupported expression syntax")

    @override
    def visitCondition(self, ctx: ignoreParser.ConditionContext):
        if ctx.LITERAL_BOOL():
            return True if ctx.LITERAL_BOOL().getText() == "True" else False
        return bool(
            self.visitExpr(ctx.expr())
        )  # an expression. If not castable to bool - then ok.

    @override
    def visitIf_statement(self, ctx: ignoreParser.If_statementContext) -> bool:
        # returns wether the condition was evaluated
        condition_result = self.visitCondition(ctx.if_().condition())
        if condition_result:
            self.visitBlock(ctx.block())
        return condition_result

    @override
    def visitElif_statement(self, ctx: ignoreParser.Elif_statementContext):
        condition_result = self.visitCondition(ctx.elif_().condition())
        if condition_result:
            self.visitBlock(ctx.block())

        return condition_result

    @override
    def visitElse_statement(self, ctx: ignoreParser.Else_statementContext):
        self.visitBlock(ctx.block())

    @override
    def visitControl_statement(self, ctx: ignoreParser.Control_statementContext):
        evaluated = self.visitIf_statement(ctx.if_statement())
        if evaluated:
            return
        for elif_ctx in ctx.elif_statement():
            evaluated = self.visitElif_statement(elif_ctx)
            if evaluated:
                break
        if ctx.else_statement() and not evaluated:
            self.visitElse_statement(ctx.else_statement())

    @override
    def visitVarDecl(self, ctx: ignoreParser.VarDeclContext):
        variable_info = self.variables[ctx]
        var_name = ctx.FUNCTION_NAME().getText()[5:]
        self.current_env.variables[var_name] = variable_info
        assert isinstance(variable_info, VariableInfo)
        if variable_info.was_evaluated == True:
            return variable_info

        var_expression = ctx.parentCtx.wrapped_expr().expr()
        expr_val = self.visitExpr(var_expression)

        if variable_info.type != None:  # jesli typ był podany w deklaracji
            var_type = Valid_Types[variable_info.type]
            try:  # jesli nie castowalne na dany typ to zwroc type error
                variable_info.value = var_type(expr_val)  # castowanie na var_type
            except ValueError:
                raise TypeError(
                    f"could not cast value of {var_name} to type : {var_type}"
                )

        else:  # jesli nie podano typu to jest przypisywany domyslny dla zmiennej
            variable_info.type = Valid_Types_Reversed.get(type(expr_val))
            variable_info.value = expr_val
        variable_info.was_evaluated = True
        print(
            f"updated variables with variable {var_name}, of type {variable_info.type}, and value = {variable_info.value}"
        )
        return variable_info

    @override
    def visitVar_assign(self, ctx: ignoreParser.Var_assignContext):
        input_string = ctx.PROPERTY_NAME().getText()
        parts = input_string.split()
        var_name = parts[0]

        current_env = self.current_env
        var_info = current_env.lookup_variable(var_name)
        assert isinstance(var_info, VariableInfo)
        if var_info != None:
            var_expression = ctx.wrapped_expr().expr()
            expr_val = self.visitExpr(var_expression)
            var_info.value = expr_val
        else:
            raise ValueError(
                f"You are trying to change value of variable = {var_name} but it was not declared in the code earlier"
            )
        # return self.visitChildren(ctx)

    @override
    def visitWhile_loop(self, ctx: ignoreParser.While_loopContext):
        condition_result = self.visitCondition(ctx.loop_condition().condition())
        while condition_result == True:
            self.visitBlock(ctx.block())
            condition_result = self.visitCondition(ctx.loop_condition().condition())

    @override
    def visitFor_loop(self, ctx: ignoreParser.For_loopContext):
        if ctx.var() is not None:
            self.visitVarDecl(ctx.var().varDecl())

        condition_result = self.visitCondition(ctx.loop_condition().condition())

        while condition_result == True:
            self.visitBlock(ctx.block())
            if ctx.var_assign() is not None:
                self.visitVar_assign(ctx.var_assign())
            condition_result = self.visitCondition(ctx.loop_condition().condition())

    @override
    def visitVar(self, ctx: ignoreParser.VarContext):
        # Normally it would evaluate expression that gives value to a new variable
        # It is already done in the `self.visitVarDecl` function. Can safely om
        return self.visitVarDecl(ctx.varDecl())

    @override
    def visitFunction(self, ctx: ignoreParser.FunctionContext):
        function_info = self.variables[ctx]
        var_name = ctx.FUNCTION_NAME().getText()[5:]

        self.current_env.variables[var_name] = function_info
        return function_info

    @override
    def visitReturnStmt(self, ctx: ignoreParser.ReturnStmtContext):
        wrapped_expr_context = ctx.wrapped_expr()
        result = None
        if wrapped_expr_context is not None:
            result = self.visit(wrapped_expr_context.expr())
        EarlyExit.return_with(result)
