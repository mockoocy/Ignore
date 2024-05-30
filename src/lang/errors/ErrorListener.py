from typing import override
from antlr4.error.ErrorListener import ErrorListener
from antlr4.Token import CommonToken

from src.lang.errors.utils import underline
from src.lang.generated.ignoreParser import ignoreParser

class IgnoreErrorListener(ErrorListener):
    # @staticmethod
    # def 
    @override
    def __init__(self, filepath: str) -> None:
        self.parsed_file: str = filepath
        super().__init__()

    @override 
    def syntaxError(self, resolver: ignoreParser, offendingSymbol: CommonToken, line: int , column: int, msg: str, _):
        underlined_line = underline(self.parsed_file, offendingSymbol)

        raise Exception(f"ERROR: when parsing line {line} column {column}:\n {underlined_line} \n {msg}\n")
