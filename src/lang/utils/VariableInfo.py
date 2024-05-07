from dataclasses import dataclass
from typing import Any, Callable, Dict, Optional, Type

from ..generated.ignoreParser import ignoreParser

Valid_Types = {  # lewo reprezentuje nasz język, prawo odpowiadajacy typ pythonowy
    "int": int,
    "float": float,
    "string": str,
    "bool": bool,
}

Valid_Types_Reversed = {val: key for key, val in Valid_Types.items()}


@dataclass
class VariableInfo[T]:
    def __init__(self, type: str, value=None, depth=None, var_decl=None, is_function=False, params=None, return_type=None, body=None, was_evaluated= False, recursion_check = 0):
        self.type = type
        self.value = value
        self.depth = depth
        self.var_decl = var_decl
        self.is_function = is_function
        self.params = params
        self.return_type = return_type
        self.body = body
        self.was_evaluated = was_evaluated
        self.recursion_check = recursion_check 


    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        if self.type in ("Any", "Function") or self.type is None:
            return self.value(*args, **kwargs)

    def __str__(self):
        return f"""VariableInfo
    value: {self.value}
    type: {self.type}
    evaluated: {self.was_evaluated}
"""

    __repr__ = __str__
