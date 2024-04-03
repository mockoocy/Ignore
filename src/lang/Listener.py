from stdlib import builtins 
from typing import Any, Dict, override
from sys import path
from generated.ignoreParserListener import ignoreParserListener
from generated.ignoreParser import ignoreParser


class Listener(ignoreParserListener):


    variables: Dict[str, Any] = builtins 
    """
        stores our var decls. For now format: name -> value.
        May move to format name -> variableSpecification 
        (whatever it would be) if convenient.
        By default stores many python functions.
    """

    @override
    def enterProgram(self, ctx:ignoreParser.ProgramContext):
        print("\x1b[6;30;42m" + "Thank you for using Ignore language! You are really awesome" +"\x1b[0m")


    @override
    def enterFunctionCall(self, ctx:ignoreParser.FunctionCallContext):

        print("enterFunctionCall")
        function_name = str(ctx.NAME())
        argument = str(ctx.expr().evaluate()) # only 1-arg functions allowed for now


        if function_name not in self.variables.keys():
            raise ValueError(f"function not defined {function_name}")
        return self.variables[function_name](argument)
