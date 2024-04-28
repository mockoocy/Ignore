import sys
from typing import Dict, Tuple

from antlr4 import *

from src.lang.utils.VariableInfo import VariableInfo

from .ErrorListener import IgnoreErrorListener
from .generated.ignoreLexer import ignoreLexer
from .generated.ignoreParser import ignoreParser
from .Listener import Listener
from .Visitor import Visitor


def first_phase(filename: str) -> Tuple[ignoreParser.ProgramContext, Dict[str, VariableInfo]]:
    # populates variables
    input_stream = FileStream(filename, encoding="utf-8")
    lexer = ignoreLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ignoreParser(stream)
    parser.addErrorListener(IgnoreErrorListener())
    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        raise SyntaxError("Found syntax errors in the code")
    firstPhaseInterpreter = Listener()
    walker = ParseTreeWalker()
    walker.walk(firstPhaseInterpreter, tree)
    return tree, firstPhaseInterpreter.variables

def second_phase(tree: ignoreParser.ProgramContext, variables: Dict[str, VariableInfo]):
    visitor = Visitor(variables)
    visitor.visit(tree)
    return visitor

def traverse(filename: str) -> Visitor:
    return second_phase(*first_phase(filename))
