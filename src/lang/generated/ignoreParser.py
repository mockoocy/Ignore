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
        4,1,49,224,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,3,2,53,8,2,1,2,1,
        2,1,2,1,2,1,2,3,2,60,8,2,1,3,1,3,1,3,5,3,65,8,3,10,3,12,3,68,9,3,
        1,3,1,3,1,3,1,4,1,4,5,4,75,8,4,10,4,12,4,78,9,4,1,4,1,4,1,5,1,5,
        1,5,3,5,85,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,3,7,95,8,7,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,5,13,125,
        8,13,10,13,12,13,128,9,13,1,13,3,13,131,8,13,1,14,5,14,134,8,14,
        10,14,12,14,137,9,14,1,14,1,14,1,14,5,14,142,8,14,10,14,12,14,145,
        9,14,1,14,1,14,5,14,149,8,14,10,14,12,14,152,9,14,1,14,1,14,1,15,
        1,15,1,15,3,15,159,8,15,1,16,1,16,1,16,1,17,1,17,1,17,1,17,4,17,
        168,8,17,11,17,12,17,169,1,17,1,17,3,17,174,8,17,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,3,18,184,8,18,1,19,4,19,187,8,19,11,19,
        12,19,188,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,
        201,8,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,5,20,215,8,20,10,20,12,20,218,9,20,1,21,1,21,1,21,1,21,1,21,
        0,1,40,22,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,0,4,1,0,35,36,3,0,29,29,31,31,35,36,2,0,38,39,42,43,1,0,40,
        41,229,0,44,1,0,0,0,2,46,1,0,0,0,4,59,1,0,0,0,6,61,1,0,0,0,8,72,
        1,0,0,0,10,81,1,0,0,0,12,88,1,0,0,0,14,94,1,0,0,0,16,96,1,0,0,0,
        18,103,1,0,0,0,20,107,1,0,0,0,22,114,1,0,0,0,24,118,1,0,0,0,26,122,
        1,0,0,0,28,135,1,0,0,0,30,155,1,0,0,0,32,160,1,0,0,0,34,173,1,0,
        0,0,36,183,1,0,0,0,38,186,1,0,0,0,40,200,1,0,0,0,42,219,1,0,0,0,
        44,45,7,0,0,0,45,1,1,0,0,0,46,47,7,1,0,0,47,3,1,0,0,0,48,49,5,30,
        0,0,49,52,5,33,0,0,50,53,3,40,20,0,51,53,3,2,1,0,52,50,1,0,0,0,52,
        51,1,0,0,0,53,54,1,0,0,0,54,55,5,34,0,0,55,60,1,0,0,0,56,57,5,30,
        0,0,57,58,5,33,0,0,58,60,5,34,0,0,59,48,1,0,0,0,59,56,1,0,0,0,60,
        5,1,0,0,0,61,62,5,1,0,0,62,66,5,21,0,0,63,65,5,23,0,0,64,63,1,0,
        0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,69,1,0,0,0,68,66,
        1,0,0,0,69,70,5,22,0,0,70,71,5,25,0,0,71,7,1,0,0,0,72,76,3,6,3,0,
        73,75,3,38,19,0,74,73,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,
        1,0,0,0,77,79,1,0,0,0,78,76,1,0,0,0,79,80,5,2,0,0,80,9,1,0,0,0,81,
        82,5,12,0,0,82,84,5,21,0,0,83,85,5,11,0,0,84,83,1,0,0,0,84,85,1,
        0,0,0,85,86,1,0,0,0,86,87,5,25,0,0,87,11,1,0,0,0,88,89,3,10,5,0,
        89,90,3,42,21,0,90,91,5,10,0,0,91,13,1,0,0,0,92,95,3,40,20,0,93,
        95,5,29,0,0,94,92,1,0,0,0,94,93,1,0,0,0,95,15,1,0,0,0,96,97,5,3,
        0,0,97,98,5,24,0,0,98,99,5,27,0,0,99,100,3,14,7,0,100,101,5,48,0,
        0,101,102,5,25,0,0,102,17,1,0,0,0,103,104,3,16,8,0,104,105,3,38,
        19,0,105,106,5,4,0,0,106,19,1,0,0,0,107,108,5,6,0,0,108,109,5,24,
        0,0,109,110,5,27,0,0,110,111,3,14,7,0,111,112,5,48,0,0,112,113,5,
        25,0,0,113,21,1,0,0,0,114,115,3,20,10,0,115,116,3,38,19,0,116,117,
        5,5,0,0,117,23,1,0,0,0,118,119,5,7,0,0,119,120,3,38,19,0,120,121,
        5,8,0,0,121,25,1,0,0,0,122,126,3,18,9,0,123,125,3,22,11,0,124,123,
        1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,130,
        1,0,0,0,128,126,1,0,0,0,129,131,3,24,12,0,130,129,1,0,0,0,130,131,
        1,0,0,0,131,27,1,0,0,0,132,134,3,8,4,0,133,132,1,0,0,0,134,137,1,
        0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,138,1,0,0,0,137,135,1,
        0,0,0,138,143,5,16,0,0,139,142,3,38,19,0,140,142,3,12,6,0,141,139,
        1,0,0,0,141,140,1,0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,144,
        1,0,0,0,144,146,1,0,0,0,145,143,1,0,0,0,146,150,5,17,0,0,147,149,
        3,8,4,0,148,147,1,0,0,0,149,152,1,0,0,0,150,148,1,0,0,0,150,151,
        1,0,0,0,151,153,1,0,0,0,152,150,1,0,0,0,153,154,5,0,0,1,154,29,1,
        0,0,0,155,158,5,26,0,0,156,159,3,42,21,0,157,159,5,20,0,0,158,156,
        1,0,0,0,158,157,1,0,0,0,159,31,1,0,0,0,160,161,5,18,0,0,161,162,
        5,25,0,0,162,33,1,0,0,0,163,164,5,19,0,0,164,174,5,25,0,0,165,167,
        5,19,0,0,166,168,3,30,15,0,167,166,1,0,0,0,168,169,1,0,0,0,169,167,
        1,0,0,0,169,170,1,0,0,0,170,171,1,0,0,0,171,172,5,25,0,0,172,174,
        1,0,0,0,173,163,1,0,0,0,173,165,1,0,0,0,174,35,1,0,0,0,175,176,3,
        34,17,0,176,177,3,42,21,0,177,178,3,32,16,0,178,184,1,0,0,0,179,
        184,3,42,21,0,180,184,3,8,4,0,181,184,3,26,13,0,182,184,3,12,6,0,
        183,175,1,0,0,0,183,179,1,0,0,0,183,180,1,0,0,0,183,181,1,0,0,0,
        183,182,1,0,0,0,184,37,1,0,0,0,185,187,3,36,18,0,186,185,1,0,0,0,
        187,188,1,0,0,0,188,186,1,0,0,0,188,189,1,0,0,0,189,39,1,0,0,0,190,
        191,6,20,-1,0,191,192,5,33,0,0,192,193,3,40,20,0,193,194,5,34,0,
        0,194,201,1,0,0,0,195,201,3,2,1,0,196,201,3,4,2,0,197,198,5,44,0,
        0,198,201,3,40,20,6,199,201,5,30,0,0,200,190,1,0,0,0,200,195,1,0,
        0,0,200,196,1,0,0,0,200,197,1,0,0,0,200,199,1,0,0,0,201,216,1,0,
        0,0,202,203,10,5,0,0,203,204,7,2,0,0,204,215,3,40,20,6,205,206,10,
        4,0,0,206,207,7,3,0,0,207,215,3,40,20,5,208,209,10,3,0,0,209,210,
        5,45,0,0,210,215,3,40,20,4,211,212,10,2,0,0,212,213,5,46,0,0,213,
        215,3,40,20,3,214,202,1,0,0,0,214,205,1,0,0,0,214,208,1,0,0,0,214,
        211,1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,
        41,1,0,0,0,218,216,1,0,0,0,219,220,5,27,0,0,220,221,3,40,20,0,221,
        222,5,48,0,0,222,43,1,0,0,0,20,52,59,66,76,84,94,126,130,135,141,
        143,150,158,169,173,183,188,200,214,216
    ]

