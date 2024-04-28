from typing import Any, Dict, override

from .generated.ignoreParser import ignoreParser
from .generated.ignoreParserVisitor import ignoreParserVisitor
from .utils.evaluate import (
    evaluate_expr,
    evaluate_functioncall,
    evaluate_literal,
    evaluate_var_decl,
)


class Visitor(ignoreParserVisitor):

    def __init__(self, variables: Dict[str, Any]):
        # By quick glance at parent classes, super class does define __init__, so no need to call super() there
        self.variables = variables
        super().__init__()  # Call parent class constructor

    @override
    def visitLiteral(self, ctx: ignoreParser.LiteralContext):
        return evaluate_literal(ctx)

    @override
    def visitFunctionCall(self, ctx: ignoreParser.FunctionCallContext):
        return evaluate_functioncall(ctx, self.variables)

    @override
    def visitExpr(self, ctx: ignoreParser.ExprContext):
        return evaluate_expr(ctx, self.variables)

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
        for elif_ctx in ctx.elif_statement():
            evaluated = self.visitElif_statement(elif_ctx)
            if not evaluated: break
        if ctx.else_statement() and not evaluated: 
            self.visitElse_statement(ctx.else_statement())


    @override
    def visitVarDecl(self, ctx: ignoreParser.VarDeclContext):
        evaluate_var_decl(ctx, self.variables)

    @override 
    def visitVar(self, ctx: ignoreParser.VarContext):
        # Normally it would evaluate expression that gives value to a new variable
        # It is already done in the `self.visitVarDecl` function. Can safely omit.
        pass
