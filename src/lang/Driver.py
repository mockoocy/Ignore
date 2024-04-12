import sys
from antlr4 import *
from generated.ignoreLexer import ignoreLexer
from Parser import Parser
from Listener import Listener
from Visitor import Visitor


def main(argv):
    input_stream = FileStream(argv[1], encoding="utf-8")
    lexer = ignoreLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Parser(stream)
    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        raise SyntaxError("Found syntax errors in the code")
    firstPhaseInterpreter = Listener()
    walker = ParseTreeWalker()
    walker.walk(firstPhaseInterpreter, tree)
    visitor = Visitor(firstPhaseInterpreter.variables)
    visitor.visit(tree)


if __name__ == "__main__":
    main(sys.argv)
