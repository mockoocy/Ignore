from typing import Dict

from src.lang.generated.ignoreParser import ignoreParser
from src.lang.utils.VariableInfo import VariableInfo

VarDeclDict = Dict[
    ignoreParser.VarDeclContext, VariableInfo
]  # maps specific declarations to info.
VariableDict = Dict[
    str, VariableInfo
]  # maps name in the current scope to specific info.
