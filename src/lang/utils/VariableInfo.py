from dataclasses import dataclass

@dataclass
class VariableInfo:
    name: str
    type: str
    scope: int