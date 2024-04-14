import sys
from antlr4 import *
from generated.ignoreLexer import ignoreLexer
from generated.ignoreParser import ignoreParser
from Listener import Listener
from Visitor import Visitor
from ErrorListener import IgnoreErrorListener

def main(argv):
    input_stream = FileStream(argv[1], encoding="utf-8")
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
    visitor = Visitor(firstPhaseInterpreter.variables).visit(tree)


if __name__ == '__main__':
    main(sys.argv)