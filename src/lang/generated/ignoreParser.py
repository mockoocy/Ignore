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
        4,1,55,267,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,3,2,63,8,2,1,2,1,2,1,2,1,2,1,2,3,
        2,70,8,2,1,3,1,3,1,3,3,3,75,8,3,1,3,3,3,78,8,3,1,3,1,3,5,3,82,8,
        3,10,3,12,3,85,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,3,5,96,8,
        5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,
        9,1,9,1,9,1,9,3,9,117,8,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,
        10,1,11,1,11,3,11,130,8,11,1,12,1,12,3,12,134,8,12,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,18,1,18,5,18,
        164,8,18,10,18,12,18,167,9,18,1,18,3,18,170,8,18,1,19,5,19,173,8,
        19,10,19,12,19,176,9,19,1,19,1,19,1,19,5,19,181,8,19,10,19,12,19,
        184,9,19,1,19,1,19,5,19,188,8,19,10,19,12,19,191,9,19,1,19,1,19,
        1,20,1,20,1,20,3,20,198,8,20,1,21,1,21,1,21,1,22,1,22,1,22,1,22,
        4,22,207,8,22,11,22,12,22,208,1,22,1,22,3,22,213,8,22,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,226,8,23,1,24,
        1,24,4,24,230,8,24,11,24,12,24,231,1,25,1,25,1,25,1,25,1,25,1,25,
        1,25,1,25,1,25,1,25,3,25,244,8,25,1,25,1,25,1,25,1,25,1,25,1,25,
        1,25,1,25,1,25,1,25,1,25,1,25,5,25,258,8,25,10,25,12,25,261,9,25,
        1,26,1,26,1,26,1,26,1,26,0,1,50,27,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,0,4,1,0,41,42,3,0,35,
        35,37,37,41,42,2,0,44,45,48,49,1,0,46,47,274,0,54,1,0,0,0,2,56,1,
        0,0,0,4,69,1,0,0,0,6,71,1,0,0,0,8,88,1,0,0,0,10,92,1,0,0,0,12,99,
        1,0,0,0,14,103,1,0,0,0,16,106,1,0,0,0,18,112,1,0,0,0,20,122,1,0,
        0,0,22,129,1,0,0,0,24,133,1,0,0,0,26,135,1,0,0,0,28,142,1,0,0,0,
        30,146,1,0,0,0,32,153,1,0,0,0,34,157,1,0,0,0,36,161,1,0,0,0,38,174,
        1,0,0,0,40,194,1,0,0,0,42,199,1,0,0,0,44,212,1,0,0,0,46,225,1,0,
        0,0,48,229,1,0,0,0,50,243,1,0,0,0,52,262,1,0,0,0,54,55,7,0,0,0,55,
        1,1,0,0,0,56,57,7,1,0,0,57,3,1,0,0,0,58,59,5,36,0,0,59,62,5,39,0,
        0,60,63,3,50,25,0,61,63,3,2,1,0,62,60,1,0,0,0,62,61,1,0,0,0,63,64,
        1,0,0,0,64,65,5,40,0,0,65,70,1,0,0,0,66,67,5,36,0,0,67,68,5,39,0,
        0,68,70,5,40,0,0,69,58,1,0,0,0,69,66,1,0,0,0,70,5,1,0,0,0,71,72,
        5,15,0,0,72,74,5,19,0,0,73,75,5,21,0,0,74,73,1,0,0,0,74,75,1,0,0,
        0,75,77,1,0,0,0,76,78,5,20,0,0,77,76,1,0,0,0,77,78,1,0,0,0,78,79,
        1,0,0,0,79,83,5,31,0,0,80,82,3,48,24,0,81,80,1,0,0,0,82,85,1,0,0,
        0,83,81,1,0,0,0,83,84,1,0,0,0,84,86,1,0,0,0,85,83,1,0,0,0,86,87,
        5,16,0,0,87,7,1,0,0,0,88,89,5,17,0,0,89,90,3,52,26,0,90,91,5,18,
        0,0,91,9,1,0,0,0,92,93,5,10,0,0,93,95,5,19,0,0,94,96,5,9,0,0,95,
        94,1,0,0,0,95,96,1,0,0,0,96,97,1,0,0,0,97,98,5,31,0,0,98,11,1,0,
        0,0,99,100,3,10,5,0,100,101,3,52,26,0,101,102,5,8,0,0,102,13,1,0,
        0,0,103,104,5,32,0,0,104,105,3,52,26,0,105,15,1,0,0,0,106,107,5,
        11,0,0,107,108,3,20,10,0,108,109,5,31,0,0,109,110,3,48,24,0,110,
        111,5,12,0,0,111,17,1,0,0,0,112,113,5,13,0,0,113,114,3,22,11,0,114,
        116,3,20,10,0,115,117,3,14,7,0,116,115,1,0,0,0,116,117,1,0,0,0,117,
        118,1,0,0,0,118,119,5,31,0,0,119,120,3,48,24,0,120,121,5,14,0,0,
        121,19,1,0,0,0,122,123,5,30,0,0,123,124,5,33,0,0,124,125,3,24,12,
        0,125,126,5,54,0,0,126,21,1,0,0,0,127,130,3,12,6,0,128,130,5,29,
        0,0,129,127,1,0,0,0,129,128,1,0,0,0,130,23,1,0,0,0,131,134,3,50,
        25,0,132,134,5,35,0,0,133,131,1,0,0,0,133,132,1,0,0,0,134,25,1,0,
        0,0,135,136,5,1,0,0,136,137,5,30,0,0,137,138,5,33,0,0,138,139,3,
        24,12,0,139,140,5,54,0,0,140,141,5,31,0,0,141,27,1,0,0,0,142,143,
        3,26,13,0,143,144,3,48,24,0,144,145,5,2,0,0,145,29,1,0,0,0,146,147,
        5,4,0,0,147,148,5,30,0,0,148,149,5,33,0,0,149,150,3,24,12,0,150,
        151,5,54,0,0,151,152,5,31,0,0,152,31,1,0,0,0,153,154,3,30,15,0,154,
        155,3,48,24,0,155,156,5,3,0,0,156,33,1,0,0,0,157,158,5,5,0,0,158,
        159,3,48,24,0,159,160,5,6,0,0,160,35,1,0,0,0,161,165,3,28,14,0,162,
        164,3,32,16,0,163,162,1,0,0,0,164,167,1,0,0,0,165,163,1,0,0,0,165,
        166,1,0,0,0,166,169,1,0,0,0,167,165,1,0,0,0,168,170,3,34,17,0,169,
        168,1,0,0,0,169,170,1,0,0,0,170,37,1,0,0,0,171,173,3,6,3,0,172,171,
        1,0,0,0,173,176,1,0,0,0,174,172,1,0,0,0,174,175,1,0,0,0,175,177,
        1,0,0,0,176,174,1,0,0,0,177,182,5,25,0,0,178,181,3,48,24,0,179,181,
        3,12,6,0,180,178,1,0,0,0,180,179,1,0,0,0,181,184,1,0,0,0,182,180,
        1,0,0,0,182,183,1,0,0,0,183,185,1,0,0,0,184,182,1,0,0,0,185,189,
        5,26,0,0,186,188,3,6,3,0,187,186,1,0,0,0,188,191,1,0,0,0,189,187,
        1,0,0,0,189,190,1,0,0,0,190,192,1,0,0,0,191,189,1,0,0,0,192,193,
        5,0,0,1,193,39,1,0,0,0,194,197,5,32,0,0,195,198,3,52,26,0,196,198,
        5,29,0,0,197,195,1,0,0,0,197,196,1,0,0,0,198,41,1,0,0,0,199,200,
        5,27,0,0,200,201,5,31,0,0,201,43,1,0,0,0,202,203,5,28,0,0,203,213,
        5,31,0,0,204,206,5,28,0,0,205,207,3,40,20,0,206,205,1,0,0,0,207,
        208,1,0,0,0,208,206,1,0,0,0,208,209,1,0,0,0,209,210,1,0,0,0,210,
        211,5,31,0,0,211,213,1,0,0,0,212,202,1,0,0,0,212,204,1,0,0,0,213,
        45,1,0,0,0,214,215,3,44,22,0,215,216,3,52,26,0,216,217,3,42,21,0,
        217,226,1,0,0,0,218,226,3,52,26,0,219,226,3,6,3,0,220,226,3,36,18,
        0,221,226,3,12,6,0,222,226,3,14,7,0,223,226,3,18,9,0,224,226,3,16,
        8,0,225,214,1,0,0,0,225,218,1,0,0,0,225,219,1,0,0,0,225,220,1,0,
        0,0,225,221,1,0,0,0,225,222,1,0,0,0,225,223,1,0,0,0,225,224,1,0,
        0,0,226,47,1,0,0,0,227,230,3,46,23,0,228,230,3,8,4,0,229,227,1,0,
        0,0,229,228,1,0,0,0,230,231,1,0,0,0,231,229,1,0,0,0,231,232,1,0,
        0,0,232,49,1,0,0,0,233,234,6,25,-1,0,234,235,5,39,0,0,235,236,3,
        50,25,0,236,237,5,40,0,0,237,244,1,0,0,0,238,244,3,2,1,0,239,244,
        3,4,2,0,240,241,5,50,0,0,241,244,3,50,25,6,242,244,5,36,0,0,243,
        233,1,0,0,0,243,238,1,0,0,0,243,239,1,0,0,0,243,240,1,0,0,0,243,
        242,1,0,0,0,244,259,1,0,0,0,245,246,10,5,0,0,246,247,7,2,0,0,247,
        258,3,50,25,6,248,249,10,4,0,0,249,250,7,3,0,0,250,258,3,50,25,5,
        251,252,10,3,0,0,252,253,5,51,0,0,253,258,3,50,25,4,254,255,10,2,
        0,0,255,256,5,52,0,0,256,258,3,50,25,3,257,245,1,0,0,0,257,248,1,
        0,0,0,257,251,1,0,0,0,257,254,1,0,0,0,258,261,1,0,0,0,259,257,1,
        0,0,0,259,260,1,0,0,0,260,51,1,0,0,0,261,259,1,0,0,0,262,263,5,33,
        0,0,263,264,3,50,25,0,264,265,5,54,0,0,265,53,1,0,0,0,24,62,69,74,
        77,83,95,116,129,133,165,169,174,180,182,189,197,208,212,225,229,
        231,243,257,259
    ]

