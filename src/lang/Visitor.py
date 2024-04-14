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
        ctx.evaluate()


    @override
    def visitFunctionCall(self, ctx: ignoreParser.FunctionCallContext):
        return ctx.evaluate()
