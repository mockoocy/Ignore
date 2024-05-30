from dataclasses import dataclass
from enum import StrEnum
from typing import Type
from antlr4.Token import CommonToken

class SpecialFormatters(StrEnum):
    START_UNDERLINE = '\033[4;31m'
    END_UNDERLINE = '\033[0m'

def underline(filepath: str, token: CommonToken):
    # Shows the line with syntax error, the exact character gets underlined.
    # line and col are 0-indexed
    with open(filepath) as file:
        text = file.read().splitlines()
    # Get the line
    line = token.line -1 # By default line is 1-indexed
    col = token.column
    length = len(token.text)
    line_text = text[line]

    # Add spaces before and after the underlined character
    return line_text[:col] + SpecialFormatters.START_UNDERLINE + line_text[col:col+length] + SpecialFormatters.END_UNDERLINE + line_text[col+length:]

    # Print the line with the underlined character


@dataclass
class IgnoreException(Exception):
    exception_type: Type[BaseException]
    message: str
    filename: str
    token: CommonToken

    def __str__(self) -> str:
        line = self.token.line
        col = self.token.column
        return f"""
{self.exception_type.__name__}: {self.message} 
in file {self.filename} at line: {line}, col: {col}
{underline(self.filename, self.token)}
"""