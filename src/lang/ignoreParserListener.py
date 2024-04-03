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
        print("\x1b[6;30;42m" + "Thank you for using Ignore language! You are really awesome" +"\x1b[0m")
        pass

    # Exit a parse tree produced by ignoreParser#program.
    def exitProgram(self, ctx:ignoreParser.ProgramContext):
        pass


    # Enter a parse tree produced by ignoreParser#statement.
    def enterStatement(self, ctx:ignoreParser.StatementContext):
        print("enter statement")
        pass

    # Exit a parse tree produced by ignoreParser#statement.
    def exitStatement(self, ctx:ignoreParser.StatementContext):
        print("exitStatement")
        pass


    # Enter a parse tree produced by ignoreParser#property.
    def enterProperty(self, ctx:ignoreParser.PropertyContext):
        
        print("enterProperty")
        pass

    # Exit a parse tree produced by ignoreParser#property.
    def exitProperty(self, ctx:ignoreParser.PropertyContext):
        
        print("exitProperty")
        pass


    # Enter a parse tree produced by ignoreParser#endTag.
    def enterEndTag(self, ctx:ignoreParser.EndTagContext):
        
        print("enterEndTag")
        pass

    # Exit a parse tree produced by ignoreParser#endTag.
    def exitEndTag(self, ctx:ignoreParser.EndTagContext):
        
        print("exitEndTag")
        pass


    # Enter a parse tree produced by ignoreParser#startTag.
    def enterStartTag(self, ctx:ignoreParser.StartTagContext):
        
        print("enterStartTag")
        pass

    # Exit a parse tree produced by ignoreParser#startTag.
    def exitStartTag(self, ctx:ignoreParser.StartTagContext):
        
        print("exitStartTag")
        pass


    # Enter a parse tree produced by ignoreParser#block.
    def enterBlock(self, ctx:ignoreParser.BlockContext):
        
        print("enterBlock")
        pass

    # Exit a parse tree produced by ignoreParser#block.
    def exitBlock(self, ctx:ignoreParser.BlockContext):
        
        print("exitBlock")
        pass


    # Enter a parse tree produced by ignoreParser#functionCall.
    def enterFunctionCall(self, ctx:ignoreParser.FunctionCallContext):

        print("enterFunctionCall")
        function_name = str(ctx.NAME())
        argument = str(ctx.expr().evaluate()) # only 1-arg functions allowed for now


        if function_name not in self.variables.keys():
            raise ValueError(f"function not defined {function_name}")
        return self.variables[function_name](argument)

    # Exit a parse tree produced by ignoreParser#functionCall.
    def exitFunctionCall(self, ctx:ignoreParser.FunctionCallContext):
        
        print("exitFunctionCall")
        pass


    # Enter a parse tree produced by ignoreParser#functionStart.
    def enterFunctionStart(self, ctx:ignoreParser.FunctionStartContext):
        # self.variable[functionanme] = funkcja
        print("enterFunctionStart")
        pass

    # Exit a parse tree produced by ignoreParser#functionStart.
    def exitFunctionStart(self, ctx:ignoreParser.FunctionStartContext):
        
        print("exitFunctionStart")
        pass


    # Enter a parse tree produced by ignoreParser#function.
    def enterFunction(self, ctx:ignoreParser.FunctionContext):
        
        print("enterFunction")
        pass

    # Exit a parse tree produced by ignoreParser#function.
    def exitFunction(self, ctx:ignoreParser.FunctionContext):
        
        print("exitFunction")
        pass


    # Enter a parse tree produced by ignoreParser#condition.
    def enterCondition(self, ctx:ignoreParser.ConditionContext):
        
        print("enterCondition")
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

    def exitVar(self, ctx: ignoreParser.VarContext):
        pass
    
    def enterVar(self, ctx: ignoreParser.VarContext):
        pass

del ignoreParser