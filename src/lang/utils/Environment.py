

from dataclasses import dataclass
from typing import Self

from src.lang.utils.VariableInfo import VariableDict



@dataclass
class Environment:
    """
    Environment is a wrapper around dictionary that maps variable names 
    to the corresponding VariableInfo objects. 
    """
    enclosing: Self | None
    variables: VariableDict
    
    def merge(self, other: "Environment") -> "Environment":
        new_vars = {
            **self.variables, 
            **{key:val 
                for (key,val) in 
                other.variables.items() 
                if key not in self.variables
            }
        }
        return Environment(enclosing=other.enclosing, variables=new_vars)


    def create_snapshot(self) -> VariableDict:
        """Creates "snapshot" of all the variables that a newly declared function can access.
        Will be used for closures most probably. 
        """
        if self.enclosing == None:
            return self.variables
        return self.merge(self.enclosing).create_snapshot()
