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
        4,1,53,265,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,3,2,63,8,2,1,2,1,2,1,2,1,2,1,2,3,
        2,70,8,2,1,3,1,3,1,3,5,3,75,8,3,10,3,12,3,78,9,3,1,3,1,3,1,3,1,4,
        1,4,5,4,85,8,4,10,4,12,4,88,9,4,1,4,1,4,1,5,1,5,1,5,3,5,95,8,5,1,
        5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,
        9,1,9,1,9,3,9,116,8,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,
        11,1,11,3,11,129,8,11,1,12,1,12,3,12,133,8,12,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,18,1,18,5,18,163,
        8,18,10,18,12,18,166,9,18,1,18,3,18,169,8,18,1,19,5,19,172,8,19,
        10,19,12,19,175,9,19,1,19,1,19,1,19,5,19,180,8,19,10,19,12,19,183,
        9,19,1,19,1,19,5,19,187,8,19,10,19,12,19,190,9,19,1,19,1,19,1,20,
        1,20,1,20,3,20,197,8,20,1,21,1,21,1,21,1,22,1,22,1,22,1,22,4,22,
        206,8,22,11,22,12,22,207,1,22,1,22,3,22,212,8,22,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,225,8,23,1,24,4,24,
        228,8,24,11,24,12,24,229,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,
        1,25,1,25,3,25,242,8,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,
        1,25,1,25,1,25,1,25,5,25,256,8,25,10,25,12,25,259,9,25,1,26,1,26,
        1,26,1,26,1,26,0,1,50,27,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,0,4,1,0,39,40,3,0,33,33,35,35,
        39,40,2,0,42,43,46,47,1,0,44,45,270,0,54,1,0,0,0,2,56,1,0,0,0,4,
        69,1,0,0,0,6,71,1,0,0,0,8,82,1,0,0,0,10,91,1,0,0,0,12,98,1,0,0,0,
        14,102,1,0,0,0,16,105,1,0,0,0,18,111,1,0,0,0,20,121,1,0,0,0,22,128,
        1,0,0,0,24,132,1,0,0,0,26,134,1,0,0,0,28,141,1,0,0,0,30,145,1,0,
        0,0,32,152,1,0,0,0,34,156,1,0,0,0,36,160,1,0,0,0,38,173,1,0,0,0,
        40,193,1,0,0,0,42,198,1,0,0,0,44,211,1,0,0,0,46,224,1,0,0,0,48,227,
        1,0,0,0,50,241,1,0,0,0,52,260,1,0,0,0,54,55,7,0,0,0,55,1,1,0,0,0,
        56,57,7,1,0,0,57,3,1,0,0,0,58,59,5,34,0,0,59,62,5,37,0,0,60,63,3,
        50,25,0,61,63,3,2,1,0,62,60,1,0,0,0,62,61,1,0,0,0,63,64,1,0,0,0,
        64,65,5,38,0,0,65,70,1,0,0,0,66,67,5,34,0,0,67,68,5,37,0,0,68,70,
        5,38,0,0,69,58,1,0,0,0,69,66,1,0,0,0,70,5,1,0,0,0,71,72,5,1,0,0,
        72,76,5,25,0,0,73,75,5,27,0,0,74,73,1,0,0,0,75,78,1,0,0,0,76,74,
        1,0,0,0,76,77,1,0,0,0,77,79,1,0,0,0,78,76,1,0,0,0,79,80,5,26,0,0,
        80,81,5,29,0,0,81,7,1,0,0,0,82,86,3,6,3,0,83,85,3,48,24,0,84,83,
        1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,89,1,0,0,0,
        88,86,1,0,0,0,89,90,5,2,0,0,90,9,1,0,0,0,91,92,5,12,0,0,92,94,5,
        25,0,0,93,95,5,11,0,0,94,93,1,0,0,0,94,95,1,0,0,0,95,96,1,0,0,0,
        96,97,5,29,0,0,97,11,1,0,0,0,98,99,3,10,5,0,99,100,3,52,26,0,100,
        101,5,10,0,0,101,13,1,0,0,0,102,103,5,30,0,0,103,104,3,52,26,0,104,
        15,1,0,0,0,105,106,5,13,0,0,106,107,3,20,10,0,107,108,5,29,0,0,108,
        109,3,48,24,0,109,110,5,14,0,0,110,17,1,0,0,0,111,112,5,15,0,0,112,
        113,3,22,11,0,113,115,3,20,10,0,114,116,3,14,7,0,115,114,1,0,0,0,
        115,116,1,0,0,0,116,117,1,0,0,0,117,118,5,29,0,0,118,119,3,48,24,
        0,119,120,5,16,0,0,120,19,1,0,0,0,121,122,5,28,0,0,122,123,5,31,
        0,0,123,124,3,24,12,0,124,125,5,52,0,0,125,21,1,0,0,0,126,129,3,
        12,6,0,127,129,5,24,0,0,128,126,1,0,0,0,128,127,1,0,0,0,129,23,1,
        0,0,0,130,133,3,50,25,0,131,133,5,33,0,0,132,130,1,0,0,0,132,131,
        1,0,0,0,133,25,1,0,0,0,134,135,5,3,0,0,135,136,5,28,0,0,136,137,
        5,31,0,0,137,138,3,24,12,0,138,139,5,52,0,0,139,140,5,29,0,0,140,
        27,1,0,0,0,141,142,3,26,13,0,142,143,3,48,24,0,143,144,5,4,0,0,144,
        29,1,0,0,0,145,146,5,6,0,0,146,147,5,28,0,0,147,148,5,31,0,0,148,
        149,3,24,12,0,149,150,5,52,0,0,150,151,5,29,0,0,151,31,1,0,0,0,152,
        153,3,30,15,0,153,154,3,48,24,0,154,155,5,5,0,0,155,33,1,0,0,0,156,
        157,5,7,0,0,157,158,3,48,24,0,158,159,5,8,0,0,159,35,1,0,0,0,160,
        164,3,28,14,0,161,163,3,32,16,0,162,161,1,0,0,0,163,166,1,0,0,0,
        164,162,1,0,0,0,164,165,1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,
        167,169,3,34,17,0,168,167,1,0,0,0,168,169,1,0,0,0,169,37,1,0,0,0,
        170,172,3,8,4,0,171,170,1,0,0,0,172,175,1,0,0,0,173,171,1,0,0,0,
        173,174,1,0,0,0,174,176,1,0,0,0,175,173,1,0,0,0,176,181,5,20,0,0,
        177,180,3,48,24,0,178,180,3,12,6,0,179,177,1,0,0,0,179,178,1,0,0,
        0,180,183,1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,184,1,0,0,
        0,183,181,1,0,0,0,184,188,5,21,0,0,185,187,3,8,4,0,186,185,1,0,0,
        0,187,190,1,0,0,0,188,186,1,0,0,0,188,189,1,0,0,0,189,191,1,0,0,
        0,190,188,1,0,0,0,191,192,5,0,0,1,192,39,1,0,0,0,193,196,5,30,0,
        0,194,197,3,52,26,0,195,197,5,24,0,0,196,194,1,0,0,0,196,195,1,0,
        0,0,197,41,1,0,0,0,198,199,5,22,0,0,199,200,5,29,0,0,200,43,1,0,
        0,0,201,202,5,23,0,0,202,212,5,29,0,0,203,205,5,23,0,0,204,206,3,
        40,20,0,205,204,1,0,0,0,206,207,1,0,0,0,207,205,1,0,0,0,207,208,
        1,0,0,0,208,209,1,0,0,0,209,210,5,29,0,0,210,212,1,0,0,0,211,201,
        1,0,0,0,211,203,1,0,0,0,212,45,1,0,0,0,213,214,3,44,22,0,214,215,
        3,52,26,0,215,216,3,42,21,0,216,225,1,0,0,0,217,225,3,52,26,0,218,
        225,3,8,4,0,219,225,3,36,18,0,220,225,3,12,6,0,221,225,3,14,7,0,
        222,225,3,18,9,0,223,225,3,16,8,0,224,213,1,0,0,0,224,217,1,0,0,
        0,224,218,1,0,0,0,224,219,1,0,0,0,224,220,1,0,0,0,224,221,1,0,0,
        0,224,222,1,0,0,0,224,223,1,0,0,0,225,47,1,0,0,0,226,228,3,46,23,
        0,227,226,1,0,0,0,228,229,1,0,0,0,229,227,1,0,0,0,229,230,1,0,0,
        0,230,49,1,0,0,0,231,232,6,25,-1,0,232,233,5,37,0,0,233,234,3,50,
        25,0,234,235,5,38,0,0,235,242,1,0,0,0,236,242,3,2,1,0,237,242,3,
        4,2,0,238,239,5,48,0,0,239,242,3,50,25,6,240,242,5,34,0,0,241,231,
        1,0,0,0,241,236,1,0,0,0,241,237,1,0,0,0,241,238,1,0,0,0,241,240,
        1,0,0,0,242,257,1,0,0,0,243,244,10,5,0,0,244,245,7,2,0,0,245,256,
        3,50,25,6,246,247,10,4,0,0,247,248,7,3,0,0,248,256,3,50,25,5,249,
        250,10,3,0,0,250,251,5,49,0,0,251,256,3,50,25,4,252,253,10,2,0,0,
        253,254,5,50,0,0,254,256,3,50,25,3,255,243,1,0,0,0,255,246,1,0,0,
        0,255,249,1,0,0,0,255,252,1,0,0,0,256,259,1,0,0,0,257,255,1,0,0,
        0,257,258,1,0,0,0,258,51,1,0,0,0,259,257,1,0,0,0,260,261,5,31,0,
        0,261,262,3,50,25,0,262,263,5,52,0,0,263,53,1,0,0,0,22,62,69,76,
        86,94,115,128,132,164,168,173,179,181,188,196,207,211,224,229,241,
        255,257
    ]

