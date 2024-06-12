from enum import StrEnum
from typing import override
from antlr4.error.ErrorListener import ErrorListener
from antlr4.Token import CommonToken
from antlr4.error.Errors import InputMismatchException, LexerNoViableAltException
from src.lang.errors.utils import IgnoreException, IgnoreLexerException
from src.lang.generated.ignoreLexer import ignoreLexer
from src.lang.generated.ignoreParser import ignoreParser

class ErrorMessages(StrEnum):
    MISMATCHED_INPUT = "mismatched input"
    TOKEN_RECOGNITION = "token recognition"

class IgnoreErrorListener(ErrorListener):
    @override
    def __init__(self, filepath: str) -> None:
        self.parsed_file: str = filepath
        super().__init__()

    def _raise_unmatched_symbol(self, err: LexerNoViableAltException):
        symbol = err.input.getText(err.startIndex, err.startIndex)
        line = err.input.getText(0, err.startIndex).count('\n')
        raise IgnoreLexerException(
            SyntaxError,
            f"unmatched symbol: '{symbol}'",
            self.parsed_file,
            line,
            symbol
        )

    @override 
    def syntaxError(self, resolver: ignoreParser | ignoreLexer, offendingSymbol: CommonToken, line: int , column: int, msg: str, err):
        if (type(resolver) == ignoreLexer and type(err) == LexerNoViableAltException):
            symbol = err.input.getText(err.startIndex, err.startIndex)
            
            if msg and ErrorMessages.TOKEN_RECOGNITION in msg:
                if symbol == '"':
                    quote_line = err.input.getText(0, err.startIndex).count('\n')
                    raise IgnoreLexerException(
                        SyntaxError,
                        "unclosed quote",
                        self.parsed_file,
                        quote_line,
                        symbol
                    )
                else:
                    self._raise_unmatched_symbol(err)


        if msg and ErrorMessages.MISMATCHED_INPUT in msg and isinstance(err, InputMismatchException):
            TAG_EXPR_OVERLAPS =  ("<", ">", "/")
            if offendingSymbol.text in TAG_EXPR_OVERLAPS:
                    raise IgnoreException(
                        SyntaxError,
                        "unclosed expression",
                        self.parsed_file,
                        offendingSymbol
                    )
            for token in err.getExpectedTokens():
                if token == resolver.CLOSE_PAREN:
                    raise IgnoreException(
                        SyntaxError,
                        "unclosed parenthesis",
                        self.parsed_file,
                        offendingSymbol
                    )
        raise IgnoreException(
            SyntaxError,
            msg,
            self.parsed_file,
            offendingSymbol
        )