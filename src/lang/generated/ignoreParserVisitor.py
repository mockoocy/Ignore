# Generated from src/grammar/ignoreParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ignoreParser import ignoreParser
else:
    from ignoreParser import ignoreParser

# This class defines a complete generic visitor for a parse tree produced by ignoreParser.

class ignoreParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ignoreParser#literalNumeric.
    def visitLiteralNumeric(self, ctx:ignoreParser.LiteralNumericContext):
        print("visiting")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#literal.
    def visitLiteral(self, ctx:ignoreParser.LiteralContext):
        print("visiting")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#program.
    def visitProgram(self, ctx:ignoreParser.ProgramContext):
        print("visiting!!!")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#statement.
    def visitStatement(self, ctx:ignoreParser.StatementContext):
        print("visiting")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#property.
    def visitProperty(self, ctx:ignoreParser.PropertyContext):
        print("visiting")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#endTag.
    def visitEndTag(self, ctx:ignoreParser.EndTagContext):
        print("visiting")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#startTag.
    def visitStartTag(self, ctx:ignoreParser.StartTagContext):
        print("visiting")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#block.
    def visitBlock(self, ctx:ignoreParser.BlockContext):
        print("visiting")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#functionCall.
    def visitFunctionCall(self, ctx:ignoreParser.FunctionCallContext):
        print("visiting")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#functionStart.
    def visitFunctionStart(self, ctx:ignoreParser.FunctionStartContext):
        print("visiting")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#function.
    def visitFunction(self, ctx:ignoreParser.FunctionContext):
        print("visiting")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#varDecl.
    def visitVarDecl(self, ctx:ignoreParser.VarDeclContext):
        print("visiting")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#var.
    def visitVar(self, ctx:ignoreParser.VarContext):
        print("visiting")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#condition.
    def visitCondition(self, ctx:ignoreParser.ConditionContext):
        print("visiting")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#if.
    def visitIf(self, ctx:ignoreParser.IfContext):
        print("visiting")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#if_statement.
    def visitIf_statement(self, ctx:ignoreParser.If_statementContext):
        print("visiting")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#elif.
    def visitElif(self, ctx:ignoreParser.ElifContext):
        print("visiting")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#elif_statement.
    def visitElif_statement(self, ctx:ignoreParser.Elif_statementContext):
        print("visiting")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#else_statement.
    def visitElse_statement(self, ctx:ignoreParser.Else_statementContext):
        print("visiting")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#control_statement.
    def visitControl_statement(self, ctx:ignoreParser.Control_statementContext):
        print("visiting")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#expr.
    def visitExpr(self, ctx:ignoreParser.ExprContext):
        print("visiting")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#wrapped_expr.
    def visitWrapped_expr(self, ctx:ignoreParser.Wrapped_exprContext):
        print("visiting")
        return self.visitChildren(ctx)



del ignoreParser