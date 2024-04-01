from inspect import getmembers
import contextlib
import io
modules =[
  "builtins",
  "collections"
]

"""
  defition of built in variable declarations and function definitions
"""

def get_all_members(modulename: str):
  return __import__(modulename).__dict__


with contextlib.redirect_stdout(io.StringIO()):
  builtins = {}
  for module in modules:
    builtins.update(get_all_members(module))