class ignoreParser ( Parser ):

    grammarFileName = "ignoreParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<if'", "'</if>'", "'</elif>'", "'<elif'", 
                     "'<else>'", "'</else>'", "'<var'", "'</var>'", "<INVALID>", 
                     "<INVALID>", "'<while'", "'</while>'", "'<for'", "'</for>'", 
                     "'<function'", "'</function>'", "'<return>'", "'</return>'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'<program>'", "'</program>'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'condition='", 
                     "'>'", "<INVALID>", "'{'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "':'", "'('", "')'", "<INVALID>", 
                     "<INVALID>", "'='", "'*'", "'/'", "'+'", "'-'", "'%'", 
                     "'//'", "'!'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "IF_TAG", "IF_END", "ELIF_END", "ELIF_TAG", 
                      "ELSE", "ELSE_END", "VAR_DECL_START", "VAR_DECL_END", 
                      "VAR_DECL_TYPE", "VAR_DECL", "WHILE_TAG", "WHILE_END", 
                      "FOR_TAG", "FOR_END", "FUNCTION_TAG_OPEN", "FUNCTION_TAG_END", 
                      "RETURN_TAG", "RETURN_END", "FUNCTION_NAME", "FUNCTION_RET_TYPE", 
                      "FUNCTION_PARAM", "COMMENT", "LINE_COMMENT", "WS", 
                      "OPEN_PROGRAM", "CLOSE_PROGRAM", "CLOSE_TAG", "OPEN_TAG", 
                      "TAG_REFERENCE", "CONDITION_EQ", "END_TAG", "PROPERTY_NAME", 
                      "OPEN_CURLY", "EXPR_WS", "LITERAL_BOOL", "NAME", "LITERAL_STRING", 
                      "COLON", "OPEN_PAREN", "CLOSE_PAREN", "LITERAL_INT", 
                      "LITERAL_FLOAT", "EQUALS", "MUL", "DIV", "ADD", "SUB", 
                      "MOD", "INT_DIV", "NOT", "OPERATOR_COMPARE", "OPERATOR_LOGIC", 
                      "EXPR_COMMENT", "CLOSE_CURLY", "EXPR_LINE_COMMENT" ]

    RULE_literalNumeric = 0
    RULE_literal = 1
    RULE_functionCall = 2
    RULE_function = 3
    RULE_returnStmt = 4
    RULE_varDecl = 5
    RULE_var = 6
    RULE_var_assign = 7
    RULE_while_loop = 8
    RULE_for_loop = 9
    RULE_loop_condition = 10
    RULE_loop_init = 11
    RULE_condition = 12
    RULE_if = 13
    RULE_if_statement = 14
    RULE_elif = 15
    RULE_elif_statement = 16
    RULE_else_statement = 17
    RULE_control_statement = 18
    RULE_program = 19
    RULE_property = 20
    RULE_endTag = 21
    RULE_startTag = 22
    RULE_statement = 23
    RULE_block = 24
    RULE_expr = 25
    RULE_wrapped_expr = 26

    ruleNames =  [ "literalNumeric", "literal", "functionCall", "function", 
                   "returnStmt", "varDecl", "var", "var_assign", "while_loop", 
                   "for_loop", "loop_condition", "loop_init", "condition", 
                   "if", "if_statement", "elif", "elif_statement", "else_statement", 
                   "control_statement", "program", "property", "endTag", 
                   "startTag", "statement", "block", "expr", "wrapped_expr" ]

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
    FOR_TAG=13
    FOR_END=14
    FUNCTION_TAG_OPEN=15
    FUNCTION_TAG_END=16
    RETURN_TAG=17
    RETURN_END=18
    FUNCTION_NAME=19
    FUNCTION_RET_TYPE=20
    FUNCTION_PARAM=21
    COMMENT=22
    LINE_COMMENT=23
    WS=24
    OPEN_PROGRAM=25
    CLOSE_PROGRAM=26
    CLOSE_TAG=27
    OPEN_TAG=28
    TAG_REFERENCE=29
    CONDITION_EQ=30
    END_TAG=31
    PROPERTY_NAME=32
    OPEN_CURLY=33
    EXPR_WS=34
    LITERAL_BOOL=35
    NAME=36
    LITERAL_STRING=37
    COLON=38
    OPEN_PAREN=39
    CLOSE_PAREN=40
    LITERAL_INT=41
    LITERAL_FLOAT=42
    EQUALS=43
    MUL=44
    DIV=45
    ADD=46
    SUB=47
    MOD=48
    INT_DIV=49
    NOT=50
    OPERATOR_COMPARE=51
    OPERATOR_LOGIC=52
    EXPR_COMMENT=53
    CLOSE_CURLY=54
    EXPR_LINE_COMMENT=55

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




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
        self.enterRule(localctx, 0, self.RULE_literalNumeric)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            _la = self._input.LA(1)
            if not(_la==41 or _la==42):
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
        self.enterRule(localctx, 2, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6768868458496) != 0)):
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


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(ignoreParser.NAME, 0)

        def OPEN_PAREN(self):
            return self.getToken(ignoreParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(ignoreParser.CLOSE_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ignoreParser.ExprContext,0)


        def literal(self):
            return self.getTypedRuleContext(ignoreParser.LiteralContext,0)


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
        self.enterRule(localctx, 4, self.RULE_functionCall)
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.match(ignoreParser.NAME)
                self.state = 59
                self.match(ignoreParser.OPEN_PAREN)
                self.state = 62
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 60
                    self.expr(0)
                    pass

                elif la_ == 2:
                    self.state = 61
                    self.literal()
                    pass


                self.state = 64
                self.match(ignoreParser.CLOSE_PAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.match(ignoreParser.NAME)
                self.state = 67
                self.match(ignoreParser.OPEN_PAREN)
                self.state = 68
                self.match(ignoreParser.CLOSE_PAREN)
                pass


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

        def FUNCTION_TAG_END(self):
            return self.getToken(ignoreParser.FUNCTION_TAG_END, 0)

        def FUNCTION_PARAM(self):
            return self.getToken(ignoreParser.FUNCTION_PARAM, 0)

        def FUNCTION_RET_TYPE(self):
            return self.getToken(ignoreParser.FUNCTION_RET_TYPE, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ignoreParser.BlockContext)
            else:
                return self.getTypedRuleContext(ignoreParser.BlockContext,i)


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
        self.enterRule(localctx, 6, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(ignoreParser.FUNCTION_TAG_OPEN)
            self.state = 72
            self.match(ignoreParser.FUNCTION_NAME)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 73
                self.match(ignoreParser.FUNCTION_PARAM)


            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 76
                self.match(ignoreParser.FUNCTION_RET_TYPE)


            self.state = 79
            self.match(ignoreParser.END_TAG)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 13153512450) != 0):
                self.state = 80
                self.block()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
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
        self.enterRule(localctx, 8, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(ignoreParser.RETURN_TAG)
            self.state = 89
            self.wrapped_expr()
            self.state = 90
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
        self.enterRule(localctx, 10, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(ignoreParser.VAR_DECL)
            self.state = 93
            self.match(ignoreParser.FUNCTION_NAME)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 94
                self.match(ignoreParser.VAR_DECL_TYPE)


            self.state = 97
            self.match(ignoreParser.END_TAG)
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
        self.enterRule(localctx, 12, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.varDecl()
            self.state = 100
            self.wrapped_expr()
            self.state = 101
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
        self.enterRule(localctx, 14, self.RULE_var_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(ignoreParser.PROPERTY_NAME)
            self.state = 104
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
        self.enterRule(localctx, 16, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(ignoreParser.WHILE_TAG)
            self.state = 107
            self.loop_condition()
            self.state = 108
            self.match(ignoreParser.END_TAG)
            self.state = 109
            self.block()
            self.state = 110
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

        def loop_init(self):
            return self.getTypedRuleContext(ignoreParser.Loop_initContext,0)


        def loop_condition(self):
            return self.getTypedRuleContext(ignoreParser.Loop_conditionContext,0)


        def END_TAG(self):
            return self.getToken(ignoreParser.END_TAG, 0)

        def block(self):
            return self.getTypedRuleContext(ignoreParser.BlockContext,0)


        def FOR_END(self):
            return self.getToken(ignoreParser.FOR_END, 0)

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
        self.enterRule(localctx, 18, self.RULE_for_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(ignoreParser.FOR_TAG)
            self.state = 113
            self.loop_init()
            self.state = 114
            self.loop_condition()
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 115
                self.var_assign()


            self.state = 118
            self.match(ignoreParser.END_TAG)
            self.state = 119
            self.block()
            self.state = 120
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
        self.enterRule(localctx, 20, self.RULE_loop_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(ignoreParser.CONDITION_EQ)
            self.state = 123
            self.match(ignoreParser.OPEN_CURLY)

            self.state = 124
            self.condition()
            self.state = 125
            self.match(ignoreParser.CLOSE_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(ignoreParser.VarContext,0)


        def TAG_REFERENCE(self):
            return self.getToken(ignoreParser.TAG_REFERENCE, 0)

        def getRuleIndex(self):
            return ignoreParser.RULE_loop_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_init" ):
                listener.enterLoop_init(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_init" ):
                listener.exitLoop_init(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_init" ):
                return visitor.visitLoop_init(self)
            else:
                return visitor.visitChildren(self)




    def loop_init(self):

        localctx = ignoreParser.Loop_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_loop_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.state = 127
                self.var()
                pass
            elif token in [29]:
                self.state = 128
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
        self.enterRule(localctx, 24, self.RULE_condition)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
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
        self.enterRule(localctx, 26, self.RULE_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(ignoreParser.IF_TAG)
            self.state = 136
            self.match(ignoreParser.CONDITION_EQ)
            self.state = 137
            self.match(ignoreParser.OPEN_CURLY)

            self.state = 138
            self.condition()
            self.state = 139
            self.match(ignoreParser.CLOSE_CURLY)
            self.state = 140
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
        self.enterRule(localctx, 28, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.if_()
            self.state = 143
            self.block()
            self.state = 144
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
        self.enterRule(localctx, 30, self.RULE_elif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(ignoreParser.ELIF_TAG)
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
        self.enterRule(localctx, 32, self.RULE_elif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.elif_()
            self.state = 154
            self.block()
            self.state = 155
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
        self.enterRule(localctx, 34, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(ignoreParser.ELSE)
            self.state = 158
            self.block()
            self.state = 159
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
        self.enterRule(localctx, 36, self.RULE_control_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.if_statement()
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 162
                self.elif_statement()
                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 168
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
        self.enterRule(localctx, 38, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 171
                self.function()
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 177
            self.match(ignoreParser.OPEN_PROGRAM)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 13153512450) != 0):
                self.state = 180
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 178
                    self.block()
                    pass

                elif la_ == 2:
                    self.state = 179
                    self.var()
                    pass


                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 185
            self.match(ignoreParser.CLOSE_PROGRAM)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 186
                self.function()
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 192
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
        self.enterRule(localctx, 40, self.RULE_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(ignoreParser.PROPERTY_NAME)
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.state = 195
                self.wrapped_expr()
                pass
            elif token in [29]:
                self.state = 196
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
        self.enterRule(localctx, 42, self.RULE_endTag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(ignoreParser.CLOSE_TAG)
            self.state = 200
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
        self.enterRule(localctx, 44, self.RULE_startTag)
        self._la = 0 # Token type
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.match(ignoreParser.OPEN_TAG)
                self.state = 203
                self.match(ignoreParser.END_TAG)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.match(ignoreParser.OPEN_TAG)
                self.state = 206 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 205
                    self.property_()
                    self.state = 208 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==32):
                        break

                self.state = 210
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
        self.enterRule(localctx, 46, self.RULE_statement)
        try:
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.startTag()
                self.state = 215
                self.wrapped_expr()
                self.state = 216
                self.endTag()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.wrapped_expr()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 219
                self.function()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 4)
                self.state = 220
                self.control_statement()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 221
                self.var()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 6)
                self.state = 222
                self.var_assign()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 7)
                self.state = 223
                self.for_loop()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 8)
                self.state = 224
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
        self.enterRule(localctx, 48, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 229
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 10, 11, 13, 15, 28, 32, 33]:
                        self.state = 227
                        self.statement()
                        pass
                    elif token in [17]:
                        self.state = 228
                        self.returnStmt()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 231 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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

        def SUB(self):
            return self.getToken(ignoreParser.SUB, 0)

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
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 234
                self.match(ignoreParser.OPEN_PAREN)
                self.state = 235
                self.expr(0)
                self.state = 236
                self.match(ignoreParser.CLOSE_PAREN)
                pass

            elif la_ == 2:
                self.state = 238
                self.literal()
                pass

            elif la_ == 3:
                self.state = 239
                self.functionCall()
                pass

            elif la_ == 4:
                self.state = 240
                self.match(ignoreParser.NOT)
                self.state = 241
                self.expr(6)
                pass

            elif la_ == 5:
                self.state = 242
                self.match(ignoreParser.NAME)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 259
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 257
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 245
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 246
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 897201488265216) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 247
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 248
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 249
                        _la = self._input.LA(1)
                        if not(_la==46 or _la==47):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 250
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 251
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")

                        self.state = 252
                        self.match(ignoreParser.OPERATOR_COMPARE)
                        self.state = 253
                        self.expr(4)
                        pass

                    elif la_ == 4:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 254
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                        self.state = 255
                        self.match(ignoreParser.OPERATOR_LOGIC)
                        self.state = 256
                        self.expr(3)
                        pass

             
                self.state = 261
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
        self.enterRule(localctx, 52, self.RULE_wrapped_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(ignoreParser.OPEN_CURLY)
            self.state = 263
            self.expr(0)
            self.state = 264
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
        self._predicates[25] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




