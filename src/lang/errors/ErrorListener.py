from typing import override
from antlr4.error.ErrorListener import ErrorListener
from antlr4.Token import CommonToken
from antlr4.error.Errors import LexerNoViableAltException
from src.lang.errors.utils import IgnoreException, IgnoreLexerException
from src.lang.generated.ignoreParser import ignoreParser

class IgnoreErrorListener(ErrorListener):
    @override
    def __init__(self, filepath: str) -> None:
        self.parsed_file: str = filepath
        super().__init__()

    @override 
    def syntaxError(self, resolver: ignoreParser, offendingSymbol: CommonToken, line: int , column: int, msg: str, err):
        if (type(err)) == LexerNoViableAltException:
            line = err.input.getText(0, err.startIndex).count("\n")
            symbol = err.input.getText(err.startIndex, err.startIndex)
            if symbol == '"':
                raise IgnoreLexerException(
                    SyntaxError,
                    "Unmatched quotes!",
                    self.parsed_file,
                    line+1,
                    symbol
                )
            if symbol == '{':
                raise IgnoreLexerException(
                    SyntaxError,
                    "Unmatched curly bracket!",
                    self.parsed_file,
                    line+1,
                    symbol
                )

        raise IgnoreException(
            SyntaxError,
            msg,
            self.parsed_file,
            offendingSymbol
        )