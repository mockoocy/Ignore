# Generated from src/grammar/ignoreParser.g4 by ANTLR 4.13.1

from typing import Any, Dict
from stdlib import builtins
from antlr4 import *
if "." in __name__:
    from .ignoreParser import ignoreParser
else:
    from ignoreParser import ignoreParser


# This class defines a complete listener for a parse tree produced by ignoreParser.
class ignoreParserListener(ParseTreeListener):

    variables: Dict[str, Any] = builtins 
    """
        stores our var decls. For now format: name -> value.
        May move to format name -> variableSpecification 
        (whatever it would be) if convenient.
        By default stores many python functions.
    """

    # Enter a parse tree produced by ignoreParser#literalNumeric.
    def enterLiteralNumeric(self, ctx:ignoreParser.LiteralNumericContext):
        pass

    # Exit a parse tree produced by ignoreParser#literalNumeric.
    def exitLiteralNumeric(self, ctx:ignoreParser.LiteralNumericContext):
        pass


    # Enter a parse tree produced by ignoreParser#literal.
    def enterLiteral(self, ctx:ignoreParser.LiteralContext):
        pass

    # Exit a parse tree produced by ignoreParser#literal.
    def exitLiteral(self, ctx:ignoreParser.LiteralContext):
        pass


    # Enter a parse tree produced by ignoreParser#program.
    def enterProgram(self, ctx:ignoreParser.ProgramContext):
        pass

    # Exit a parse tree produced by ignoreParser#program.
    def exitProgram(self, ctx:ignoreParser.ProgramContext):
        pass


    # Enter a parse tree produced by ignoreParser#statement.
    def enterStatement(self, ctx:ignoreParser.StatementContext):
        pass

    # Exit a parse tree produced by ignoreParser#statement.
    def exitStatement(self, ctx:ignoreParser.StatementContext):
        pass


    # Enter a parse tree produced by ignoreParser#property.
    def enterProperty(self, ctx:ignoreParser.PropertyContext):
        pass

    # Exit a parse tree produced by ignoreParser#property.
    def exitProperty(self, ctx:ignoreParser.PropertyContext):
        pass


    # Enter a parse tree produced by ignoreParser#endTag.
    def enterEndTag(self, ctx:ignoreParser.EndTagContext):
        pass

    # Exit a parse tree produced by ignoreParser#endTag.
    def exitEndTag(self, ctx:ignoreParser.EndTagContext):
        pass


    # Enter a parse tree produced by ignoreParser#startTag.
    def enterStartTag(self, ctx:ignoreParser.StartTagContext):
        pass

    # Exit a parse tree produced by ignoreParser#startTag.
    def exitStartTag(self, ctx:ignoreParser.StartTagContext):
        pass


    # Enter a parse tree produced by ignoreParser#block.
    def enterBlock(self, ctx:ignoreParser.BlockContext):
        pass

    # Exit a parse tree produced by ignoreParser#block.
    def exitBlock(self, ctx:ignoreParser.BlockContext):
        pass


    # Enter a parse tree produced by ignoreParser#functionCall.
    def enterFunctionCall(self, ctx:ignoreParser.FunctionCallContext):

        function_name = str(ctx.NAME())
        argument = str(ctx.expr()) # only 1-arg functions allowed for now
        if function_name not in self.variables.keys():
            raise ValueError(f"function not defined {function_name}")
        print(f"calling {function_name} with {argument}")
        return self.variables[function_name](argument)

    # Exit a parse tree produced by ignoreParser#functionCall.
    def exitFunctionCall(self, ctx:ignoreParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by ignoreParser#functionStart.
    def enterFunctionStart(self, ctx:ignoreParser.FunctionStartContext):
        pass

    # Exit a parse tree produced by ignoreParser#functionStart.
    def exitFunctionStart(self, ctx:ignoreParser.FunctionStartContext):
        pass


    # Enter a parse tree produced by ignoreParser#function.
    def enterFunction(self, ctx:ignoreParser.FunctionContext):
        pass

    # Exit a parse tree produced by ignoreParser#function.
    def exitFunction(self, ctx:ignoreParser.FunctionContext):
        pass


    # Enter a parse tree produced by ignoreParser#condition.
    def enterCondition(self, ctx:ignoreParser.ConditionContext):
        pass

    # Exit a parse tree produced by ignoreParser#condition.
    def exitCondition(self, ctx:ignoreParser.ConditionContext):
        pass


    # Enter a parse tree produced by ignoreParser#if.
    def enterIf(self, ctx:ignoreParser.IfContext):
        print(f"if {ctx.condition}")
        pass

    # Exit a parse tree produced by ignoreParser#if.
    def exitIf(self, ctx:ignoreParser.IfContext):
        print(f"endif {ctx.condition}")
        pass


    # Enter a parse tree produced by ignoreParser#if_statement.
    def enterIf_statement(self, ctx:ignoreParser.If_statementContext):
        pass

    # Exit a parse tree produced by ignoreParser#if_statement.
    def exitIf_statement(self, ctx:ignoreParser.If_statementContext):
        pass


    # Enter a parse tree produced by ignoreParser#elif.
    def enterElif(self, ctx:ignoreParser.ElifContext):
        pass

    # Exit a parse tree produced by ignoreParser#elif.
    def exitElif(self, ctx:ignoreParser.ElifContext):
        pass


    # Enter a parse tree produced by ignoreParser#elif_statement.
    def enterElif_statement(self, ctx:ignoreParser.Elif_statementContext):
        pass

    # Exit a parse tree produced by ignoreParser#elif_statement.
    def exitElif_statement(self, ctx:ignoreParser.Elif_statementContext):
        pass


    # Enter a parse tree produced by ignoreParser#else_statement.
    def enterElse_statement(self, ctx:ignoreParser.Else_statementContext):
        pass

    # Exit a parse tree produced by ignoreParser#else_statement.
    def exitElse_statement(self, ctx:ignoreParser.Else_statementContext):
        pass


    # Enter a parse tree produced by ignoreParser#control_statement.
    def enterControl_statement(self, ctx:ignoreParser.Control_statementContext):
        pass

    # Exit a parse tree produced by ignoreParser#control_statement.
    def exitControl_statement(self, ctx:ignoreParser.Control_statementContext):
        pass


    # Enter a parse tree produced by ignoreParser#expr.
    def enterExpr(self, ctx:ignoreParser.ExprContext):
        pass

    # Exit a parse tree produced by ignoreParser#expr.
    def exitExpr(self, ctx:ignoreParser.ExprContext):
        pass


    # Enter a parse tree produced by ignoreParser#wrapped_expr.
    def enterWrapped_expr(self, ctx:ignoreParser.Wrapped_exprContext):
        pass

    # Exit a parse tree produced by ignoreParser#wrapped_expr.
    def exitWrapped_expr(self, ctx:ignoreParser.Wrapped_exprContext):
        pass



del ignoreParser