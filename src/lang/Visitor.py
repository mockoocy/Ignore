from stdlib import builtins
from typing import Any, Dict, override
from generated.ignoreParserVisitor import ignoreParserVisitor
from generated.ignoreParser import ignoreParser
from typing import Dict, Any

class Visitor(ignoreParserVisitor):

    def __init__(self, variables: Dict[str, Any]):
        # By quick glance at parent classes, super class does define __init__, so no need to call super() there
        self.variables = variables
        super().__init__()  # Call parent class constructor


    @override
    def visitLiteral(self, ctx: ignoreParser.LiteralContext):
        if ctx.LITERAL_STRING() is not None:
            raw_string = str(ctx.LITERAL_STRING())
            return raw_string[1:-1]

        elif ctx.LITERAL_INT() is not None:
            return int(str(ctx.LITERAL_INT()))

        elif ctx.LITERAL_FLOAT() is not None:
            return float(str(ctx.LITERAL_FLOAT()))

        elif ctx.LITERAL_BOOL() is not None:
            bool_str = str(ctx.LITERAL_BOOL())
            if bool_str == "True":
                return True
            elif bool_str == "False":
                return False

        else:
            raise NotImplementedError("Unsupported literal type")

    @override
    def visitProgram(self, ctx: ignoreParser.ProgramContext):
        return self.visitChildren(ctx)

    @override
    def visitExpr(self, ctx: ignoreParser.ExprContext):
        return ctx.evaluate()

    @override
    def visitFunctionCall(self, ctx: ignoreParser.FunctionCallContext):
        return ctx.evaluate()
    
    @override
    def visitWrapped_expr(self, ctx: ignoreParser.Wrapped_exprContext):
        return super().visitWrapped_expr(ctx)

    @override
    def visitBlock(self, ctx: ignoreParser.BlockContext):
        return super().visitBlock(ctx)

    @override
    def visitCondition(self, ctx: ignoreParser.ConditionContext):
        return super().visitCondition(ctx)

    @override
    def visitControl_statement(self, ctx: ignoreParser.Control_statementContext):
        return super().visitControl_statement(ctx)
