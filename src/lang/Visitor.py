from stdlib import builtins 
from typing import Any, Dict, override
from generated.ignoreParserVisitor import ignoreParserVisitor
from generated.ignoreParser import ignoreParser
from typing import Dict, Any

class Visitor(ignoreParserVisitor):

    def __init__(self, variables: Dict[str, Any]):
        # By quick glance at parent classes, super class does define __init__, so no need to call super() there
        self.variables = variables

    variables: Dict[str, Any] = builtins 
    """
        stores our var decls. For now format: name -> value.
        May move to format name -> variableSpecification 
        (whatever it would be) if convenient.
        By default stores many python functions.
    """


    @override
    def visitFunctionCall(self, ctx:ignoreParser.FunctionCallContext):
        function_name = str(ctx.NAME())
        argument = ctx.expr().evaluate() # only 1-arg functions allowed for now
        if function_name not in self.variables.keys():
            raise ValueError(f"function not defined {function_name}")
        return self.variables[function_name](argument)
