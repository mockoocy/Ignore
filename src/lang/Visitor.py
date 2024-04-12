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

    variables: Dict[str, Any] = builtins
    """
        stores our var decls. For now format: name -> value.
        May move to format name -> variableSpecification 
        (whatever it would be) if convenient.
        By default stores many python functions.
    """

    @override
    def visitProgram(self, ctx: ignoreParser.ProgramContext):
        print("sieman")
        print(self.visitChildren(ctx))
        return self.visitChildren(ctx)

    @override
    def visitExpr(self, ctx: ignoreParser.ExprContext):
        return ctx.expr().evaluate()

    @override
    def visitFunctionCall(self, ctx: ignoreParser.FunctionCallContext):
        print("asasd")
        function_name = str(ctx.NAME())
        # I think we will want to use this kind of syntax now
        # It seems to be pattern to work with visitors in antlr4 isntead of accessing ctx directly.
        argument = self.visitExpr(ctx.expr())  # only 1-arg functions allowed for now
        if function_name not in self.variables.keys():
            raise ValueError(f"function not defined {function_name}")
        return self.variables[function_name](argument)

    @override
    def visitCondition(self, ctx: ignoreParser.ConditionContext):
        return super().visitCondition(ctx)

    @override
    def visitControl_statement(self, ctx: ignoreParser.Control_statementContext):
        return super().visitControl_statement(ctx)