class ignoreParser ( Parser ):

    grammarFileName = "ignoreParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<function'", "'</function>'", "'<if'", 
                     "'</if>'", "'</elif>'", "'<elif'", "'<else>'", "'</else>'", 
                     "'<var'", "'</var>'", "<INVALID>", "<INVALID>", "'<while'", 
                     "'</while>'", "'<for'", "'</for>'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'<program>'", "'</program>'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'condition='", "'>'", "<INVALID>", "'{'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "':'", "'('", "')'", "<INVALID>", "<INVALID>", "'='", 
                     "'*'", "'/'", "'+'", "'-'", "'%'", "'//'", "'!'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'}'" ]

    symbolicNames = [ "<INVALID>", "FUNCTION_TAG_OPEN", "FUNCTION_TAG_END", 
                      "IF_TAG", "IF_END", "ELIF_END", "ELIF_TAG", "ELSE", 
                      "ELSE_END", "VAR_DECL_START", "VAR_DECL_END", "VAR_DECL_TYPE", 
                      "VAR_DECL", "WHILE_TAG", "WHILE_END", "FOR_TAG", "FOR_END", 
                      "COMMENT", "LINE_COMMENT", "WS", "OPEN_PROGRAM", "CLOSE_PROGRAM", 
                      "CLOSE_TAG", "OPEN_TAG", "TAG_REFERENCE", "FUNCTION_NAME", 
                      "FUNCTION_RET_TYPE", "FUNCTION_PARAM", "CONDITION_EQ", 
                      "END_TAG", "PROPERTY_NAME", "OPEN_CURLY", "EXPR_WS", 
                      "LITERAL_BOOL", "NAME", "LITERAL_STRING", "COLON", 
                      "OPEN_PAREN", "CLOSE_PAREN", "LITERAL_INT", "LITERAL_FLOAT", 
                      "EQUALS", "MUL", "DIV", "ADD", "SUB", "MOD", "INT_DIV", 
                      "NOT", "OPERATOR_COMPARE", "OPERATOR_LOGIC", "EXPR_COMMENT", 
                      "CLOSE_CURLY", "EXPR_LINE_COMMENT" ]

    RULE_literalNumeric = 0
    RULE_literal = 1
    RULE_functionCall = 2
    RULE_functionStart = 3
    RULE_function = 4
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

    ruleNames =  [ "literalNumeric", "literal", "functionCall", "functionStart", 
                   "function", "varDecl", "var", "var_assign", "while_loop", 
                   "for_loop", "loop_condition", "loop_init", "condition", 
                   "if", "if_statement", "elif", "elif_statement", "else_statement", 
                   "control_statement", "program", "property", "endTag", 
                   "startTag", "statement", "block", "expr", "wrapped_expr" ]

    EOF = Token.EOF
    FUNCTION_TAG_OPEN=1
    FUNCTION_TAG_END=2
    IF_TAG=3
    IF_END=4
    ELIF_END=5
    ELIF_TAG=6
    ELSE=7
    ELSE_END=8
    VAR_DECL_START=9
    VAR_DECL_END=10
    VAR_DECL_TYPE=11
    VAR_DECL=12
    WHILE_TAG=13
    WHILE_END=14
    FOR_TAG=15
    FOR_END=16
    COMMENT=17
    LINE_COMMENT=18
    WS=19
    OPEN_PROGRAM=20
    CLOSE_PROGRAM=21
    CLOSE_TAG=22
    OPEN_TAG=23
    TAG_REFERENCE=24
    FUNCTION_NAME=25
    FUNCTION_RET_TYPE=26
    FUNCTION_PARAM=27
    CONDITION_EQ=28
    END_TAG=29
    PROPERTY_NAME=30
    OPEN_CURLY=31
    EXPR_WS=32
    LITERAL_BOOL=33
    NAME=34
    LITERAL_STRING=35
    COLON=36
    OPEN_PAREN=37
    CLOSE_PAREN=38
    LITERAL_INT=39
    LITERAL_FLOAT=40
    EQUALS=41
    MUL=42
    DIV=43
    ADD=44
    SUB=45
    MOD=46
    INT_DIV=47
    NOT=48
    OPERATOR_COMPARE=49
    OPERATOR_LOGIC=50
    EXPR_COMMENT=51
    CLOSE_CURLY=52
    EXPR_LINE_COMMENT=53

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
            if not(_la==39 or _la==40):
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
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1692217114624) != 0)):
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


    class FunctionStartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION_TAG_OPEN(self):
            return self.getToken(ignoreParser.FUNCTION_TAG_OPEN, 0)

        def FUNCTION_NAME(self):
            return self.getToken(ignoreParser.FUNCTION_NAME, 0)

        def FUNCTION_RET_TYPE(self):
            return self.getToken(ignoreParser.FUNCTION_RET_TYPE, 0)

        def END_TAG(self):
            return self.getToken(ignoreParser.END_TAG, 0)

        def FUNCTION_PARAM(self, i:int=None):
            if i is None:
                return self.getTokens(ignoreParser.FUNCTION_PARAM)
            else:
                return self.getToken(ignoreParser.FUNCTION_PARAM, i)

        def getRuleIndex(self):
            return ignoreParser.RULE_functionStart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionStart" ):
                listener.enterFunctionStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionStart" ):
                listener.exitFunctionStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionStart" ):
                return visitor.visitFunctionStart(self)
            else:
                return visitor.visitChildren(self)




    def functionStart(self):

        localctx = ignoreParser.FunctionStartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_functionStart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(ignoreParser.FUNCTION_TAG_OPEN)
            self.state = 72
            self.match(ignoreParser.FUNCTION_NAME)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 73
                self.match(ignoreParser.FUNCTION_PARAM)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
            self.match(ignoreParser.FUNCTION_RET_TYPE)
            self.state = 80
            self.match(ignoreParser.END_TAG)
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

        def functionStart(self):
            return self.getTypedRuleContext(ignoreParser.FunctionStartContext,0)


        def FUNCTION_TAG_END(self):
            return self.getToken(ignoreParser.FUNCTION_TAG_END, 0)

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
        self.enterRule(localctx, 8, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.functionStart()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3229659146) != 0):
                self.state = 83
                self.block()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self.match(ignoreParser.FUNCTION_TAG_END)
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
            self.state = 91
            self.match(ignoreParser.VAR_DECL)
            self.state = 92
            self.match(ignoreParser.FUNCTION_NAME)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 93
                self.match(ignoreParser.VAR_DECL_TYPE)


            self.state = 96
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
            self.state = 98
            self.varDecl()
            self.state = 99
            self.wrapped_expr()
            self.state = 100
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
            self.state = 102
            self.match(ignoreParser.PROPERTY_NAME)
            self.state = 103
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
            self.state = 105
            self.match(ignoreParser.WHILE_TAG)
            self.state = 106
            self.loop_condition()
            self.state = 107
            self.match(ignoreParser.END_TAG)
            self.state = 108
            self.block()
            self.state = 109
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
            self.state = 111
            self.match(ignoreParser.FOR_TAG)
            self.state = 112
            self.loop_init()
            self.state = 113
            self.loop_condition()
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 114
                self.var_assign()


            self.state = 117
            self.match(ignoreParser.END_TAG)
            self.state = 118
            self.block()
            self.state = 119
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
            self.state = 121
            self.match(ignoreParser.CONDITION_EQ)
            self.state = 122
            self.match(ignoreParser.OPEN_CURLY)

            self.state = 123
            self.condition()
            self.state = 124
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
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.state = 126
                self.var()
                pass
            elif token in [24]:
                self.state = 127
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
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
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
            self.state = 134
            self.match(ignoreParser.IF_TAG)
            self.state = 135
            self.match(ignoreParser.CONDITION_EQ)
            self.state = 136
            self.match(ignoreParser.OPEN_CURLY)

            self.state = 137
            self.condition()
            self.state = 138
            self.match(ignoreParser.CLOSE_CURLY)
            self.state = 139
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
            self.state = 141
            self.if_()
            self.state = 142
            self.block()
            self.state = 143
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
            self.state = 145
            self.match(ignoreParser.ELIF_TAG)
            self.state = 146
            self.match(ignoreParser.CONDITION_EQ)
            self.state = 147
            self.match(ignoreParser.OPEN_CURLY)

            self.state = 148
            self.condition()
            self.state = 149
            self.match(ignoreParser.CLOSE_CURLY)
            self.state = 150
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
            self.state = 152
            self.elif_()
            self.state = 153
            self.block()
            self.state = 154
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
            self.state = 156
            self.match(ignoreParser.ELSE)
            self.state = 157
            self.block()
            self.state = 158
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
            self.state = 160
            self.if_statement()
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 161
                self.elif_statement()
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 167
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
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 170
                self.function()
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 176
            self.match(ignoreParser.OPEN_PROGRAM)
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3229659146) != 0):
                self.state = 179
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 177
                    self.block()
                    pass

                elif la_ == 2:
                    self.state = 178
                    self.var()
                    pass


                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 184
            self.match(ignoreParser.CLOSE_PROGRAM)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 185
                self.function()
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 191
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
            self.state = 193
            self.match(ignoreParser.PROPERTY_NAME)
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.state = 194
                self.wrapped_expr()
                pass
            elif token in [24]:
                self.state = 195
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
            self.state = 198
            self.match(ignoreParser.CLOSE_TAG)
            self.state = 199
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
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.match(ignoreParser.OPEN_TAG)
                self.state = 202
                self.match(ignoreParser.END_TAG)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.match(ignoreParser.OPEN_TAG)
                self.state = 205 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 204
                    self.property_()
                    self.state = 207 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==30):
                        break

                self.state = 209
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
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.startTag()
                self.state = 214
                self.wrapped_expr()
                self.state = 215
                self.endTag()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.wrapped_expr()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 218
                self.function()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 219
                self.control_statement()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 220
                self.var()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 6)
                self.state = 221
                self.var_assign()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 7)
                self.state = 222
                self.for_loop()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 8)
                self.state = 223
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
            self.state = 227 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 226
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 229 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 232
                self.match(ignoreParser.OPEN_PAREN)
                self.state = 233
                self.expr(0)
                self.state = 234
                self.match(ignoreParser.CLOSE_PAREN)
                pass

            elif la_ == 2:
                self.state = 236
                self.literal()
                pass

            elif la_ == 3:
                self.state = 237
                self.functionCall()
                pass

            elif la_ == 4:
                self.state = 238
                self.match(ignoreParser.NOT)
                self.state = 239
                self.expr(6)
                pass

            elif la_ == 5:
                self.state = 240
                self.match(ignoreParser.NAME)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 257
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 255
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 243
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 244
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 224300372066304) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 245
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 246
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 247
                        _la = self._input.LA(1)
                        if not(_la==44 or _la==45):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 248
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 249
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")

                        self.state = 250
                        self.match(ignoreParser.OPERATOR_COMPARE)
                        self.state = 251
                        self.expr(4)
                        pass

                    elif la_ == 4:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 252
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                        self.state = 253
                        self.match(ignoreParser.OPERATOR_LOGIC)
                        self.state = 254
                        self.expr(3)
                        pass

             
                self.state = 259
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
            self.state = 260
            self.match(ignoreParser.OPEN_CURLY)
            self.state = 261
            self.expr(0)
            self.state = 262
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
         




