# Generated from src/grammar/ignoreParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,57,281,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,1,0,1,1,1,1,1,2,1,2,1,3,4,3,66,8,3,11,3,
        12,3,67,1,4,1,4,1,4,3,4,73,8,4,1,4,3,4,76,8,4,1,5,1,5,1,5,5,5,81,
        8,5,10,5,12,5,84,9,5,1,5,3,5,87,8,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,
        1,6,1,7,1,7,1,7,3,7,100,8,7,1,7,1,7,1,7,1,7,3,7,106,8,7,1,7,3,7,
        109,8,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,
        1,11,1,11,3,11,126,8,11,1,11,1,11,3,11,130,8,11,1,11,1,11,1,11,1,
        11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,14,1,14,3,14,145,8,14,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,
        20,1,20,5,20,175,8,20,10,20,12,20,178,9,20,1,20,3,20,181,8,20,1,
        21,5,21,184,8,21,10,21,12,21,187,9,21,1,21,1,21,1,21,5,21,192,8,
        21,10,21,12,21,195,9,21,1,21,1,21,5,21,199,8,21,10,21,12,21,202,
        9,21,1,21,1,21,1,22,1,22,1,22,3,22,209,8,22,1,23,1,23,1,23,1,24,
        1,24,1,24,1,24,4,24,218,8,24,11,24,12,24,219,1,24,1,24,3,24,224,
        8,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,
        237,8,25,1,26,1,26,1,26,4,26,242,8,26,11,26,12,26,243,1,27,1,27,
        1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,258,8,27,
        1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,5,27,
        272,8,27,10,27,12,27,275,9,27,1,28,1,28,1,28,1,28,1,28,0,1,54,29,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,50,52,54,56,0,4,1,0,51,52,3,0,37,37,39,39,51,52,2,0,44,45,
        48,49,1,0,46,47,290,0,58,1,0,0,0,2,60,1,0,0,0,4,62,1,0,0,0,6,65,
        1,0,0,0,8,69,1,0,0,0,10,77,1,0,0,0,12,92,1,0,0,0,14,108,1,0,0,0,
        16,110,1,0,0,0,18,114,1,0,0,0,20,117,1,0,0,0,22,123,1,0,0,0,24,135,
        1,0,0,0,26,140,1,0,0,0,28,144,1,0,0,0,30,146,1,0,0,0,32,153,1,0,
        0,0,34,157,1,0,0,0,36,164,1,0,0,0,38,168,1,0,0,0,40,172,1,0,0,0,
        42,185,1,0,0,0,44,205,1,0,0,0,46,210,1,0,0,0,48,223,1,0,0,0,50,236,
        1,0,0,0,52,241,1,0,0,0,54,257,1,0,0,0,56,276,1,0,0,0,58,59,5,35,
        0,0,59,1,1,0,0,0,60,61,7,0,0,0,61,3,1,0,0,0,62,63,7,1,0,0,63,5,1,
        0,0,0,64,66,3,54,27,0,65,64,1,0,0,0,66,67,1,0,0,0,67,65,1,0,0,0,
        67,68,1,0,0,0,68,7,1,0,0,0,69,70,5,38,0,0,70,72,5,41,0,0,71,73,3,
        6,3,0,72,71,1,0,0,0,72,73,1,0,0,0,73,75,1,0,0,0,74,76,5,42,0,0,75,
        74,1,0,0,0,75,76,1,0,0,0,76,9,1,0,0,0,77,78,5,16,0,0,78,82,5,20,
        0,0,79,81,5,22,0,0,80,79,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,
        83,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,85,87,5,21,0,0,86,85,1,0,
        0,0,86,87,1,0,0,0,87,88,1,0,0,0,88,89,5,32,0,0,89,90,3,52,26,0,90,
        91,5,17,0,0,91,11,1,0,0,0,92,93,5,18,0,0,93,94,3,56,28,0,94,95,5,
        19,0,0,95,13,1,0,0,0,96,97,5,10,0,0,97,99,5,20,0,0,98,100,5,9,0,
        0,99,98,1,0,0,0,99,100,1,0,0,0,100,101,1,0,0,0,101,109,5,32,0,0,
        102,103,5,10,0,0,103,105,5,20,0,0,104,106,5,9,0,0,105,104,1,0,0,
        0,105,106,1,0,0,0,106,107,1,0,0,0,107,109,5,32,0,0,108,96,1,0,0,
        0,108,102,1,0,0,0,109,15,1,0,0,0,110,111,3,14,7,0,111,112,3,56,28,
        0,112,113,5,8,0,0,113,17,1,0,0,0,114,115,5,33,0,0,115,116,3,56,28,
        0,116,19,1,0,0,0,117,118,5,11,0,0,118,119,3,24,12,0,119,120,5,32,
        0,0,120,121,3,52,26,0,121,122,5,12,0,0,122,21,1,0,0,0,123,125,5,
        14,0,0,124,126,3,16,8,0,125,124,1,0,0,0,125,126,1,0,0,0,126,127,
        1,0,0,0,127,129,3,24,12,0,128,130,3,18,9,0,129,128,1,0,0,0,129,130,
        1,0,0,0,130,131,1,0,0,0,131,132,5,32,0,0,132,133,3,52,26,0,133,134,
        5,15,0,0,134,23,1,0,0,0,135,136,5,31,0,0,136,137,5,34,0,0,137,138,
        3,28,14,0,138,139,5,56,0,0,139,25,1,0,0,0,140,141,5,13,0,0,141,27,
        1,0,0,0,142,145,3,54,27,0,143,145,5,37,0,0,144,142,1,0,0,0,144,143,
        1,0,0,0,145,29,1,0,0,0,146,147,5,1,0,0,147,148,5,31,0,0,148,149,
        5,34,0,0,149,150,3,28,14,0,150,151,5,56,0,0,151,152,5,32,0,0,152,
        31,1,0,0,0,153,154,3,30,15,0,154,155,3,52,26,0,155,156,5,2,0,0,156,
        33,1,0,0,0,157,158,5,4,0,0,158,159,5,31,0,0,159,160,5,34,0,0,160,
        161,3,28,14,0,161,162,5,56,0,0,162,163,5,32,0,0,163,35,1,0,0,0,164,
        165,3,34,17,0,165,166,3,52,26,0,166,167,5,3,0,0,167,37,1,0,0,0,168,
        169,5,5,0,0,169,170,3,52,26,0,170,171,5,6,0,0,171,39,1,0,0,0,172,
        176,3,32,16,0,173,175,3,36,18,0,174,173,1,0,0,0,175,178,1,0,0,0,
        176,174,1,0,0,0,176,177,1,0,0,0,177,180,1,0,0,0,178,176,1,0,0,0,
        179,181,3,38,19,0,180,179,1,0,0,0,180,181,1,0,0,0,181,41,1,0,0,0,
        182,184,3,10,5,0,183,182,1,0,0,0,184,187,1,0,0,0,185,183,1,0,0,0,
        185,186,1,0,0,0,186,188,1,0,0,0,187,185,1,0,0,0,188,193,5,26,0,0,
        189,192,3,52,26,0,190,192,3,16,8,0,191,189,1,0,0,0,191,190,1,0,0,
        0,192,195,1,0,0,0,193,191,1,0,0,0,193,194,1,0,0,0,194,196,1,0,0,
        0,195,193,1,0,0,0,196,200,5,27,0,0,197,199,3,10,5,0,198,197,1,0,
        0,0,199,202,1,0,0,0,200,198,1,0,0,0,200,201,1,0,0,0,201,203,1,0,
        0,0,202,200,1,0,0,0,203,204,5,0,0,1,204,43,1,0,0,0,205,208,5,33,
        0,0,206,209,3,56,28,0,207,209,5,30,0,0,208,206,1,0,0,0,208,207,1,
        0,0,0,209,45,1,0,0,0,210,211,5,28,0,0,211,212,5,32,0,0,212,47,1,
        0,0,0,213,214,5,29,0,0,214,224,5,32,0,0,215,217,5,29,0,0,216,218,
        3,44,22,0,217,216,1,0,0,0,218,219,1,0,0,0,219,217,1,0,0,0,219,220,
        1,0,0,0,220,221,1,0,0,0,221,222,5,32,0,0,222,224,1,0,0,0,223,213,
        1,0,0,0,223,215,1,0,0,0,224,49,1,0,0,0,225,226,3,48,24,0,226,227,
        3,56,28,0,227,228,3,46,23,0,228,237,1,0,0,0,229,237,3,56,28,0,230,
        237,3,10,5,0,231,237,3,40,20,0,232,237,3,16,8,0,233,237,3,18,9,0,
        234,237,3,22,11,0,235,237,3,20,10,0,236,225,1,0,0,0,236,229,1,0,
        0,0,236,230,1,0,0,0,236,231,1,0,0,0,236,232,1,0,0,0,236,233,1,0,
        0,0,236,234,1,0,0,0,236,235,1,0,0,0,237,51,1,0,0,0,238,242,3,50,
        25,0,239,242,3,12,6,0,240,242,3,26,13,0,241,238,1,0,0,0,241,239,
        1,0,0,0,241,240,1,0,0,0,242,243,1,0,0,0,243,241,1,0,0,0,243,244,
        1,0,0,0,244,53,1,0,0,0,245,246,6,27,-1,0,246,247,5,41,0,0,247,248,
        3,54,27,0,248,249,5,42,0,0,249,258,1,0,0,0,250,251,5,47,0,0,251,
        258,3,54,27,9,252,258,3,4,2,0,253,258,3,8,4,0,254,255,5,50,0,0,255,
        258,3,54,27,2,256,258,5,38,0,0,257,245,1,0,0,0,257,250,1,0,0,0,257,
        252,1,0,0,0,257,253,1,0,0,0,257,254,1,0,0,0,257,256,1,0,0,0,258,
        273,1,0,0,0,259,260,10,8,0,0,260,261,7,2,0,0,261,272,3,54,27,9,262,
        263,10,7,0,0,263,264,7,3,0,0,264,272,3,54,27,8,265,266,10,6,0,0,
        266,267,5,53,0,0,267,272,3,54,27,7,268,269,10,5,0,0,269,270,5,54,
        0,0,270,272,3,54,27,6,271,259,1,0,0,0,271,262,1,0,0,0,271,265,1,
        0,0,0,271,268,1,0,0,0,272,275,1,0,0,0,273,271,1,0,0,0,273,274,1,
        0,0,0,274,55,1,0,0,0,275,273,1,0,0,0,276,277,5,34,0,0,277,278,3,
        54,27,0,278,279,5,56,0,0,279,57,1,0,0,0,26,67,72,75,82,86,99,105,
        108,125,129,144,176,180,185,191,193,200,208,219,223,236,241,243,
        257,271,273
    ]

