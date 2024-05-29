from dataclasses import dataclass


@dataclass
class FunctionArgument[T]:
    value: T
    type: str
