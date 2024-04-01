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
        4,1,42,208,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        1,0,1,1,1,1,1,2,5,2,46,8,2,10,2,12,2,49,9,2,1,2,1,2,5,2,53,8,2,10,
        2,12,2,56,9,2,1,2,1,2,5,2,60,8,2,10,2,12,2,63,9,2,1,2,1,2,1,3,1,
        3,3,3,69,8,3,1,4,1,4,1,4,3,4,74,8,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,
        4,6,83,8,6,11,6,12,6,84,1,6,1,6,3,6,89,8,6,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,3,7,98,8,7,1,8,1,8,1,8,1,8,3,8,104,8,8,1,8,1,8,1,8,1,8,1,8,
        3,8,111,8,8,1,9,1,9,1,9,5,9,116,8,9,10,9,12,9,119,9,9,1,9,1,9,1,
        9,1,10,1,10,5,10,126,8,10,10,10,12,10,129,9,10,1,10,1,10,1,11,1,
        11,1,11,1,11,1,11,1,11,3,11,139,8,11,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,5,17,169,8,17,10,
        17,12,17,172,9,17,1,17,3,17,175,8,17,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,3,18,185,8,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,5,18,199,8,18,10,18,12,18,202,9,18,1,19,1,
        19,1,19,1,19,1,19,0,1,36,20,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,0,4,1,0,31,32,2,0,26,26,30,32,1,0,34,35,1,0,36,
        37,212,0,40,1,0,0,0,2,42,1,0,0,0,4,47,1,0,0,0,6,68,1,0,0,0,8,70,
        1,0,0,0,10,75,1,0,0,0,12,88,1,0,0,0,14,97,1,0,0,0,16,110,1,0,0,0,
        18,112,1,0,0,0,20,123,1,0,0,0,22,138,1,0,0,0,24,140,1,0,0,0,26,147,
        1,0,0,0,28,151,1,0,0,0,30,158,1,0,0,0,32,162,1,0,0,0,34,166,1,0,
        0,0,36,184,1,0,0,0,38,203,1,0,0,0,40,41,7,0,0,0,41,1,1,0,0,0,42,
        43,7,1,0,0,43,3,1,0,0,0,44,46,3,20,10,0,45,44,1,0,0,0,46,49,1,0,
        0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,47,1,0,0,0,50,54,
        5,12,0,0,51,53,3,14,7,0,52,51,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,
        0,54,55,1,0,0,0,55,57,1,0,0,0,56,54,1,0,0,0,57,61,5,13,0,0,58,60,
        3,20,10,0,59,58,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,
        0,62,64,1,0,0,0,63,61,1,0,0,0,64,65,5,0,0,1,65,5,1,0,0,0,66,69,3,
        14,7,0,67,69,3,38,19,0,68,66,1,0,0,0,68,67,1,0,0,0,69,7,1,0,0,0,
        70,73,5,22,0,0,71,74,3,38,19,0,72,74,5,16,0,0,73,71,1,0,0,0,73,72,
        1,0,0,0,74,9,1,0,0,0,75,76,5,14,0,0,76,77,5,21,0,0,77,11,1,0,0,0,
        78,79,5,15,0,0,79,89,5,21,0,0,80,82,5,15,0,0,81,83,3,8,4,0,82,81,
        1,0,0,0,83,84,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,86,1,0,0,0,
        86,87,5,21,0,0,87,89,1,0,0,0,88,78,1,0,0,0,88,80,1,0,0,0,89,13,1,
        0,0,0,90,91,3,12,6,0,91,92,3,38,19,0,92,93,3,10,5,0,93,98,1,0,0,
        0,94,98,3,38,19,0,95,98,3,20,10,0,96,98,3,34,17,0,97,90,1,0,0,0,
        97,94,1,0,0,0,97,95,1,0,0,0,97,96,1,0,0,0,98,15,1,0,0,0,99,100,5,
        25,0,0,100,103,5,28,0,0,101,104,3,36,18,0,102,104,3,2,1,0,103,101,
        1,0,0,0,103,102,1,0,0,0,104,105,1,0,0,0,105,106,5,29,0,0,106,111,
        1,0,0,0,107,108,5,25,0,0,108,109,5,28,0,0,109,111,5,29,0,0,110,99,
        1,0,0,0,110,107,1,0,0,0,111,17,1,0,0,0,112,113,5,1,0,0,113,117,5,
        17,0,0,114,116,5,19,0,0,115,114,1,0,0,0,116,119,1,0,0,0,117,115,
        1,0,0,0,117,118,1,0,0,0,118,120,1,0,0,0,119,117,1,0,0,0,120,121,
        5,18,0,0,121,122,5,21,0,0,122,19,1,0,0,0,123,127,3,18,9,0,124,126,
        3,14,7,0,125,124,1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,127,128,
        1,0,0,0,128,130,1,0,0,0,129,127,1,0,0,0,130,131,5,2,0,0,131,21,1,
        0,0,0,132,133,3,36,18,0,133,134,5,39,0,0,134,135,3,36,18,0,135,139,
        1,0,0,0,136,139,3,36,18,0,137,139,5,30,0,0,138,132,1,0,0,0,138,136,
        1,0,0,0,138,137,1,0,0,0,139,23,1,0,0,0,140,141,5,3,0,0,141,142,5,
        20,0,0,142,143,5,23,0,0,143,144,3,22,11,0,144,145,5,41,0,0,145,146,
        5,21,0,0,146,25,1,0,0,0,147,148,3,24,12,0,148,149,3,6,3,0,149,150,
        5,4,0,0,150,27,1,0,0,0,151,152,5,6,0,0,152,153,5,20,0,0,153,154,
        5,23,0,0,154,155,3,22,11,0,155,156,5,41,0,0,156,157,5,21,0,0,157,
        29,1,0,0,0,158,159,3,28,14,0,159,160,3,6,3,0,160,161,5,5,0,0,161,
        31,1,0,0,0,162,163,5,7,0,0,163,164,3,6,3,0,164,165,5,8,0,0,165,33,
        1,0,0,0,166,170,3,26,13,0,167,169,3,30,15,0,168,167,1,0,0,0,169,
        172,1,0,0,0,170,168,1,0,0,0,170,171,1,0,0,0,171,174,1,0,0,0,172,
        170,1,0,0,0,173,175,3,32,16,0,174,173,1,0,0,0,174,175,1,0,0,0,175,
        35,1,0,0,0,176,177,6,18,-1,0,177,178,5,28,0,0,178,179,3,36,18,0,
        179,180,5,29,0,0,180,185,1,0,0,0,181,185,3,2,1,0,182,185,3,16,8,
        0,183,185,5,25,0,0,184,176,1,0,0,0,184,181,1,0,0,0,184,182,1,0,0,
        0,184,183,1,0,0,0,185,200,1,0,0,0,186,187,10,5,0,0,187,188,7,2,0,
        0,188,199,3,36,18,6,189,190,10,4,0,0,190,191,7,3,0,0,191,199,3,36,
        18,5,192,193,10,3,0,0,193,194,5,38,0,0,194,199,3,36,18,4,195,196,
        10,2,0,0,196,197,5,39,0,0,197,199,3,36,18,3,198,186,1,0,0,0,198,
        189,1,0,0,0,198,192,1,0,0,0,198,195,1,0,0,0,199,202,1,0,0,0,200,
        198,1,0,0,0,200,201,1,0,0,0,201,37,1,0,0,0,202,200,1,0,0,0,203,204,
        5,23,0,0,204,205,3,36,18,0,205,206,5,41,0,0,206,39,1,0,0,0,18,47,
        54,61,68,73,84,88,97,103,110,117,127,138,170,174,184,198,200
    ]

