from dataclasses import dataclass
from enum import StrEnum
from typing import Type
from antlr4.Token import CommonToken

class SpecialFormatters(StrEnum):
    START_UNDERLINE = '\033[4;31m'
    END_UNDERLINE = '\033[0m'

def underline_word(word: str):
    return SpecialFormatters.START_UNDERLINE + word + SpecialFormatters.END_UNDERLINE

def underline(filepath: str, line: int, col:int, text: str):
    # Shows the line with syntax error, the exact character gets underlined.
    # line and col are 0-indexed
    with open(filepath) as file:
        filetext = file.read().splitlines()
    # Get the line
    length = len(text)
    line_text = filetext[line]

    # Add spaces before and after the underlined character
    prev_line = ""
    next_line = ""
    if line > 0:
        prev_line = '\n' + filetext[line - 1] + '\n'
    if line +1 < len(filetext):
        next_line = '\n' + filetext[line + 1]
    return (prev_line +
        line_text[:col] + 
        underline_word(line_text[col: col+length]) + 
        line_text[col+length:] +
        next_line
    ) 

def underline_whole_line(filepath: str, line: int, text: str):
    with open(filepath) as file:
        filetext = file.read().splitlines()
    # Get the line
    length = len(text)
    line_text = filetext[line]
    prev_line = ""
    next_line = ""
    if line > 0:
        prev_line = '\n' + filetext[line - 1] + '\n'
    if line +1 < len(filetext):
        next_line = '\n' + filetext[line + 1]

    return (prev_line +
        underline_word(line_text) + 
        next_line
    ) 

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
{underline(self.filename, line - 1, col, self.token.text)}
"""
    

@dataclass
class IgnoreLexerException(Exception):
    exception_type: Type[BaseException]
    message: str
    filename: str
    line: int
    text: str

    def __str__(self) -> str:
        return f"""{underline_word(self.exception_type.__name__)}: {self.message} 
in file {self.filename} at line: {self.line}
{underline_whole_line(self.filename, self.line, self.text)}
"""