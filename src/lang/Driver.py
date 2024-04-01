import sys
from antlr4 import *
from ignoreLexer import ignoreLexer
from ignoreParser import ignoreParser
from ignoreParserListener import ignoreParserListener

def main(argv):
    input_stream = FileStream(argv[1], encoding="utf-8")
    lexer = ignoreLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ignoreParser(stream)
    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        linterp = ignoreParserListener()
        walker = ParseTreeWalker()
        walker.walk(linterp, tree)

if __name__ == '__main__':
    main(sys.argv)