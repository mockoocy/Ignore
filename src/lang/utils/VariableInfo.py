from dataclasses import dataclass
from typing import Any, Dict

from ..generated.ignoreParser import ignoreParser

Valid_Types = {  # lewo reprezentuje nasz język, prawo odpowiadajacy typ pythonowy
    "int": int,
    "float": float,
    "string": str,
    "bool": bool,
}

Valid_Types_Reversed = {val: key for key,val in Valid_Types.items()} 


@dataclass
class VariableInfo[T]:
    value: T
    type: str | None = None
    depth: int = 0
    var_decl: ignoreParser.VarDeclContext | None = None
    was_evaluated: bool = False
    recursion_check: int = 0

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        if self.type in ("Any", "Function") or self.type is None:
            return self.value(*args, **kwargs)
        

    def __str__(self):
        return (
f"""VariableInfo
    value: {self.value}
    type: {self.type}
    evaluated: {self.was_evaluated}
""")
    __repr__ = __str__
