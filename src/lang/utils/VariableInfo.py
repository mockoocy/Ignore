from dataclasses import dataclass

from ..generated.ignoreParser import ignoreParser

Valid_Types = {  # lewo reprezentuje nasz język, prawo odpowiadajacy typ pythonowy
    "int": int,
    "float": float,
    "string": str,
    "bool": bool,
    "Function": lambda x : x
}

Valid_Types_Reversed = {val: key for key, val in Valid_Types.items()}


@dataclass
class VariableInfo[T]:
    value: T
    var_decl: ignoreParser.VarDeclContext
    type: str | None = None
    was_evaluated: bool = False

    def __str__(self):
        return f"""VariableInfo
    value: {self.value}
    type: {self.type}
    evaluated: {self.was_evaluated}
"""

    __repr__ = __str__
