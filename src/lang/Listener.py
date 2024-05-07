from copy import deepcopy
from typing import Dict, List, override

from src.lang.utils.Environment import Environment

from .generated.ignoreParser import ignoreParser
from .generated.ignoreParserListener import ignoreParserListener
from .stdlib import global_env
from .utils.VariableInfo import Valid_Types, VariableInfo


class Listener(ignoreParserListener):

    def __init__(self):
        self.env_stack: List[Environment] = [deepcopy(global_env)]
        self.current_depth = 0
        self.variables: Dict[object(), VariableInfo] = {}

        """
            stores our var decls. For now format: name -> value.
            May move to format name -> variableSpecification 
            (whatever it would be) if convenient.
            By default stores many python functions.
        """

    def _get_var_type(self, ctx: ignoreParser.VarDeclContext):
        if (
            ctx.VAR_DECL_TYPE() is None
        ):  # jesli typ nie był podany to narazie None (w wizytorze automatycznie bedzie przypisany)
            return None
        var_type = str(ctx.VAR_DECL_TYPE())[5:]
        if (
            var_type not in Valid_Types.keys()
        ):  # sprawdzenie czy typ jest wspierany przez język
            raise TypeError(f"type {var_type} is not supported!")
        return var_type

    def _add_new_var(
        self, var_name: str, var_type: str | None, ctx: ignoreParser.VarDeclContext
    ):
        # sprawdzenie czy istnieje taka zmienna
        current_env = self.env_stack[-1]
        if var_name in current_env.variables:
            raise ReferenceError(f"variable {var_name} is already defined!")
            # dodanie zmiennych do slownika wraz z typem bez wartosci
        new_var = VariableInfo(
            value=None,
            depth=self.current_depth,
            var_decl=ctx,
            type=var_type,
        )
        #print(
        #    f"assigned {var_name} with value {None} and type={var_type}, is_evaluated = {new_var.was_evaluated} "
       #  )
        current_env.variables[var_name] = new_var
        self.variables[ctx] = new_var

    def _extract_function_params(self, ctx):
        params = {}
        # for param_ctx in ctx.FUNCTION_PARAM():
        param_name, param_type = ctx.FUNCTION_PARAM().getText().split(':')
        params[param_name] = param_type
        return params

    def _add_new_function(self, function_name, params, body, return_type, ctx: ignoreParser.FunctionContext):
        current_env = self.env_stack[-1] 
        if function_name in current_env.variables:
            raise ReferenceError(f"Function '{function_name}' already defined")
        new_function = VariableInfo( 
            value = None,
            type = 'Function',
            is_function=True,
            body=body,
            depth = self.current_depth,
            var_decl = ctx,
            return_type=return_type,
        )
        current_env.variables[function_name] = new_function
        self.variables[ctx] = new_function
        # print(f"Defined function '{function_name}' with parameters {params} and return type '{return_type}'")


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
    def enterBlock(self, ctx: ignoreParser.BlockContext):
        self.current_depth += 1
        current_stack = self.env_stack[-1] if len(self.env_stack) > 0 else None
        self.env_stack.append(Environment(enclosing=current_stack, variables={}))
        return super().enterBlock(ctx)

    @override
    def exitBlock(self, ctx: ignoreParser.BlockContext):
        self.current_depth -= 1
        self.env_stack.pop()
        return super().exitBlock(ctx)

    @override
    def enterVarDecl(self, ctx: ignoreParser.VarDeclContext):
        var_name = ctx.FUNCTION_NAME().getText()[5:]
        # dodanie typu
        var_type = self._get_var_type(ctx)
        self._add_new_var(var_name, var_type, ctx)

    @override 
    def enterFunction(self, ctx: ignoreParser.FunctionContext):
        # print("ENTER FUNCTION!!! W LISTENERZE")
        function_name = ctx.FUNCTION_NAME().getText()[5:]
        params = self._extract_function_params(ctx)
        body = ctx.block()[0] 
        return_type = ctx.FUNCTION_RET_TYPE().getText().split('=')[1] if ctx.FUNCTION_RET_TYPE() else None
        self._add_new_function(function_name, params, body, return_type, ctx)
    