class ignoreParser ( Parser ):

    grammarFileName = "ignoreParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<if'", "'</if>'", "'</elif>'", "'<elif'", 
                     "'<else>'", "'</else>'", "'<var'", "'</var>'", "<INVALID>", 
                     "<INVALID>", "'<while'", "'</while>'", "<INVALID>", 
                     "'<for'", "'</for>'", "'<function'", "'</function>'", 
                     "'<return>'", "'</return>'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'<program>'", "'</program>'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'condition='", "'>'", "<INVALID>", "'{'", 
                     "','", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "':'", "'('", "')'", "'='", "'*'", "'/'", "'+'", "'-'", 
                     "'%'", "'//'", "'!'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'}'" ]

    symbolicNames = [ "<INVALID>", "IF_TAG", "IF_END", "ELIF_END", "ELIF_TAG", 
                      "ELSE", "ELSE_END", "VAR_DECL_START", "VAR_DECL_END", 
                      "VAR_DECL_TYPE", "VAR_DECL", "WHILE_TAG", "WHILE_END", 
                      "BREAK", "FOR_TAG", "FOR_END", "FUNCTION_TAG_OPEN", 
                      "FUNCTION_TAG_END", "RETURN_TAG", "RETURN_END", "FUNCTION_NAME", 
                      "FUNCTION_RET_TYPE", "FUNCTION_PARAM", "COMMENT", 
                      "LINE_COMMENT", "WS", "OPEN_PROGRAM", "CLOSE_PROGRAM", 
                      "CLOSE_TAG", "OPEN_TAG", "TAG_REFERENCE", "CONDITION_EQ", 
                      "END_TAG", "PROPERTY_NAME", "OPEN_CURLY", "COMMA", 
                      "EXPR_WS", "LITERAL_BOOL", "NAME", "LITERAL_STRING", 
                      "COLON", "OPEN_PAREN", "CLOSE_PAREN", "EQUALS", "MUL", 
                      "DIV", "ADD", "SUB", "MOD", "INT_DIV", "NOT", "LITERAL_INT", 
                      "LITERAL_FLOAT", "OPERATOR_COMPARE", "OPERATOR_LOGIC", 
                      "EXPR_COMMENT", "CLOSE_CURLY", "EXPR_LINE_COMMENT" ]

    RULE_comma = 0
    RULE_literalNumeric = 1
    RULE_literal = 2
    RULE_argumentList = 3
    RULE_functionCall = 4
    RULE_function = 5
    RULE_returnStmt = 6
    RULE_varDecl = 7
    RULE_var = 8
    RULE_var_assign = 9
    RULE_while_loop = 10
    RULE_for_loop = 11
    RULE_loop_condition = 12
    RULE_break = 13
    RULE_condition = 14
    RULE_if = 15
    RULE_if_statement = 16
    RULE_elif = 17
    RULE_elif_statement = 18
    RULE_else_statement = 19
    RULE_control_statement = 20
    RULE_program = 21
    RULE_property = 22
    RULE_endTag = 23
    RULE_startTag = 24
    RULE_statement = 25
    RULE_block = 26
    RULE_expr = 27
    RULE_wrapped_expr = 28

    ruleNames =  [ "comma", "literalNumeric", "literal", "argumentList", 
                   "functionCall", "function", "returnStmt", "varDecl", 
                   "var", "var_assign", "while_loop", "for_loop", "loop_condition", 
                   "break", "condition", "if", "if_statement", "elif", "elif_statement", 
                   "else_statement", "control_statement", "program", "property", 
                   "endTag", "startTag", "statement", "block", "expr", "wrapped_expr" ]

    EOF = Token.EOF
    IF_TAG=1
    IF_END=2
    ELIF_END=3
    ELIF_TAG=4
    ELSE=5
    ELSE_END=6
    VAR_DECL_START=7
    VAR_DECL_END=8
    VAR_DECL_TYPE=9
    VAR_DECL=10
    WHILE_TAG=11
    WHILE_END=12
    BREAK=13
    FOR_TAG=14
    FOR_END=15
    FUNCTION_TAG_OPEN=16
    FUNCTION_TAG_END=17
    RETURN_TAG=18
    RETURN_END=19
    FUNCTION_NAME=20
    FUNCTION_RET_TYPE=21
    FUNCTION_PARAM=22
    COMMENT=23
    LINE_COMMENT=24
    WS=25
    OPEN_PROGRAM=26
    CLOSE_PROGRAM=27
    CLOSE_TAG=28
    OPEN_TAG=29
    TAG_REFERENCE=30
    CONDITION_EQ=31
    END_TAG=32
    PROPERTY_NAME=33
    OPEN_CURLY=34
    COMMA=35
    EXPR_WS=36
    LITERAL_BOOL=37
    NAME=38
    LITERAL_STRING=39
    COLON=40
    OPEN_PAREN=41
    CLOSE_PAREN=42
    EQUALS=43
    MUL=44
    DIV=45
    ADD=46
    SUB=47
    MOD=48
    INT_DIV=49
    NOT=50
    LITERAL_INT=51
    LITERAL_FLOAT=52
    OPERATOR_COMPARE=53
    OPERATOR_LOGIC=54
    EXPR_COMMENT=55
    CLOSE_CURLY=56
    EXPR_LINE_COMMENT=57

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CommaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ignoreParser.COMMA, 0)

        def getRuleIndex(self):
            return ignoreParser.RULE_comma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComma" ):
                listener.enterComma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComma" ):
                listener.exitComma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComma" ):
                return visitor.visitComma(self)
            else:
                return visitor.visitChildren(self)




    def comma(self):

        localctx = ignoreParser.CommaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_comma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(ignoreParser.COMMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralNumericContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LITERAL_INT(self):
            return self.getToken(ignoreParser.LITERAL_INT, 0)

        def LITERAL_FLOAT(self):
            return self.getToken(ignoreParser.LITERAL_FLOAT, 0)

        def getRuleIndex(self):
            return ignoreParser.RULE_literalNumeric

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralNumeric" ):
                listener.enterLiteralNumeric(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralNumeric" ):
                listener.exitLiteralNumeric(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralNumeric" ):
                return visitor.visitLiteralNumeric(self)
            else:
                return visitor.visitChildren(self)




    def literalNumeric(self):

        localctx = ignoreParser.LiteralNumericContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_literalNumeric)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            _la = self._input.LA(1)
            if not(_la==51 or _la==52):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LITERAL_INT(self):
            return self.getToken(ignoreParser.LITERAL_INT, 0)

        def LITERAL_FLOAT(self):
            return self.getToken(ignoreParser.LITERAL_FLOAT, 0)

        def LITERAL_STRING(self):
            return self.getToken(ignoreParser.LITERAL_STRING, 0)

        def LITERAL_BOOL(self):
            return self.getToken(ignoreParser.LITERAL_BOOL, 0)

        def getRuleIndex(self):
            return ignoreParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ignoreParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6756086635823104) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ignoreParser.ExprContext)
            else:
                return self.getTypedRuleContext(ignoreParser.ExprContext,i)


        def getRuleIndex(self):
            return ignoreParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = ignoreParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_argumentList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 64
                    self.expr(0)

                else:
                    raise NoViableAltException(self)
                self.state = 67 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(ignoreParser.NAME, 0)

        def OPEN_PAREN(self):
            return self.getToken(ignoreParser.OPEN_PAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(ignoreParser.ArgumentListContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(ignoreParser.CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return ignoreParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = ignoreParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(ignoreParser.NAME)
            self.state = 70
            self.match(ignoreParser.OPEN_PAREN)
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 71
                self.argumentList()


            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 74
                self.match(ignoreParser.CLOSE_PAREN)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION_TAG_OPEN(self):
            return self.getToken(ignoreParser.FUNCTION_TAG_OPEN, 0)

        def FUNCTION_NAME(self):
            return self.getToken(ignoreParser.FUNCTION_NAME, 0)

        def END_TAG(self):
            return self.getToken(ignoreParser.END_TAG, 0)

        def block(self):
            return self.getTypedRuleContext(ignoreParser.BlockContext,0)


        def FUNCTION_TAG_END(self):
            return self.getToken(ignoreParser.FUNCTION_TAG_END, 0)

        def FUNCTION_PARAM(self, i:int=None):
            if i is None:
                return self.getTokens(ignoreParser.FUNCTION_PARAM)
            else:
                return self.getToken(ignoreParser.FUNCTION_PARAM, i)

        def FUNCTION_RET_TYPE(self):
            return self.getToken(ignoreParser.FUNCTION_RET_TYPE, 0)

        def getRuleIndex(self):
            return ignoreParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = ignoreParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(ignoreParser.FUNCTION_TAG_OPEN)
            self.state = 78
            self.match(ignoreParser.FUNCTION_NAME)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 79
                self.match(ignoreParser.FUNCTION_PARAM)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 85
                self.match(ignoreParser.FUNCTION_RET_TYPE)


            self.state = 88
            self.match(ignoreParser.END_TAG)
            self.state = 89
            self.block()
            self.state = 90
            self.match(ignoreParser.FUNCTION_TAG_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_TAG(self):
            return self.getToken(ignoreParser.RETURN_TAG, 0)

        def wrapped_expr(self):
            return self.getTypedRuleContext(ignoreParser.Wrapped_exprContext,0)


        def RETURN_END(self):
            return self.getToken(ignoreParser.RETURN_END, 0)

        def getRuleIndex(self):
            return ignoreParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = ignoreParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(ignoreParser.RETURN_TAG)
            self.state = 93
            self.wrapped_expr()
            self.state = 94
            self.match(ignoreParser.RETURN_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_DECL(self):
            return self.getToken(ignoreParser.VAR_DECL, 0)

        def FUNCTION_NAME(self):
            return self.getToken(ignoreParser.FUNCTION_NAME, 0)

        def END_TAG(self):
            return self.getToken(ignoreParser.END_TAG, 0)

        def VAR_DECL_TYPE(self):
            return self.getToken(ignoreParser.VAR_DECL_TYPE, 0)

        def getRuleIndex(self):
            return ignoreParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = ignoreParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.match(ignoreParser.VAR_DECL)
                self.state = 97
                self.match(ignoreParser.FUNCTION_NAME)
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 98
                    self.match(ignoreParser.VAR_DECL_TYPE)


                self.state = 101
                self.match(ignoreParser.END_TAG)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.match(ignoreParser.VAR_DECL)
                self.state = 103
                self.match(ignoreParser.FUNCTION_NAME)
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 104
                    self.match(ignoreParser.VAR_DECL_TYPE)


                self.state = 107
                self.match(ignoreParser.END_TAG)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(ignoreParser.VarDeclContext,0)


        def wrapped_expr(self):
            return self.getTypedRuleContext(ignoreParser.Wrapped_exprContext,0)


        def VAR_DECL_END(self):
            return self.getToken(ignoreParser.VAR_DECL_END, 0)

        def getRuleIndex(self):
            return ignoreParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = ignoreParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.varDecl()
            self.state = 111
            self.wrapped_expr()
            self.state = 112
            self.match(ignoreParser.VAR_DECL_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROPERTY_NAME(self):
            return self.getToken(ignoreParser.PROPERTY_NAME, 0)

        def wrapped_expr(self):
            return self.getTypedRuleContext(ignoreParser.Wrapped_exprContext,0)


        def getRuleIndex(self):
            return ignoreParser.RULE_var_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_assign" ):
                listener.enterVar_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_assign" ):
                listener.exitVar_assign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_assign" ):
                return visitor.visitVar_assign(self)
            else:
                return visitor.visitChildren(self)




    def var_assign(self):

        localctx = ignoreParser.Var_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_var_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(ignoreParser.PROPERTY_NAME)
            self.state = 115
            self.wrapped_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE_TAG(self):
            return self.getToken(ignoreParser.WHILE_TAG, 0)

        def loop_condition(self):
            return self.getTypedRuleContext(ignoreParser.Loop_conditionContext,0)


        def END_TAG(self):
            return self.getToken(ignoreParser.END_TAG, 0)

        def block(self):
            return self.getTypedRuleContext(ignoreParser.BlockContext,0)


        def WHILE_END(self):
            return self.getToken(ignoreParser.WHILE_END, 0)

        def getRuleIndex(self):
            return ignoreParser.RULE_while_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_loop" ):
                listener.enterWhile_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_loop" ):
                listener.exitWhile_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_loop" ):
                return visitor.visitWhile_loop(self)
            else:
                return visitor.visitChildren(self)




    def while_loop(self):

        localctx = ignoreParser.While_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(ignoreParser.WHILE_TAG)
            self.state = 118
            self.loop_condition()
            self.state = 119
            self.match(ignoreParser.END_TAG)
            self.state = 120
            self.block()
            self.state = 121
            self.match(ignoreParser.WHILE_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR_TAG(self):
            return self.getToken(ignoreParser.FOR_TAG, 0)

        def loop_condition(self):
            return self.getTypedRuleContext(ignoreParser.Loop_conditionContext,0)


        def END_TAG(self):
            return self.getToken(ignoreParser.END_TAG, 0)

        def block(self):
            return self.getTypedRuleContext(ignoreParser.BlockContext,0)


        def FOR_END(self):
            return self.getToken(ignoreParser.FOR_END, 0)

        def var(self):
            return self.getTypedRuleContext(ignoreParser.VarContext,0)


        def var_assign(self):
            return self.getTypedRuleContext(ignoreParser.Var_assignContext,0)


        def getRuleIndex(self):
            return ignoreParser.RULE_for_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_loop" ):
                listener.enterFor_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_loop" ):
                listener.exitFor_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop" ):
                return visitor.visitFor_loop(self)
            else:
                return visitor.visitChildren(self)




    def for_loop(self):

        localctx = ignoreParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_for_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(ignoreParser.FOR_TAG)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 124
                self.var()


            self.state = 127
            self.loop_condition()
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 128
                self.var_assign()


            self.state = 131
            self.match(ignoreParser.END_TAG)
            self.state = 132
            self.block()
            self.state = 133
            self.match(ignoreParser.FOR_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONDITION_EQ(self):
            return self.getToken(ignoreParser.CONDITION_EQ, 0)

        def OPEN_CURLY(self):
            return self.getToken(ignoreParser.OPEN_CURLY, 0)

        def CLOSE_CURLY(self):
            return self.getToken(ignoreParser.CLOSE_CURLY, 0)

        def condition(self):
            return self.getTypedRuleContext(ignoreParser.ConditionContext,0)


        def getRuleIndex(self):
            return ignoreParser.RULE_loop_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_condition" ):
                listener.enterLoop_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_condition" ):
                listener.exitLoop_condition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_condition" ):
                return visitor.visitLoop_condition(self)
            else:
                return visitor.visitChildren(self)




    def loop_condition(self):

        localctx = ignoreParser.Loop_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_loop_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(ignoreParser.CONDITION_EQ)
            self.state = 136
            self.match(ignoreParser.OPEN_CURLY)

            self.state = 137
            self.condition()
            self.state = 138
            self.match(ignoreParser.CLOSE_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ignoreParser.BREAK, 0)

        def getRuleIndex(self):
            return ignoreParser.RULE_break

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak" ):
                listener.enterBreak(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak" ):
                listener.exitBreak(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak" ):
                return visitor.visitBreak(self)
            else:
                return visitor.visitChildren(self)




    def break_(self):

        localctx = ignoreParser.BreakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(ignoreParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ignoreParser.ExprContext,0)


        def LITERAL_BOOL(self):
            return self.getToken(ignoreParser.LITERAL_BOOL, 0)

        def getRuleIndex(self):
            return ignoreParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = ignoreParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_condition)
        try:
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.match(ignoreParser.LITERAL_BOOL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_TAG(self):
            return self.getToken(ignoreParser.IF_TAG, 0)

        def CONDITION_EQ(self):
            return self.getToken(ignoreParser.CONDITION_EQ, 0)

        def OPEN_CURLY(self):
            return self.getToken(ignoreParser.OPEN_CURLY, 0)

        def CLOSE_CURLY(self):
            return self.getToken(ignoreParser.CLOSE_CURLY, 0)

        def END_TAG(self):
            return self.getToken(ignoreParser.END_TAG, 0)

        def condition(self):
            return self.getTypedRuleContext(ignoreParser.ConditionContext,0)


        def getRuleIndex(self):
            return ignoreParser.RULE_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)




    def if_(self):

        localctx = ignoreParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(ignoreParser.IF_TAG)
            self.state = 147
            self.match(ignoreParser.CONDITION_EQ)
            self.state = 148
            self.match(ignoreParser.OPEN_CURLY)

            self.state = 149
            self.condition()
            self.state = 150
            self.match(ignoreParser.CLOSE_CURLY)
            self.state = 151
            self.match(ignoreParser.END_TAG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_(self):
            return self.getTypedRuleContext(ignoreParser.IfContext,0)


        def block(self):
            return self.getTypedRuleContext(ignoreParser.BlockContext,0)


        def IF_END(self):
            return self.getToken(ignoreParser.IF_END, 0)

        def getRuleIndex(self):
            return ignoreParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = ignoreParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.if_()
            self.state = 154
            self.block()
            self.state = 155
            self.match(ignoreParser.IF_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF_TAG(self):
            return self.getToken(ignoreParser.ELIF_TAG, 0)

        def CONDITION_EQ(self):
            return self.getToken(ignoreParser.CONDITION_EQ, 0)

        def OPEN_CURLY(self):
            return self.getToken(ignoreParser.OPEN_CURLY, 0)

        def CLOSE_CURLY(self):
            return self.getToken(ignoreParser.CLOSE_CURLY, 0)

        def END_TAG(self):
            return self.getToken(ignoreParser.END_TAG, 0)

        def condition(self):
            return self.getTypedRuleContext(ignoreParser.ConditionContext,0)


        def getRuleIndex(self):
            return ignoreParser.RULE_elif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElif" ):
                listener.enterElif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElif" ):
                listener.exitElif(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif" ):
                return visitor.visitElif(self)
            else:
                return visitor.visitChildren(self)




    def elif_(self):

        localctx = ignoreParser.ElifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_elif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(ignoreParser.ELIF_TAG)
            self.state = 158
            self.match(ignoreParser.CONDITION_EQ)
            self.state = 159
            self.match(ignoreParser.OPEN_CURLY)

            self.state = 160
            self.condition()
            self.state = 161
            self.match(ignoreParser.CLOSE_CURLY)
            self.state = 162
            self.match(ignoreParser.END_TAG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_(self):
            return self.getTypedRuleContext(ignoreParser.ElifContext,0)


        def block(self):
            return self.getTypedRuleContext(ignoreParser.BlockContext,0)


        def ELIF_END(self):
            return self.getToken(ignoreParser.ELIF_END, 0)

        def getRuleIndex(self):
            return ignoreParser.RULE_elif_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElif_statement" ):
                listener.enterElif_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElif_statement" ):
                listener.exitElif_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_statement" ):
                return visitor.visitElif_statement(self)
            else:
                return visitor.visitChildren(self)




    def elif_statement(self):

        localctx = ignoreParser.Elif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_elif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.elif_()
            self.state = 165
            self.block()
            self.state = 166
            self.match(ignoreParser.ELIF_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ignoreParser.ELSE, 0)

        def block(self):
            return self.getTypedRuleContext(ignoreParser.BlockContext,0)


        def ELSE_END(self):
            return self.getToken(ignoreParser.ELSE_END, 0)

        def getRuleIndex(self):
            return ignoreParser.RULE_else_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_statement" ):
                listener.enterElse_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_statement" ):
                listener.exitElse_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = ignoreParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(ignoreParser.ELSE)
            self.state = 169
            self.block()
            self.state = 170
            self.match(ignoreParser.ELSE_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Control_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_statement(self):
            return self.getTypedRuleContext(ignoreParser.If_statementContext,0)


        def elif_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ignoreParser.Elif_statementContext)
            else:
                return self.getTypedRuleContext(ignoreParser.Elif_statementContext,i)


        def else_statement(self):
            return self.getTypedRuleContext(ignoreParser.Else_statementContext,0)


        def getRuleIndex(self):
            return ignoreParser.RULE_control_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterControl_statement" ):
                listener.enterControl_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitControl_statement" ):
                listener.exitControl_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitControl_statement" ):
                return visitor.visitControl_statement(self)
            else:
                return visitor.visitChildren(self)




    def control_statement(self):

        localctx = ignoreParser.Control_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_control_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.if_statement()
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 173
                self.elif_statement()
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 179
                self.else_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PROGRAM(self):
            return self.getToken(ignoreParser.OPEN_PROGRAM, 0)

        def CLOSE_PROGRAM(self):
            return self.getToken(ignoreParser.CLOSE_PROGRAM, 0)

        def EOF(self):
            return self.getToken(ignoreParser.EOF, 0)

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ignoreParser.FunctionContext)
            else:
                return self.getTypedRuleContext(ignoreParser.FunctionContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ignoreParser.BlockContext)
            else:
                return self.getTypedRuleContext(ignoreParser.BlockContext,i)


        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ignoreParser.VarContext)
            else:
                return self.getTypedRuleContext(ignoreParser.VarContext,i)


        def getRuleIndex(self):
            return ignoreParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ignoreParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 182
                self.function()
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 188
            self.match(ignoreParser.OPEN_PROGRAM)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 26307030018) != 0):
                self.state = 191
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 189
                    self.block()
                    pass

                elif la_ == 2:
                    self.state = 190
                    self.var()
                    pass


                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 196
            self.match(ignoreParser.CLOSE_PROGRAM)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 197
                self.function()
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 203
            self.match(ignoreParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROPERTY_NAME(self):
            return self.getToken(ignoreParser.PROPERTY_NAME, 0)

        def wrapped_expr(self):
            return self.getTypedRuleContext(ignoreParser.Wrapped_exprContext,0)


        def TAG_REFERENCE(self):
            return self.getToken(ignoreParser.TAG_REFERENCE, 0)

        def getRuleIndex(self):
            return ignoreParser.RULE_property

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProperty" ):
                listener.enterProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProperty" ):
                listener.exitProperty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProperty" ):
                return visitor.visitProperty(self)
            else:
                return visitor.visitChildren(self)




    def property_(self):

        localctx = ignoreParser.PropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(ignoreParser.PROPERTY_NAME)
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.state = 206
                self.wrapped_expr()
                pass
            elif token in [30]:
                self.state = 207
                self.match(ignoreParser.TAG_REFERENCE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndTagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLOSE_TAG(self):
            return self.getToken(ignoreParser.CLOSE_TAG, 0)

        def END_TAG(self):
            return self.getToken(ignoreParser.END_TAG, 0)

        def getRuleIndex(self):
            return ignoreParser.RULE_endTag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndTag" ):
                listener.enterEndTag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndTag" ):
                listener.exitEndTag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndTag" ):
                return visitor.visitEndTag(self)
            else:
                return visitor.visitChildren(self)




    def endTag(self):

        localctx = ignoreParser.EndTagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_endTag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(ignoreParser.CLOSE_TAG)
            self.state = 211
            self.match(ignoreParser.END_TAG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StartTagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_TAG(self):
            return self.getToken(ignoreParser.OPEN_TAG, 0)

        def END_TAG(self):
            return self.getToken(ignoreParser.END_TAG, 0)

        def property_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ignoreParser.PropertyContext)
            else:
                return self.getTypedRuleContext(ignoreParser.PropertyContext,i)


        def getRuleIndex(self):
            return ignoreParser.RULE_startTag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStartTag" ):
                listener.enterStartTag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStartTag" ):
                listener.exitStartTag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStartTag" ):
                return visitor.visitStartTag(self)
            else:
                return visitor.visitChildren(self)




    def startTag(self):

        localctx = ignoreParser.StartTagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_startTag)
        self._la = 0 # Token type
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.match(ignoreParser.OPEN_TAG)
                self.state = 214
                self.match(ignoreParser.END_TAG)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.match(ignoreParser.OPEN_TAG)
                self.state = 217 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 216
                    self.property_()
                    self.state = 219 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==33):
                        break

                self.state = 221
                self.match(ignoreParser.END_TAG)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def startTag(self):
            return self.getTypedRuleContext(ignoreParser.StartTagContext,0)


        def wrapped_expr(self):
            return self.getTypedRuleContext(ignoreParser.Wrapped_exprContext,0)


        def endTag(self):
            return self.getTypedRuleContext(ignoreParser.EndTagContext,0)


        def function(self):
            return self.getTypedRuleContext(ignoreParser.FunctionContext,0)


        def control_statement(self):
            return self.getTypedRuleContext(ignoreParser.Control_statementContext,0)


        def var(self):
            return self.getTypedRuleContext(ignoreParser.VarContext,0)


        def var_assign(self):
            return self.getTypedRuleContext(ignoreParser.Var_assignContext,0)


        def for_loop(self):
            return self.getTypedRuleContext(ignoreParser.For_loopContext,0)


        def while_loop(self):
            return self.getTypedRuleContext(ignoreParser.While_loopContext,0)


        def getRuleIndex(self):
            return ignoreParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ignoreParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_statement)
        try:
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.startTag()
                self.state = 226
                self.wrapped_expr()
                self.state = 227
                self.endTag()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.wrapped_expr()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 230
                self.function()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 4)
                self.state = 231
                self.control_statement()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 232
                self.var()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 6)
                self.state = 233
                self.var_assign()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 7)
                self.state = 234
                self.for_loop()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 8)
                self.state = 235
                self.while_loop()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ignoreParser.StatementContext)
            else:
                return self.getTypedRuleContext(ignoreParser.StatementContext,i)


        def returnStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ignoreParser.ReturnStmtContext)
            else:
                return self.getTypedRuleContext(ignoreParser.ReturnStmtContext,i)


        def break_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ignoreParser.BreakContext)
            else:
                return self.getTypedRuleContext(ignoreParser.BreakContext,i)


        def getRuleIndex(self):
            return ignoreParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = ignoreParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 241
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 10, 11, 14, 16, 29, 33, 34]:
                        self.state = 238
                        self.statement()
                        pass
                    elif token in [18]:
                        self.state = 239
                        self.returnStmt()
                        pass
                    elif token in [13]:
                        self.state = 240
                        self.break_()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 243 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PAREN(self):
            return self.getToken(ignoreParser.OPEN_PAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ignoreParser.ExprContext)
            else:
                return self.getTypedRuleContext(ignoreParser.ExprContext,i)


        def CLOSE_PAREN(self):
            return self.getToken(ignoreParser.CLOSE_PAREN, 0)

        def SUB(self):
            return self.getToken(ignoreParser.SUB, 0)

        def literal(self):
            return self.getTypedRuleContext(ignoreParser.LiteralContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(ignoreParser.FunctionCallContext,0)


        def NOT(self):
            return self.getToken(ignoreParser.NOT, 0)

        def NAME(self):
            return self.getToken(ignoreParser.NAME, 0)

        def MUL(self):
            return self.getToken(ignoreParser.MUL, 0)

        def DIV(self):
            return self.getToken(ignoreParser.DIV, 0)

        def MOD(self):
            return self.getToken(ignoreParser.MOD, 0)

        def INT_DIV(self):
            return self.getToken(ignoreParser.INT_DIV, 0)

        def ADD(self):
            return self.getToken(ignoreParser.ADD, 0)

        def OPERATOR_COMPARE(self):
            return self.getToken(ignoreParser.OPERATOR_COMPARE, 0)

        def OPERATOR_LOGIC(self):
            return self.getToken(ignoreParser.OPERATOR_LOGIC, 0)

        def getRuleIndex(self):
            return ignoreParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ignoreParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 246
                self.match(ignoreParser.OPEN_PAREN)
                self.state = 247
                self.expr(0)
                self.state = 248
                self.match(ignoreParser.CLOSE_PAREN)
                pass

            elif la_ == 2:
                self.state = 250
                self.match(ignoreParser.SUB)
                self.state = 251
                self.expr(9)
                pass

            elif la_ == 3:
                self.state = 252
                self.literal()
                pass

            elif la_ == 4:
                self.state = 253
                self.functionCall()
                pass

            elif la_ == 5:
                self.state = 254
                self.match(ignoreParser.NOT)
                self.state = 255
                self.expr(2)
                pass

            elif la_ == 6:
                self.state = 256
                self.match(ignoreParser.NAME)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 273
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 271
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 259
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 260
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 897201488265216) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 261
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 262
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 263
                        _la = self._input.LA(1)
                        if not(_la==46 or _la==47):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 264
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 265
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")

                        self.state = 266
                        self.match(ignoreParser.OPERATOR_COMPARE)
                        self.state = 267
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 268
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")

                        self.state = 269
                        self.match(ignoreParser.OPERATOR_LOGIC)
                        self.state = 270
                        self.expr(6)
                        pass

             
                self.state = 275
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Wrapped_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_CURLY(self):
            return self.getToken(ignoreParser.OPEN_CURLY, 0)

        def expr(self):
            return self.getTypedRuleContext(ignoreParser.ExprContext,0)


        def CLOSE_CURLY(self):
            return self.getToken(ignoreParser.CLOSE_CURLY, 0)

        def getRuleIndex(self):
            return ignoreParser.RULE_wrapped_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrapped_expr" ):
                listener.enterWrapped_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrapped_expr" ):
                listener.exitWrapped_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrapped_expr" ):
                return visitor.visitWrapped_expr(self)
            else:
                return visitor.visitChildren(self)




    def wrapped_expr(self):

        localctx = ignoreParser.Wrapped_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_wrapped_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(ignoreParser.OPEN_CURLY)
            self.state = 277
            self.expr(0)
            self.state = 278
            self.match(ignoreParser.CLOSE_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[27] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         




