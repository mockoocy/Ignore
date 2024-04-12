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

    """
        stores our var decls. For now format: name -> value.
        May move to format name -> variableSpecification 
        (whatever it would be) if convenient.
        By default stores many python functions.
    """

    # @override
    # def visitTerminal(self, node):
    #     print(f">>{node}")
    #     return super().visitTerminal(node)

    # @override
    # def visitLiteral(self, ctx: ignoreParser.LiteralContext):
    #     if ctx.LITERAL_STRING() is not None:
    #         raw_string = str(ctx.LITERAL_STRING())
    #         return raw_string[1:-1]

    #     elif ctx.LITERAL_INT() is not None:
    #         return int(str(ctx.LITERAL_INT()))

    #     elif ctx.LITERAL_FLOAT() is not None:
    #         return float(str(ctx.LITERAL_FLOAT()))

    #     elif ctx.LITERAL_BOOL() is not None:
    #         bool_str = str(ctx.LITERAL_BOOL())
    #         if bool_str == "True":
    #             return True
    #         elif bool_str == "False":
    #             return False

    #     else:
    #         raise NotImplementedError("Unsupported literal type")

    # @override
    # def visitProgram(self, ctx: ignoreParser.ProgramContext):
    #     print("sieman")
    #     print(self.visitChildren(ctx))
    #     return self.visitChildren(ctx)

    # @override
    # def visitExpr(self, ctx: ignoreParser.ExprContext):
    #     print("exprs")
    #     print(ctx.expr().__dict__)
    #     return ctx.expr().evaluate()

    # @override
    # def visitFunctionCall(self, ctx: ignoreParser.FunctionCallContext):
    #     print("asasd")
    #     function_name = str(ctx.NAME())
    #     # I think we will want to use this kind of syntax now
    #     # It seems to be pattern to work with visitors in antlr4 isntead of accessing ctx directly.
    #     argument = self.visitExpr(ctx.expr())  # only 1-arg functions allowed for now
    #     if function_name not in self.variables.keys():
    #         raise ValueError(f"function not defined {function_name}")
    #     return self.variables[function_name](argument)

    # @override
    # def visitWrapped_expr(self, ctx: ignoreParser.Wrapped_exprContext):
    #     print("wrapped")
    #     return super().visitWrapped_expr(ctx)

    # @override
    # def visitBlock(self, ctx: ignoreParser.BlockContext):
    #     print("blok")
    #     return super().visitBlock(ctx)

    # @override
    # def visitCondition(self, ctx: ignoreParser.ConditionContext):
    #     return super().visitCondition(ctx)

    # @override
    # def visitControl_statement(self, ctx: ignoreParser.Control_statementContext):
    #     return super().visitControl_statement(ctx)
