from typing import  Tuple

from antlr4 import *

from .errors.ErrorListener import IgnoreErrorListener
from .generated.ignoreLexer import ignoreLexer
from .generated.ignoreParser import ignoreParser
from .Listener import Listener
from .utils.types import VarDeclDict
from .Visitor import Visitor


def first_phase(filename: str) -> Tuple[ignoreParser.ProgramContext, VarDeclDict, str]:
    # populates variables
    input_stream = FileStream(filename, encoding="utf-8")
    lexer = ignoreLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ignoreParser(stream)
    parser.addErrorListener(IgnoreErrorListener(filename))
    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        raise SyntaxError("Found syntax errors in the code")
    firstPhaseInterpreter = Listener(filename)
    walker = ParseTreeWalker()
    walker.walk(firstPhaseInterpreter, tree)
    return tree, firstPhaseInterpreter.variables, filename


def second_phase(tree: ignoreParser.ProgramContext, variables: VarDeclDict, filename):
    visitor = Visitor(variables, filename)
    visitor.visit(tree)
    return visitor


def traverse(filename: str) -> Visitor:
    return second_phase(*first_phase(filename))
