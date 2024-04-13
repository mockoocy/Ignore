from utils.VariableInfo import VariableInfo
from stdlib import builtins
from typing import Any, Dict, override
from generated.ignoreParserListener import ignoreParserListener
from generated.ignoreParser import ignoreParser


class Listener(ignoreParserListener):

    variables: Dict[str, Any] = builtins
    current_scope = 0
    """
        stores our var decls. For now format: name -> value.
        May move to format name -> variableSpecification 
        (whatever it would be) if convenient.
        By default stores many python functions.
    """

    @override
    def enterProgram(self, ctx: ignoreParser.ProgramContext):
        print(
            "\x1b[6;30;42m"
            + "Thank you for using Ignore language! You are really awesome"
            + "\x1b[0m"
        )

    @override
    def exitProgram(self, ctx: ignoreParser.ProgramContext):
        print("\x1b[46;20;20m" + "Ended first phase of interpreting" + "\x1b[0m")

    @override
    def enterFunction(self, ctx: ignoreParser.FunctionContext):
        self.current_scope += 1
        return super().enterFunction(ctx)
    
    def exitFunction(self, ctx: ignoreParser.FunctionContext):
        # should be done for more blocks
        self.current_scope -= 1
        return super().exitFunction(ctx)

    @override
    def enterVarDecl(self, ctx: ignoreParser.VarDeclContext):
        var_name = str(ctx.FUNCTION_NAME())[5:]
        expression = ctx.parentCtx.wrapped_expr().expr().evaluate()


        if var_name not in self.variables:
            self.variables[var_name] = VariableInfo(expression, scope=self.current_scope)
        else:
            raise ReferenceError(f"variable {var_name} is already defined!")
        # jesli expression to name to byla proba przypisania wartosci jednej zmiennej do drugiej
        # ... wspieramy przypisania?
        # if ctx.parentCtx.wrapped_expr().expr().NAME() is not None:
        #     if str(expression) not in self.variables.keys():
        #         raise ValueError(f"No such variable declared {str(expression)}")
        #     self.variables[var_name] = self.variables[str(expression)]
        # else:
        #     self.variables[var_name] = expression
