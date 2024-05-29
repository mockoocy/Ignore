from typing import Dict, NamedTuple

from src.lang.generated.ignoreParser import ignoreParser
from src.lang.utils.BuiltIn import BuiltIn
from src.lang.utils.FunctionArgument import FunctionArgument
from src.lang.utils.FunctionInfo import FunctionInfo
from src.lang.utils.VariableInfo import VariableInfo

ValueWrapper = VariableInfo | FunctionInfo | BuiltIn | FunctionArgument

ValueDecl = ignoreParser.VarDeclContext | ignoreParser.FunctionContext

VarDeclDict = Dict[ValueDecl, ValueWrapper]  # maps specific declarations to info.
VariableDict = Dict[
    str, ValueWrapper
]  # maps name in the current scope to specific info.

class TypedParam(NamedTuple):
    name: str
    type: str