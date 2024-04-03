"""This cursed file is a workaround around the fact that any change to grammar causes regeneration 
    of antlr files. A reccomended apprach is to create a subclass that is overriding methods
    exposed by the generated classes. While this approach works well with Listeners, there is no simple way
    to override nested ParserRuleContext subclasses of the ignoreParser classes. For example 
    overriding ExprContext in custom Parser class would not make functionCallContext's expr() method return 
    the overridden class member:) 
"""

from generated.ignoreParser import ignoreParser



def evaluate_expr(expr: ignoreParser.ExprContext):
    if expr.literal() is not None:
        print("LITERAL!")
        return expr.literal().evaluate()

    elif expr.functionCall() is not None:
        print("function")
        return expr.functionCall().evaluate()

    elif expr.ADD() is not None or expr.SUB() is not None or expr.MUL() is not None or expr.DIV() is not None:
        print("arithmetic")
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


def evaluate_literal(literal: ignoreParser.LiteralContext):

    if literal.LITERAL_STRING() is not None:
        raw_string = str(literal.LITERAL_STRING())
        print("literal string")
        return raw_string[1:-1] 
    
    elif literal.LITERAL_INT() is not None:
        print("literal int")
        return str(literal.LITERAL_INT())
    
    elif literal.LITERAL_FLOAT() is not None:
        print("literal float")
        return str(literal.LITERAL_FLOAT())
    
    # not working!
    elif literal.LITERAL_BOOL() is not None:
        print("literal bool")
        return str(literal.LITERAL_BOOL())
    
    else:
        raise NotImplementedError("Unsupported literal type")

ignoreParser.ExprContext.evaluate = evaluate_expr
ignoreParser.LiteralContext.evaluate = evaluate_literal
Parser = ignoreParser