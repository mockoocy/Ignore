from copy import deepcopy
from typing import Any, Dict, override
from .generated.ignoreParser import ignoreParser
from .generated.ignoreParserListener import ignoreParserListener
from .stdlib import builtins
from .utils.VariableInfo import Valid_Types, VariableInfo


class Listener(ignoreParserListener):

    def __init__(self):
        self.variables: Dict[str, Any] = deepcopy(builtins)

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
    def enterVarDecl(self, ctx: ignoreParser.VarDeclContext):
        var_name = str(ctx.FUNCTION_NAME())[5:]
        var_expression = ctx.parentCtx.wrapped_expr().expr()

        # dodanie typu
        if ctx.VAR_DECL_TYPE() != None:
            var_type = str(ctx.VAR_DECL_TYPE())[5:]
            if (
                var_type not in Valid_Types.keys()
            ):  # sprawdzenie czy typ jest wspierany przez język
                raise TypeError(f"type {var_name} is not supported!")
        else:  # jesli typ nie był podany to narazie None (w wizytorze automatycznie bedzie przypisany)
            var_type = None

        # sprawdzenie czy istnieje taka zmienna
        if var_name not in self.variables:
            # dodanie zmiennych do slownika wraz z typem bez wartosci
            self.variables[var_name] = VariableInfo(
                value=None,
                expression=var_expression,
                var_decl=ctx,
                type=var_type,
            )  #
            print(
                f"assigned {var_name} with value {None} and type={var_type}, is_evaluated = {self.variables[var_name].was_evaluated} "
            )
        else:
            # wyrzucenie błędu gdy próbujemy redeklarować zmienną
            raise ReferenceError(f"variable {var_name} is already defined!")

