from typing import override
from antlr4.error.ErrorListener import ErrorListener
from antlr4.Token import CommonToken

from src.lang.errors.utils import IgnoreException
from src.lang.generated.ignoreParser import ignoreParser

class IgnoreErrorListener(ErrorListener):
    @override
    def __init__(self, filepath: str) -> None:
        self.parsed_file: str = filepath
        super().__init__()

    @override 
    def syntaxError(self, resolver: ignoreParser, offendingSymbol: CommonToken, line: int , column: int, msg: str, _):
        raise IgnoreException(
            SyntaxError,
            msg,
            self.parsed_file,
            offendingSymbol
        )