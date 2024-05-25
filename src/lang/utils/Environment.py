from dataclasses import dataclass, field
from typing import Self

from src.lang.utils.types import VariableDict
from src.lang.utils.VariableInfo import VariableInfo


@dataclass
class Environment:
    """
    Environment is a wrapper around dictionary that maps variable names
    to the corresponding VariableInfo objects.
    """

    enclosing: Self | None
    # dataclass way to have a mutable default value
    variables: VariableDict = field(default_factory=lambda: dict())

    def merge(self, other: "Environment") -> "Environment":
        new_vars = {
            **other.variables,
            **self.variables,
        }
        return Environment(enclosing=other.enclosing, variables=new_vars)

    def create_snapshot(self) -> VariableDict:
        """Creates "snapshot" of all the variables that a newly declared function can access.
        Will be used for closures most probably.
        """
        if self.enclosing == None:
            return self.variables
        return self.merge(self.enclosing).create_snapshot()

    # methods to quickly extract variable, if we know depth at which it was declared.
    # def ancestor(self, distance: int) -> "Environment":
    #     env = self
    #     for _ in range(distance):
    #         env = env.enclosing
    #     return env

    # def get_at(self, distance: int, name: str) -> VariableInfo:
    #     return self.ancestor(distance).variables[name]

    def lookup_variable(self, var_name: str):
        environment = self
        while environment != None:
            if var_name in environment.variables:
                return environment.variables[var_name]
            environment = environment.enclosing
        return None
