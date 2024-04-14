from dataclasses import dataclass
from typing import Any
from Parser import Parser
@dataclass
class VariableInfo[T]:
    value: T
    type: str = "Any"
    scope: int = 0 # deeper we get, bigger it gets
    expression: Parser.ExprContext

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        if (self.type in ("Any", "Function")):
            return self.value(*args, **kwargs)
