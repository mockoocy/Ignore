from typing import Dict

from ..generated.ignoreParser import ignoreParser
from .VariableInfo import Valid_Types, Valid_Types_Reversed, VariableInfo


def evaluate_expr(expr: ignoreParser.ExprContext, variables: Dict[str, VariableInfo]):
    if expr.OPEN_PAREN() and expr.CLOSE_PAREN():
        return evaluate_expr(expr.expr(0), variables)
    if expr.literal() is not None:
        return evaluate_literal(expr.literal())
    elif expr.NAME() is not None:
        if str(expr.NAME()) not in variables.keys():
            raise ValueError(f"No such variable declared {str(expr.NAME())}")
        elif (
            str(expr.NAME()) in variables.keys()
            and variables[str(expr.NAME())].was_evaluated == False
        ):
            var_info = variables[str(expr.NAME())]
            evaluate_var_decl(var_info.var_decl, variables)
            return variables[str(expr.NAME())].value
        else:
            return variables[str(expr.NAME())].value

    elif expr.functionCall() is not None:
        # print(evaluate_functioncall(expr.functionCall(), variables))
        return evaluate_functioncall(expr.functionCall(), variables)
    elif (
        expr.ADD() is not None
        or expr.SUB() is not None
        or expr.MUL() is not None
        or expr.DIV() is not None
        or expr.MOD() is not None
        or expr.INT_DIV() is not None  # cant just omit this and go to ifs directly?
    ):

        left = evaluate_expr(expr.expr(0), variables)
        right = evaluate_expr(expr.expr(1), variables)

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
    elif expr.OPERATOR_COMPARE() is not None:
        left = evaluate_expr(expr.expr(0), variables)
        right = evaluate_expr(expr.expr(1), variables)
        if str(expr.OPERATOR_COMPARE()) == "==":
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
        left = evaluate_expr(expr.expr(0), variables)
        right = evaluate_expr(expr.expr(1), variables)
        if str(expr.OPERATOR_LOGIC()) == "&&":
            return left and right
        elif str(expr.OPERATOR_LOGIC()) == "||":
            return left or right
    else:

        raise NotImplementedError("Unsupported expression syntax")


def evaluate_literal(literal: ignoreParser.LiteralContext):

    if literal.LITERAL_STRING() is not None:
        raw_string = str(literal.LITERAL_STRING())
        return raw_string[1:-1]

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


def evaluate_functioncall(
    ctx: ignoreParser.FunctionCallContext, variables: Dict[str, VariableInfo]
):
    function_name = str(ctx.NAME())
    argument = evaluate_expr(
        ctx.expr(), variables
    )  # only 1-arg functions allowed for now
    if function_name not in variables:
        raise ValueError(f"function not defined {function_name}")
    return variables[function_name](argument)


def evaluate_var_decl(
    ctx: ignoreParser.VarDeclContext, variables: Dict[str, VariableInfo]
):
    var_name = str(ctx.FUNCTION_NAME())[5:]
    variable_info = variables.get(var_name)
    if variable_info.was_evaluated == True:
        return
    # sprawdzenie czy istnieje taka zmienna
    if variable_info is not None:
        expr_val = evaluate_expr(
            variable_info.expression, variables
        )  # obliczenie warotsci exprresion

        if variable_info.type != None:  # jesli typ był podany w deklaracji
            var_type = Valid_Types[variable_info.type]
            try:  # jesli nie castowalne na dany typ to zwroc type error
                variable_info.value = var_type(expr_val)  # castowanie na var_type
            except ValueError:
                raise TypeError(
                    f"could not cast value of {var_name} to type : {var_type}"
                )

        else:  # jesli nie podano typu to jest przypisywany domyslny dla zmiennej
            expr_val = evaluate_expr(variable_info.expression, variables)
            variable_info.type = Valid_Types_Reversed.get(type(expr_val))
            variable_info.value = expr_val
        variable_info.was_evaluated = True
        print(
            f"updated variables with variable {var_name}, of type {variable_info.type}, and value = {variable_info.value}"
        )
    else:
        raise NameError(f"variable {var_name} was not declared")
