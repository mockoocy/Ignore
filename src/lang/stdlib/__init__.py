import contextlib
import io
from types import ModuleType

from src.lang.utils.Environment import Environment

from ..utils.VariableInfo import VariableInfo

modules = ["builtins", "collections"]

"""
    defition of built in variable declarations and function definitions
"""


def get_all_members(modulename: str):
    return __import__(modulename).__dict__


with contextlib.redirect_stdout(io.StringIO()):
    builtins = {}
    for module in modules:
        builtins.update(
            {
                var_name: VariableInfo(variable_value)
                for (var_name, variable_value) in get_all_members(module).items()
                if type(variable_value) != ModuleType
            }
        )
    global global_env
    global_env = Environment(None, builtins)
