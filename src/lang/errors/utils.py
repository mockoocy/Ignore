from dataclasses import dataclass
from enum import StrEnum
from typing import Type
from antlr4.Token import CommonToken

class SpecialFormatters(StrEnum):
    START_UNDERLINE = '\033[4;31m'
    END_UNDERLINE = '\033[0m'

def underline_word(word: str):
    return SpecialFormatters.START_UNDERLINE + word + SpecialFormatters.END_UNDERLINE

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
    prev_line = ""
    next_line = ""
    if line > 0:
        prev_line = '\n' + text[line - 1] + '\n'
    if line +1 < len(text):
        next_line = '\n' + text[line + 1]
    return (prev_line +
        line_text[:col] + 
        underline_word(line_text[col: col+length]) + 
        line_text[col+length:] +
        next_line
    ) 

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
        return f"""{underline_word(self.exception_type.__name__)}: {self.message} 
in file {self.filename} at line: {line}, col: {col}
{underline(self.filename, self.token)}
"""