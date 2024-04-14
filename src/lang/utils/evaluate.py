from typing import Dict
from generated.ignoreParser import ignoreParser
from utils.VariableInfo import VariableInfo


def evaluate_expr(expr: ignoreParser.ExprContext, variables: Dict[str, VariableInfo]):
    if expr.literal() is not None:
        return evaluate_literal(expr.literal())
    elif expr.NAME() is not None:
        if str(expr.NAME()) not in variables.keys():
            raise ValueError(f"No such variable declared {str(expr.NAME())}")
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
        or expr.INT_DIV() is not None # cant just omit this and go to ifs directly?
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


def evaluate_functioncall(ctx: ignoreParser.FunctionCallContext, variables: Dict[str, VariableInfo]):
    function_name = str(ctx.NAME())
    argument = evaluate_expr(ctx.expr(), variables)  # only 1-arg functions allowed for now
    if function_name not in variables:
        raise ValueError(f"function not defined {function_name}")
    return variables[function_name](argument)