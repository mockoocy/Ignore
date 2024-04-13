"""This cursed file is a workaround around the fact that VariableInfo change to grammar causes regeneration 
    of antlr files. A reccomended apprach is to create a subclass that is overriding methods
    exposed by the generated classes. While this approach works well with Listeners, there is no simple way
    to override nested ParserRuleContext subclasses of the ignoreParser classes. For example 
    overriding ExprContext in custom Parser class would not make functionCallContext's expr() method return 
    the overridden class member:) 
"""

from typing import Dict
from generated.ignoreParser import ignoreParser
from Listener import Listener
from utils.VariableInfo import VariableInfo


def evaluate_expr(expr: ignoreParser.ExprContext, variables: Dict[str, VariableInfo]):

    if expr.literal() is not None:
        return expr.literal().evaluate()

    elif expr.NAME() is not None:
        if str(expr.NAME()) not in variables.keys():
            raise ValueError(f"No such variable declared {str(expr.NAME())}")
        return variables[str(expr.NAME())].value

    elif expr.functionCall() is not None:
        return expr.functionCall().evaluate()

    elif (
        expr.ADD() is not None
        or expr.SUB() is not None
        or expr.MUL() is not None
        or expr.DIV() is not None
    ):
        left = expr.expr(0).evaluate()
        right = expr.expr(1).evaluate()

        if expr.ADD() is not None:
            return left + right
        elif expr.SUB() is not None:
            return left - right
        elif expr.MUL() is not None:
            return left * right
        elif expr.DIV() is not None:
            return left / right  # division by zero?!
    elif expr.OPERATOR_COMPARE() is not None:
        left = expr.expr(0).evaluate()
        right = expr.expr(1).evaluate()
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
        left = expr.expr(0).evaluate()
        right = expr.expr(1).evaluate()
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
    argument = ctx.expr().evaluate()  # only 1-arg functions allowed for now
    if function_name not in variables:
        raise ValueError(f"function not defined {function_name}")
    return variables[function_name](argument)

ignoreParser.ExprContext.evaluate = lambda expr: evaluate_expr(expr, Listener.variables)
ignoreParser.LiteralContext.evaluate = evaluate_literal
ignoreParser.FunctionCallContext.evaluate = lambda call: evaluate_functioncall(call, Listener.variables)
# zacomentowalem mozna by przepisac cale evaluate_expr
# ale to kopiowanie kodu bezsensu
# wystarczy zamiast wrapped_expr.evaluate() pisac wrapped_expression.expression().evaluate()
# ignoreParser.Wrapped_exprContext.evaluate = evaluate_wrapped_expr
Parser = ignoreParser
