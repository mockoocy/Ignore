from dataclasses import dataclass
from typing import Any

from ..generated.ignoreParser import ignoreParser

Valid_Types = {  # lewo reprezentuje nasz język, prawo odpowiadajacy typ pythonowy
    "int": int,
    "float": float,
    "string": str,
    "bool": bool,
}

Valid_Types_Reversed = (
    {  # lewo reprezentuje python, prawo odpowiadajacy typ w naszym jezyku
        int: "int",
        float: "float",
        str: "string",
        bool: "bool",
    }
)


@dataclass
class VariableInfo[T]:
    value: T
    type: str = "Any"
    scope: int = 0  # deeper we get, bigger it gets
    expression: ignoreParser.ExprContext | None = None
    var_decl: ignoreParser.VarDeclContext | None = None
    was_evaluated: bool = False

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        if self.type in ("Any", "Function"):
            return self.value(*args, **kwargs)
