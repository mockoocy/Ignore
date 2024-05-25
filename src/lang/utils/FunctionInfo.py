from dataclasses import dataclass
from typing import Dict, Self

from src.lang.generated.ignoreParser import ignoreParser
from src.lang.utils.BuiltIn import BuiltIn
from src.lang.utils.FunctionArgument import FunctionArgument
from src.lang.utils.VariableInfo import VariableInfo


@dataclass
class FunctionInfo:
    body: ignoreParser.BlockContext
    var_decl: ignoreParser.FunctionContext
    function_env: Dict[str, VariableInfo | Self | BuiltIn | FunctionArgument] | None = (
        None
    )
    params: Dict[str, str] | None = None
    return_type: str | None = None
    is_builtin: bool = False

    def __str__(self):
        return f"""Function {list(self.params.values()) if self.params else None} => {self.return_type}"""

    __repr__ = __str__
