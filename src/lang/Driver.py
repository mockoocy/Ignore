import sys

from antlr4 import *

from .ErrorListener import IgnoreErrorListener
from .generated.ignoreLexer import ignoreLexer
from .generated.ignoreParser import ignoreParser
from .Listener import Listener
from .Visitor import Visitor


def traverse(filename: str) -> Visitor:
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
    visitor = Visitor(firstPhaseInterpreter.variables)
    visitor.visit(tree)
    return visitor
