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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#literal.
    def visitLiteral(self, ctx:ignoreParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#functionCall.
    def visitFunctionCall(self, ctx:ignoreParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#function.
    def visitFunction(self, ctx:ignoreParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#returnStmt.
    def visitReturnStmt(self, ctx:ignoreParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#varDecl.
    def visitVarDecl(self, ctx:ignoreParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#var.
    def visitVar(self, ctx:ignoreParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#var_assign.
    def visitVar_assign(self, ctx:ignoreParser.Var_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#while_loop.
    def visitWhile_loop(self, ctx:ignoreParser.While_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#for_loop.
    def visitFor_loop(self, ctx:ignoreParser.For_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#loop_condition.
    def visitLoop_condition(self, ctx:ignoreParser.Loop_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#loop_init.
    def visitLoop_init(self, ctx:ignoreParser.Loop_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#condition.
    def visitCondition(self, ctx:ignoreParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#if.
    def visitIf(self, ctx:ignoreParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#if_statement.
    def visitIf_statement(self, ctx:ignoreParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#elif.
    def visitElif(self, ctx:ignoreParser.ElifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#elif_statement.
    def visitElif_statement(self, ctx:ignoreParser.Elif_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#else_statement.
    def visitElse_statement(self, ctx:ignoreParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#control_statement.
    def visitControl_statement(self, ctx:ignoreParser.Control_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#program.
    def visitProgram(self, ctx:ignoreParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#property.
    def visitProperty(self, ctx:ignoreParser.PropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#endTag.
    def visitEndTag(self, ctx:ignoreParser.EndTagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#startTag.
    def visitStartTag(self, ctx:ignoreParser.StartTagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#statement.
    def visitStatement(self, ctx:ignoreParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#block.
    def visitBlock(self, ctx:ignoreParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#expr.
    def visitExpr(self, ctx:ignoreParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ignoreParser#wrapped_expr.
    def visitWrapped_expr(self, ctx:ignoreParser.Wrapped_exprContext):
        return self.visitChildren(ctx)



del ignoreParser