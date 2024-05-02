from typing import Any, Dict, override

from src.lang.utils.VariableInfo import Valid_Types, Valid_Types_Reversed, VariableInfo

from .generated.ignoreParser import ignoreParser
from .generated.ignoreParserVisitor import ignoreParserVisitor


class Visitor(ignoreParserVisitor):

    def __init__(self, variables: Dict[str, Any]):
        # By quick glance at parent classes, super class does define __init__, so no need to call super() there
        self.variables = variables
        super().__init__()  # Call parent class constructor

    @override
    def visitLiteral(self, ctx: ignoreParser.LiteralContext):
        literal = ctx
        if literal.LITERAL_STRING() is not None:
            raw_string = str(literal.LITERAL_STRING())
            return raw_string[1:-1] # removes quotes

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
    def visitFunctionCall(self, ctx: ignoreParser.FunctionCallContext):
        function_name = str(ctx.NAME())
        
        argument = self.visitExpr(ctx.expr())  # only 1-arg functions allowed for now
        if function_name not in self.variables:
            raise ValueError(f"function not defined {function_name}")
        return self.variables[function_name](argument)

    @override
    def visitExpr(self, ctx: ignoreParser.ExprContext):
        expr = ctx
        variables = self.variables
        if expr.OPEN_PAREN() and expr.CLOSE_PAREN():
            return self.visitExpr(expr.expr(0)) 
        if expr.literal() is not None:
            return self.visitLiteral(expr.literal())
        if expr.NAME() is not None:
            if str(expr.NAME()) not in variables.keys():
                raise ValueError(f"No such variable declared {str(expr.NAME())}")
            elif (
                str(expr.NAME()) in variables.keys()
                and variables[str(expr.NAME())].was_evaluated == False
            ):
                var_info = variables[str(expr.NAME())]
                self.visitVarDecl(var_info.var_decl)
                return variables[str(expr.NAME())].value
            else:
                return variables[str(expr.NAME())].value

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
            self.visitStatement(ctx.statement())
        return condition_result

    @override
    def visitElif_statement(self, ctx: ignoreParser.Elif_statementContext):
        condition_result = self.visitCondition(ctx.elif_().condition())
        if condition_result:
            return self.visitStatement(ctx.statement())
        return condition_result

    @override
    def visitElse_statement(self, ctx: ignoreParser.Else_statementContext):
        self.visitStatement(ctx.statement())

    @override
    def visitControl_statement(self, ctx: ignoreParser.Control_statementContext):
        evaluated = self.visitIf_statement(ctx.if_statement())
        if evaluated: return
        for elif_ctx in ctx.elif_statement():
            evaluated = self.visitElif_statement(elif_ctx)
            if evaluated: break
        if ctx.else_statement() and not evaluated: 
            self.visitElse_statement(ctx.else_statement())


    @override
    def visitVarDecl(self, ctx: ignoreParser.VarDeclContext):
        variables = self.variables
        var_name = str(ctx.FUNCTION_NAME())[5:]
        variable_info = variables.get(var_name, VariableInfo(var_name))
        if variable_info.was_evaluated == True:
            return variable_info
        
        variable_info.recursion_check += 1 
        if variable_info.recursion_check > 1:
            raise RecursionError(f"Circular dependency detected for variable {var_name}")
        expr_val = self.visitExpr(variable_info.expression)

        if variable_info.type != None:  # jesli typ był podany w deklaracji
            var_type = Valid_Types[variable_info.type]
            try:  # jesli nie castowalne na dany typ to zwroc type error
                variable_info.value = var_type(expr_val)  # castowanie na var_type
            except ValueError:
                raise TypeError(f"could not cast value of {var_name} to type : {var_type}")

        else:  # jesli nie podano typu to jest przypisywany domyslny dla zmiennej
            variable_info.type = Valid_Types_Reversed.get(type(expr_val))
            variable_info.value = expr_val
        variable_info.was_evaluated = True
        print(
            f"updated variables with variable {var_name}, of type {variable_info.type}, and value = {variable_info.value}"
        )
        return variable_info

    @override 
    def visitVar(self, ctx: ignoreParser.VarContext):
        # Normally it would evaluate expression that gives value to a new variable
        # It is already done in the `self.visitVarDecl` function. Can safely om
        return self.visitVarDecl(ctx.varDecl())