class ignoreParser ( Parser ):

    grammarFileName = "ignoreParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<function'", "'</function>'", "'<if'", 
                     "'</if>'", "'</elif>'", "'<elif'", "'<else>'", "'</else>'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'<program>'", 
                     "'</program>'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'condition='", 
                     "'>'", "<INVALID>", "'{'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "':'", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'='", "'*'", "'/'", "'+'", "'-'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'}'" ]

    symbolicNames = [ "<INVALID>", "FUNCTION_TAG_OPEN", "FUNCTION_TAG_END", 
                      "IF_TAG", "IF_END", "ELIF_END", "ELIF_TAG", "ELSE", 
                      "ELSE_END", "COMMENT", "LINE_COMMENT", "WS", "OPEN_PROGRAM", 
                      "CLOSE_PROGRAM", "CLOSE_TAG", "OPEN_TAG", "TAG_REFERENCE", 
                      "FUNCTION_NAME", "FUNCTION_RET_TYPE", "FUNCTION_PARAM", 
                      "CONDITION_EQ", "END_TAG", "PROPERTY_NAME", "OPEN_CURLY", 
                      "EXPR_WS", "NAME", "LITERAL_STRING", "COLON", "OPEN_PAREN", 
                      "CLOSE_PAREN", "LITERAL_BOOL", "LITERAL_INT", "LITERAL_FLOAT", 
                      "EQUALS", "MUL", "DIV", "ADD", "SUB", "OPERATOR_COMPARE", 
                      "OPERATOR_LOGIC", "EXPR_COMMENT", "CLOSE_CURLY", "EXPR_LINE_COMMENT" ]

    RULE_literalNumeric = 0
    RULE_literal = 1
    RULE_program = 2
    RULE_statement = 3
    RULE_property = 4
    RULE_endTag = 5
    RULE_startTag = 6
    RULE_block = 7
    RULE_functionCall = 8
    RULE_functionStart = 9
    RULE_function = 10
    RULE_condition = 11
    RULE_if = 12
    RULE_if_statement = 13
    RULE_elif = 14
    RULE_elif_statement = 15
    RULE_else_statement = 16
    RULE_control_statement = 17
    RULE_expr = 18
    RULE_wrapped_expr = 19

    ruleNames =  [ "literalNumeric", "literal", "program", "statement", 
                   "property", "endTag", "startTag", "block", "functionCall", 
                   "functionStart", "function", "condition", "if", "if_statement", 
                   "elif", "elif_statement", "else_statement", "control_statement", 
                   "expr", "wrapped_expr" ]

    EOF = Token.EOF
    FUNCTION_TAG_OPEN=1
    FUNCTION_TAG_END=2
    IF_TAG=3
    IF_END=4
    ELIF_END=5
    ELIF_TAG=6
    ELSE=7
    ELSE_END=8
    COMMENT=9
    LINE_COMMENT=10
    WS=11
    OPEN_PROGRAM=12
    CLOSE_PROGRAM=13
    CLOSE_TAG=14
    OPEN_TAG=15
    TAG_REFERENCE=16
    FUNCTION_NAME=17
    FUNCTION_RET_TYPE=18
    FUNCTION_PARAM=19
    CONDITION_EQ=20
    END_TAG=21
    PROPERTY_NAME=22
    OPEN_CURLY=23
    EXPR_WS=24
    NAME=25
    LITERAL_STRING=26
    COLON=27
    OPEN_PAREN=28
    CLOSE_PAREN=29
    LITERAL_BOOL=30
    LITERAL_INT=31
    LITERAL_FLOAT=32
    EQUALS=33
    MUL=34
    DIV=35
    ADD=36
    SUB=37
    OPERATOR_COMPARE=38
    OPERATOR_LOGIC=39
    EXPR_COMMENT=40
    CLOSE_CURLY=41
    EXPR_LINE_COMMENT=42

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




    def literalNumeric(self):

        localctx = ignoreParser.LiteralNumericContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_literalNumeric)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            _la = self._input.LA(1)
            if not(_la==31 or _la==32):
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




    def literal(self):

        localctx = ignoreParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7583301632) != 0)):
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


        def getRuleIndex(self):
            return ignoreParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ignoreParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 44
                self.function()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(ignoreParser.OPEN_PROGRAM)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8421386) != 0):
                self.state = 51
                self.block()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 57
            self.match(ignoreParser.CLOSE_PROGRAM)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 58
                self.function()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(ignoreParser.EOF)
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

        def block(self):
            return self.getTypedRuleContext(ignoreParser.BlockContext,0)


        def wrapped_expr(self):
            return self.getTypedRuleContext(ignoreParser.Wrapped_exprContext,0)


        def getRuleIndex(self):
            return ignoreParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ignoreParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.wrapped_expr()
                pass


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




    def property_(self):

        localctx = ignoreParser.PropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(ignoreParser.PROPERTY_NAME)
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.state = 71
                self.wrapped_expr()
                pass
            elif token in [16]:
                self.state = 72
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




    def endTag(self):

        localctx = ignoreParser.EndTagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_endTag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(ignoreParser.CLOSE_TAG)
            self.state = 76
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




    def startTag(self):

        localctx = ignoreParser.StartTagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_startTag)
        self._la = 0 # Token type
        try:
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(ignoreParser.OPEN_TAG)
                self.state = 79
                self.match(ignoreParser.END_TAG)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.match(ignoreParser.OPEN_TAG)
                self.state = 82 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 81
                    self.property_()
                    self.state = 84 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==22):
                        break

                self.state = 86
                self.match(ignoreParser.END_TAG)
                pass


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


        def getRuleIndex(self):
            return ignoreParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = ignoreParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_block)
        try:
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.startTag()
                self.state = 91
                self.wrapped_expr()
                self.state = 92
                self.endTag()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.wrapped_expr()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.function()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 96
                self.control_statement()
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




    def functionCall(self):

        localctx = ignoreParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_functionCall)
        try:
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.match(ignoreParser.NAME)
                self.state = 100
                self.match(ignoreParser.OPEN_PAREN)
                self.state = 103
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 101
                    self.expr(0)
                    pass

                elif la_ == 2:
                    self.state = 102
                    self.literal()
                    pass


                self.state = 105
                self.match(ignoreParser.CLOSE_PAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.match(ignoreParser.NAME)
                self.state = 108
                self.match(ignoreParser.OPEN_PAREN)
                self.state = 109
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




    def functionStart(self):

        localctx = ignoreParser.FunctionStartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_functionStart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(ignoreParser.FUNCTION_TAG_OPEN)
            self.state = 113
            self.match(ignoreParser.FUNCTION_NAME)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 114
                self.match(ignoreParser.FUNCTION_PARAM)
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
            self.match(ignoreParser.FUNCTION_RET_TYPE)
            self.state = 121
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




    def function(self):

        localctx = ignoreParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.functionStart()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8421386) != 0):
                self.state = 124
                self.block()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 130
            self.match(ignoreParser.FUNCTION_TAG_END)
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ignoreParser.ExprContext)
            else:
                return self.getTypedRuleContext(ignoreParser.ExprContext,i)


        def OPERATOR_LOGIC(self):
            return self.getToken(ignoreParser.OPERATOR_LOGIC, 0)

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




    def condition(self):

        localctx = ignoreParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_condition)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.expr(0)
                self.state = 133
                self.match(ignoreParser.OPERATOR_LOGIC)
                self.state = 134
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 137
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




    def if_(self):

        localctx = ignoreParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(ignoreParser.IF_TAG)
            self.state = 141
            self.match(ignoreParser.CONDITION_EQ)
            self.state = 142
            self.match(ignoreParser.OPEN_CURLY)

            self.state = 143
            self.condition()
            self.state = 144
            self.match(ignoreParser.CLOSE_CURLY)
            self.state = 145
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


        def statement(self):
            return self.getTypedRuleContext(ignoreParser.StatementContext,0)


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




    def if_statement(self):

        localctx = ignoreParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.if_()
            self.state = 148
            self.statement()
            self.state = 149
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




    def elif_(self):

        localctx = ignoreParser.ElifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_elif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(ignoreParser.ELIF_TAG)
            self.state = 152
            self.match(ignoreParser.CONDITION_EQ)
            self.state = 153
            self.match(ignoreParser.OPEN_CURLY)

            self.state = 154
            self.condition()
            self.state = 155
            self.match(ignoreParser.CLOSE_CURLY)
            self.state = 156
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


        def statement(self):
            return self.getTypedRuleContext(ignoreParser.StatementContext,0)


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




    def elif_statement(self):

        localctx = ignoreParser.Elif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_elif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.elif_()
            self.state = 159
            self.statement()
            self.state = 160
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

        def statement(self):
            return self.getTypedRuleContext(ignoreParser.StatementContext,0)


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




    def else_statement(self):

        localctx = ignoreParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(ignoreParser.ELSE)
            self.state = 163
            self.statement()
            self.state = 164
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




    def control_statement(self):

        localctx = ignoreParser.Control_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_control_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.if_statement()
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 167
                self.elif_statement()
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 173
                self.else_statement()


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


        def NAME(self):
            return self.getToken(ignoreParser.NAME, 0)

        def MUL(self):
            return self.getToken(ignoreParser.MUL, 0)

        def DIV(self):
            return self.getToken(ignoreParser.DIV, 0)

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



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ignoreParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 177
                self.match(ignoreParser.OPEN_PAREN)
                self.state = 178
                self.expr(0)
                self.state = 179
                self.match(ignoreParser.CLOSE_PAREN)
                pass

            elif la_ == 2:
                self.state = 181
                self.literal()
                pass

            elif la_ == 3:
                self.state = 182
                self.functionCall()
                pass

            elif la_ == 4:
                self.state = 183
                self.match(ignoreParser.NAME)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 200
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 198
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 186
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 187
                        _la = self._input.LA(1)
                        if not(_la==34 or _la==35):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 188
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 189
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 190
                        _la = self._input.LA(1)
                        if not(_la==36 or _la==37):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 191
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 192
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")

                        self.state = 193
                        self.match(ignoreParser.OPERATOR_COMPARE)
                        self.state = 194
                        self.expr(4)
                        pass

                    elif la_ == 4:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 195
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                        self.state = 196
                        self.match(ignoreParser.OPERATOR_LOGIC)
                        self.state = 197
                        self.expr(3)
                        pass

             
                self.state = 202
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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




    def wrapped_expr(self):

        localctx = ignoreParser.Wrapped_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_wrapped_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(ignoreParser.OPEN_CURLY)
            self.state = 204
            self.expr(0)
            self.state = 205
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
        self._predicates[18] = self.expr_sempred
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
         




