from copy import deepcopy
from typing import Dict, List, override

from src.lang.errors.utils import IgnoreException
from src.lang.utils.Environment import Environment
from src.lang.utils.FunctionArgument import FunctionArgument
from src.lang.utils.FunctionInfo import FunctionInfo
from src.lang.utils.types import TypedParam, VarDeclDict

from .generated.ignoreParser import ignoreParser
from .generated.ignoreParserListener import ignoreParserListener
from .stdlib import global_env
from .utils.VariableInfo import Valid_Types, VariableInfo
from antlr4.tree.Tree import TerminalNodeImpl

class Listener(ignoreParserListener):

    def __init__(self, filename):
        self.filename = filename
        self.env_stack: List[Environment] = [deepcopy(global_env)]
        self.variables: VarDeclDict = {}
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
        ):  # sprawdzenie czy typ jest wspierany przez 
            type_token = ctx.VAR_DECL_TYPE().getSymbol()
            raise IgnoreException(
                TypeError,
                f"type {var_type} is not supported!",
                self.filename,
                type_token
            )
        return var_type

    def _add_new_var(
        self, var_name: str, var_type: str | None, ctx: ignoreParser.VarDeclContext
    ):
        # sprawdzenie czy istnieje taka zmienna
        current_env = self.env_stack[-1]
        if var_name in current_env.variables:
            # raise ReferenceError(f"variable {var_name} is already defined!")
            var_decl_token = ctx.VAR_DECL().getSymbol()
            raise IgnoreException(
                ReferenceError,
                f"Variable '{var_name}' already defined",
                self.filename,
                var_decl_token
            )
            # dodanie zmiennych do slownika wraz z ty
            # pem bez wartosci
        new_var = VariableInfo(
            value=None,
            var_decl=ctx,
            type=var_type,
        )
        current_env.variables[var_name] = new_var
        self.variables[ctx] = new_var


    def _extract_function_param(self, param_node: TerminalNodeImpl) -> TypedParam:
        param_name, param_type = param_node.getText().split(":", 2) 
        return TypedParam(param_name, param_type)

    def _extract_function_params(self, ctx: ignoreParser.FunctionContext) -> Dict[str, str]:
        function_param = ctx.FUNCTION_PARAM()
        if not (params := list(map(lambda param_node: self._extract_function_param(param_node), function_param))):
            return {}
        if len(params) != len(set(params)):
            raise IgnoreException(
                AttributeError,
                f"the same argument has been declared twice",
                self.filename,
                ctx.FUNCTION_NAME().getSymbol()
            )
        return {param.name : param.type for param in params}

    def _add_new_function(
        self,
        function_name,
        params,
        body,
        return_type,
        ctx: ignoreParser.FunctionContext,
    ):
        current_env = self.env_stack[-1]
        if function_name in current_env.variables:
            function_name_token = ctx.FUNCTION_NAME().getSymbol()
            raise IgnoreException(
                ReferenceError,
                f"Function '{function_name}' already defined",
                self.filename,
                function_name_token
            )
        new_function = FunctionInfo(
            body=body, var_decl=ctx, return_type=return_type, params=params
        )
        current_env.variables[function_name] = new_function
        self.variables[ctx] = new_function

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
        current_stack = self.env_stack[-1] if len(self.env_stack) > 0 else None
        parent = ctx.parentCtx
        params = {}
        if parent in self.variables and isinstance(
            function := self.variables[parent], FunctionInfo
        ):
            function_params = function.params or {}
            params = {param_name: FunctionArgument(None, param_type) for (param_name, param_type) in function_params.items()}
        self.env_stack.append(Environment(enclosing=current_stack, variables=params)) # type: ignore
        return super().enterBlock(ctx)

    @override
    def exitBlock(self, ctx: ignoreParser.BlockContext):
        parent = ctx.parentCtx
        if parent in self.variables and isinstance(
            function := self.variables[parent], FunctionInfo
        ):
            function.function_env = self.env_stack[-1].create_snapshot() 
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
        function_name = ctx.FUNCTION_NAME().getText()[5:]
        params = self._extract_function_params(ctx)
        body = ctx.block()
        print(type(body))
        assert isinstance(body, ignoreParser.BlockContext) #python can't properly infer type of this, this is supposed to help it.
        return_type = (
            ctx.FUNCTION_RET_TYPE().getText().split("=",2)[1]
            if ctx.FUNCTION_RET_TYPE()
            else None
        )
        if return_type is None and any((isinstance(child, ignoreParser.ReturnStmtContext) for child in body.getChildren())):
            raise IgnoreException(
                ValueError,
                f"Attempting to return from function that does not define return type",
                self.filename,
                body.returnStmt()[0].RETURN_TAG().getSymbol()
            )
        
        self._add_new_function(function_name, params, body, return_type, ctx)

    @override
    def exitFunction(self, ctx: ignoreParser.FunctionContext):
        return super().exitFunction(ctx)