class ignoreParser ( Parser ):

    grammarFileName = "ignoreParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<function'", "'</function>'", "'<if'", 
                     "'</if>'", "'</elif>'", "'<elif'", "'<else>'", "'</else>'", 
                     "'<var'", "'</var>'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'<program>'", "'</program>'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'condition='", "'>'", "<INVALID>", 
                     "'{'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "':'", "'('", "')'", "<INVALID>", "<INVALID>", "'='", 
                     "'*'", "'/'", "'+'", "'-'", "'%'", "'//'", "'!'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'}'" ]

    symbolicNames = [ "<INVALID>", "FUNCTION_TAG_OPEN", "FUNCTION_TAG_END", 
                      "IF_TAG", "IF_END", "ELIF_END", "ELIF_TAG", "ELSE", 
                      "ELSE_END", "VAR_DECL_START", "VAR_DECL_END", "VAR_DECL_TYPE", 
                      "VAR_DECL", "COMMENT", "LINE_COMMENT", "WS", "OPEN_PROGRAM", 
                      "CLOSE_PROGRAM", "CLOSE_TAG", "OPEN_TAG", "TAG_REFERENCE", 
                      "FUNCTION_NAME", "FUNCTION_RET_TYPE", "FUNCTION_PARAM", 
                      "CONDITION_EQ", "END_TAG", "PROPERTY_NAME", "OPEN_CURLY", 
                      "EXPR_WS", "LITERAL_BOOL", "NAME", "LITERAL_STRING", 
                      "COLON", "OPEN_PAREN", "CLOSE_PAREN", "LITERAL_INT", 
                      "LITERAL_FLOAT", "EQUALS", "MUL", "DIV", "ADD", "SUB", 
                      "MOD", "INT_DIV", "NOT", "OPERATOR_COMPARE", "OPERATOR_LOGIC", 
                      "EXPR_COMMENT", "CLOSE_CURLY", "EXPR_LINE_COMMENT" ]

    RULE_literalNumeric = 0
    RULE_literal = 1
    RULE_functionCall = 2
    RULE_functionStart = 3
    RULE_function = 4
    RULE_varDecl = 5
    RULE_var = 6
    RULE_condition = 7
    RULE_if = 8
    RULE_if_statement = 9
    RULE_elif = 10
    RULE_elif_statement = 11
    RULE_else_statement = 12
    RULE_control_statement = 13
    RULE_program = 14
    RULE_property = 15
    RULE_endTag = 16
    RULE_startTag = 17
    RULE_statement = 18
    RULE_block = 19
    RULE_expr = 20
    RULE_wrapped_expr = 21

    ruleNames =  [ "literalNumeric", "literal", "functionCall", "functionStart", 
                   "function", "varDecl", "var", "condition", "if", "if_statement", 
                   "elif", "elif_statement", "else_statement", "control_statement", 
                   "program", "property", "endTag", "startTag", "statement", 
                   "block", "expr", "wrapped_expr" ]

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
    COMMENT=13
    LINE_COMMENT=14
    WS=15
    OPEN_PROGRAM=16
    CLOSE_PROGRAM=17
    CLOSE_TAG=18
    OPEN_TAG=19
    TAG_REFERENCE=20
    FUNCTION_NAME=21
    FUNCTION_RET_TYPE=22
    FUNCTION_PARAM=23
    CONDITION_EQ=24
    END_TAG=25
    PROPERTY_NAME=26
    OPEN_CURLY=27
    EXPR_WS=28
    LITERAL_BOOL=29
    NAME=30
    LITERAL_STRING=31
    COLON=32
    OPEN_PAREN=33
    CLOSE_PAREN=34
    LITERAL_INT=35
    LITERAL_FLOAT=36
    EQUALS=37
    MUL=38
    DIV=39
    ADD=40
    SUB=41
    MOD=42
    INT_DIV=43
    NOT=44
    OPERATOR_COMPARE=45
    OPERATOR_LOGIC=46
    EXPR_COMMENT=47
    CLOSE_CURLY=48
    EXPR_LINE_COMMENT=49

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
            self.state = 44
            _la = self._input.LA(1)
            if not(_la==35 or _la==36):
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
            self.state = 46
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 105763569664) != 0)):
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
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.match(ignoreParser.NAME)
                self.state = 49
                self.match(ignoreParser.OPEN_PAREN)
                self.state = 52
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 50
                    self.expr(0)
                    pass

                elif la_ == 2:
                    self.state = 51
                    self.literal()
                    pass


                self.state = 54
                self.match(ignoreParser.CLOSE_PAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.match(ignoreParser.NAME)
                self.state = 57
                self.match(ignoreParser.OPEN_PAREN)
                self.state = 58
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
            self.state = 61
            self.match(ignoreParser.FUNCTION_TAG_OPEN)
            self.state = 62
            self.match(ignoreParser.FUNCTION_NAME)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 63
                self.match(ignoreParser.FUNCTION_PARAM)
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 69
            self.match(ignoreParser.FUNCTION_RET_TYPE)
            self.state = 70
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
            self.state = 72
            self.functionStart()
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134746122) != 0):
                self.state = 73
                self.block()
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
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
            self.state = 81
            self.match(ignoreParser.VAR_DECL)
            self.state = 82
            self.match(ignoreParser.FUNCTION_NAME)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 83
                self.match(ignoreParser.VAR_DECL_TYPE)


            self.state = 86
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
            self.state = 88
            self.varDecl()
            self.state = 89
            self.wrapped_expr()
            self.state = 90
            self.match(ignoreParser.VAR_DECL_END)
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
        self.enterRule(localctx, 14, self.RULE_condition)
        try:
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
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
        self.enterRule(localctx, 16, self.RULE_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(ignoreParser.IF_TAG)
            self.state = 97
            self.match(ignoreParser.CONDITION_EQ)
            self.state = 98
            self.match(ignoreParser.OPEN_CURLY)

            self.state = 99
            self.condition()
            self.state = 100
            self.match(ignoreParser.CLOSE_CURLY)
            self.state = 101
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
        self.enterRule(localctx, 18, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.if_()
            self.state = 104
            self.block()
            self.state = 105
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
        self.enterRule(localctx, 20, self.RULE_elif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(ignoreParser.ELIF_TAG)
            self.state = 108
            self.match(ignoreParser.CONDITION_EQ)
            self.state = 109
            self.match(ignoreParser.OPEN_CURLY)

            self.state = 110
            self.condition()
            self.state = 111
            self.match(ignoreParser.CLOSE_CURLY)
            self.state = 112
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
        self.enterRule(localctx, 22, self.RULE_elif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.elif_()
            self.state = 115
            self.block()
            self.state = 116
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
        self.enterRule(localctx, 24, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(ignoreParser.ELSE)
            self.state = 119
            self.block()
            self.state = 120
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
        self.enterRule(localctx, 26, self.RULE_control_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.if_statement()
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 123
                self.elif_statement()
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 129
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
        self.enterRule(localctx, 28, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 132
                self.function()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 138
            self.match(ignoreParser.OPEN_PROGRAM)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134746122) != 0):
                self.state = 141
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 139
                    self.block()
                    pass

                elif la_ == 2:
                    self.state = 140
                    self.var()
                    pass


                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 146
            self.match(ignoreParser.CLOSE_PROGRAM)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 147
                self.function()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 153
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
        self.enterRule(localctx, 30, self.RULE_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(ignoreParser.PROPERTY_NAME)
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.state = 156
                self.wrapped_expr()
                pass
            elif token in [20]:
                self.state = 157
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
        self.enterRule(localctx, 32, self.RULE_endTag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(ignoreParser.CLOSE_TAG)
            self.state = 161
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
        self.enterRule(localctx, 34, self.RULE_startTag)
        self._la = 0 # Token type
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.match(ignoreParser.OPEN_TAG)
                self.state = 164
                self.match(ignoreParser.END_TAG)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.match(ignoreParser.OPEN_TAG)
                self.state = 167 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 166
                    self.property_()
                    self.state = 169 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==26):
                        break

                self.state = 171
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
        self.enterRule(localctx, 36, self.RULE_statement)
        try:
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.startTag()
                self.state = 176
                self.wrapped_expr()
                self.state = 177
                self.endTag()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.wrapped_expr()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 180
                self.function()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 181
                self.control_statement()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 182
                self.var()
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
        self.enterRule(localctx, 38, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 185
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 188 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 191
                self.match(ignoreParser.OPEN_PAREN)
                self.state = 192
                self.expr(0)
                self.state = 193
                self.match(ignoreParser.CLOSE_PAREN)
                pass

            elif la_ == 2:
                self.state = 195
                self.literal()
                pass

            elif la_ == 3:
                self.state = 196
                self.functionCall()
                pass

            elif la_ == 4:
                self.state = 197
                self.match(ignoreParser.NOT)
                self.state = 198
                self.expr(6)
                pass

            elif la_ == 5:
                self.state = 199
                self.match(ignoreParser.NAME)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 216
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 214
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 202
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 203
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14018773254144) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 204
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 205
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 206
                        _la = self._input.LA(1)
                        if not(_la==40 or _la==41):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 207
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 208
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")

                        self.state = 209
                        self.match(ignoreParser.OPERATOR_COMPARE)
                        self.state = 210
                        self.expr(4)
                        pass

                    elif la_ == 4:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 211
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                        self.state = 212
                        self.match(ignoreParser.OPERATOR_LOGIC)
                        self.state = 213
                        self.expr(3)
                        pass

             
                self.state = 218
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        self.enterRule(localctx, 42, self.RULE_wrapped_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(ignoreParser.OPEN_CURLY)
            self.state = 220
            self.expr(0)
            self.state = 221
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
        self._predicates[20] = self.expr_sempred
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
         




