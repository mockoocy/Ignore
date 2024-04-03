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
        4,1,45,221,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,1,0,1,1,1,1,1,2,5,2,50,8,2,10,2,12,2,53,9,2,1,
        2,1,2,1,2,5,2,58,8,2,10,2,12,2,61,9,2,1,2,1,2,5,2,65,8,2,10,2,12,
        2,68,9,2,1,2,1,2,1,3,1,3,3,3,74,8,3,1,4,1,4,1,4,3,4,79,8,4,1,5,1,
        5,1,5,1,6,1,6,1,6,1,6,4,6,88,8,6,11,6,12,6,89,1,6,1,6,3,6,94,8,6,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,103,8,7,1,8,1,8,1,8,1,8,3,8,109,
        8,8,1,8,1,8,1,8,1,8,1,8,3,8,116,8,8,1,9,1,9,1,9,5,9,121,8,9,10,9,
        12,9,124,9,9,1,9,1,9,1,9,1,10,1,10,5,10,131,8,10,10,10,12,10,134,
        9,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,
        1,13,1,13,1,13,1,13,3,13,152,8,13,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,17,
        1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,5,19,182,8,19,10,19,
        12,19,185,9,19,1,19,3,19,188,8,19,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,3,20,198,8,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,5,20,212,8,20,10,20,12,20,215,9,20,1,21,1,21,
        1,21,1,21,1,21,0,1,40,22,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,0,4,1,0,34,35,2,0,29,29,33,35,1,0,37,38,1,0,
        39,40,224,0,44,1,0,0,0,2,46,1,0,0,0,4,51,1,0,0,0,6,73,1,0,0,0,8,
        75,1,0,0,0,10,80,1,0,0,0,12,93,1,0,0,0,14,102,1,0,0,0,16,115,1,0,
        0,0,18,117,1,0,0,0,20,128,1,0,0,0,22,137,1,0,0,0,24,141,1,0,0,0,
        26,151,1,0,0,0,28,153,1,0,0,0,30,160,1,0,0,0,32,164,1,0,0,0,34,171,
        1,0,0,0,36,175,1,0,0,0,38,179,1,0,0,0,40,197,1,0,0,0,42,216,1,0,
        0,0,44,45,7,0,0,0,45,1,1,0,0,0,46,47,7,1,0,0,47,3,1,0,0,0,48,50,
        3,20,10,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,
        0,52,54,1,0,0,0,53,51,1,0,0,0,54,59,5,15,0,0,55,58,3,14,7,0,56,58,
        3,24,12,0,57,55,1,0,0,0,57,56,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,
        0,59,60,1,0,0,0,60,62,1,0,0,0,61,59,1,0,0,0,62,66,5,16,0,0,63,65,
        3,20,10,0,64,63,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,
        0,67,69,1,0,0,0,68,66,1,0,0,0,69,70,5,0,0,1,70,5,1,0,0,0,71,74,3,
        14,7,0,72,74,3,42,21,0,73,71,1,0,0,0,73,72,1,0,0,0,74,7,1,0,0,0,
        75,78,5,25,0,0,76,79,3,42,21,0,77,79,5,19,0,0,78,76,1,0,0,0,78,77,
        1,0,0,0,79,9,1,0,0,0,80,81,5,17,0,0,81,82,5,24,0,0,82,11,1,0,0,0,
        83,84,5,18,0,0,84,94,5,24,0,0,85,87,5,18,0,0,86,88,3,8,4,0,87,86,
        1,0,0,0,88,89,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,91,1,0,0,0,
        91,92,5,24,0,0,92,94,1,0,0,0,93,83,1,0,0,0,93,85,1,0,0,0,94,13,1,
        0,0,0,95,96,3,12,6,0,96,97,3,42,21,0,97,98,3,10,5,0,98,103,1,0,0,
        0,99,103,3,42,21,0,100,103,3,20,10,0,101,103,3,38,19,0,102,95,1,
        0,0,0,102,99,1,0,0,0,102,100,1,0,0,0,102,101,1,0,0,0,103,15,1,0,
        0,0,104,105,5,28,0,0,105,108,5,31,0,0,106,109,3,40,20,0,107,109,
        3,2,1,0,108,106,1,0,0,0,108,107,1,0,0,0,109,110,1,0,0,0,110,111,
        5,32,0,0,111,116,1,0,0,0,112,113,5,28,0,0,113,114,5,31,0,0,114,116,
        5,32,0,0,115,104,1,0,0,0,115,112,1,0,0,0,116,17,1,0,0,0,117,118,
        5,1,0,0,118,122,5,20,0,0,119,121,5,22,0,0,120,119,1,0,0,0,121,124,
        1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,125,1,0,0,0,124,122,
        1,0,0,0,125,126,5,21,0,0,126,127,5,24,0,0,127,19,1,0,0,0,128,132,
        3,18,9,0,129,131,3,14,7,0,130,129,1,0,0,0,131,134,1,0,0,0,132,130,
        1,0,0,0,132,133,1,0,0,0,133,135,1,0,0,0,134,132,1,0,0,0,135,136,
        5,2,0,0,136,21,1,0,0,0,137,138,5,11,0,0,138,139,5,20,0,0,139,140,
        5,24,0,0,140,23,1,0,0,0,141,142,3,22,11,0,142,143,3,42,21,0,143,
        144,5,10,0,0,144,25,1,0,0,0,145,146,3,40,20,0,146,147,5,42,0,0,147,
        148,3,40,20,0,148,152,1,0,0,0,149,152,3,40,20,0,150,152,5,33,0,0,
        151,145,1,0,0,0,151,149,1,0,0,0,151,150,1,0,0,0,152,27,1,0,0,0,153,
        154,5,3,0,0,154,155,5,23,0,0,155,156,5,26,0,0,156,157,3,26,13,0,
        157,158,5,44,0,0,158,159,5,24,0,0,159,29,1,0,0,0,160,161,3,28,14,
        0,161,162,3,6,3,0,162,163,5,4,0,0,163,31,1,0,0,0,164,165,5,6,0,0,
        165,166,5,23,0,0,166,167,5,26,0,0,167,168,3,26,13,0,168,169,5,44,
        0,0,169,170,5,24,0,0,170,33,1,0,0,0,171,172,3,32,16,0,172,173,3,
        6,3,0,173,174,5,5,0,0,174,35,1,0,0,0,175,176,5,7,0,0,176,177,3,6,
        3,0,177,178,5,8,0,0,178,37,1,0,0,0,179,183,3,30,15,0,180,182,3,34,
        17,0,181,180,1,0,0,0,182,185,1,0,0,0,183,181,1,0,0,0,183,184,1,0,
        0,0,184,187,1,0,0,0,185,183,1,0,0,0,186,188,3,36,18,0,187,186,1,
        0,0,0,187,188,1,0,0,0,188,39,1,0,0,0,189,190,6,20,-1,0,190,191,5,
        31,0,0,191,192,3,40,20,0,192,193,5,32,0,0,193,198,1,0,0,0,194,198,
        3,2,1,0,195,198,3,16,8,0,196,198,5,28,0,0,197,189,1,0,0,0,197,194,
        1,0,0,0,197,195,1,0,0,0,197,196,1,0,0,0,198,213,1,0,0,0,199,200,
        10,5,0,0,200,201,7,2,0,0,201,212,3,40,20,6,202,203,10,4,0,0,203,
        204,7,3,0,0,204,212,3,40,20,5,205,206,10,3,0,0,206,207,5,41,0,0,
        207,212,3,40,20,4,208,209,10,2,0,0,209,210,5,42,0,0,210,212,3,40,
        20,3,211,199,1,0,0,0,211,202,1,0,0,0,211,205,1,0,0,0,211,208,1,0,
        0,0,212,215,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,41,1,0,0,
        0,215,213,1,0,0,0,216,217,5,26,0,0,217,218,3,40,20,0,218,219,5,44,
        0,0,219,43,1,0,0,0,19,51,57,59,66,73,78,89,93,102,108,115,122,132,
        151,183,187,197,211,213
    ]

class ignoreParser ( Parser ):

    grammarFileName = "ignoreParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<function'", "'</function>'", "'<if'", 
                     "'</if>'", "'</elif>'", "'<elif'", "'<else>'", "'</else>'", 
                     "'<var'", "'</var>'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'<program>'", "'</program>'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'condition='", "'>'", "<INVALID>", "'{'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "':'", "'('", 
                     "')'", "<INVALID>", "<INVALID>", "<INVALID>", "'='", 
                     "'*'", "'/'", "'+'", "'-'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'}'" ]

    symbolicNames = [ "<INVALID>", "FUNCTION_TAG_OPEN", "FUNCTION_TAG_END", 
                      "IF_TAG", "IF_END", "ELIF_END", "ELIF_TAG", "ELSE", 
                      "ELSE_END", "VAR_DECL_START", "VAR_DECL_END", "VAR_DECL", 
                      "COMMENT", "LINE_COMMENT", "WS", "OPEN_PROGRAM", "CLOSE_PROGRAM", 
                      "CLOSE_TAG", "OPEN_TAG", "TAG_REFERENCE", "FUNCTION_NAME", 
                      "FUNCTION_RET_TYPE", "FUNCTION_PARAM", "CONDITION_EQ", 
                      "END_TAG", "PROPERTY_NAME", "OPEN_CURLY", "EXPR_WS", 
                      "NAME", "LITERAL_STRING", "COLON", "OPEN_PAREN", "CLOSE_PAREN", 
                      "LITERAL_BOOL", "LITERAL_INT", "LITERAL_FLOAT", "EQUALS", 
                      "MUL", "DIV", "ADD", "SUB", "OPERATOR_COMPARE", "OPERATOR_LOGIC", 
                      "EXPR_COMMENT", "CLOSE_CURLY", "EXPR_LINE_COMMENT" ]

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
    RULE_varDecl = 11
    RULE_var = 12
    RULE_condition = 13
    RULE_if = 14
    RULE_if_statement = 15
    RULE_elif = 16
    RULE_elif_statement = 17
    RULE_else_statement = 18
    RULE_control_statement = 19
    RULE_expr = 20
    RULE_wrapped_expr = 21

    ruleNames =  [ "literalNumeric", "literal", "program", "statement", 
                   "property", "endTag", "startTag", "block", "functionCall", 
                   "functionStart", "function", "varDecl", "var", "condition", 
                   "if", "if_statement", "elif", "elif_statement", "else_statement", 
                   "control_statement", "expr", "wrapped_expr" ]

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
    VAR_DECL=11
    COMMENT=12
    LINE_COMMENT=13
    WS=14
    OPEN_PROGRAM=15
    CLOSE_PROGRAM=16
    CLOSE_TAG=17
    OPEN_TAG=18
    TAG_REFERENCE=19
    FUNCTION_NAME=20
    FUNCTION_RET_TYPE=21
    FUNCTION_PARAM=22
    CONDITION_EQ=23
    END_TAG=24
    PROPERTY_NAME=25
    OPEN_CURLY=26
    EXPR_WS=27
    NAME=28
    LITERAL_STRING=29
    COLON=30
    OPEN_PAREN=31
    CLOSE_PAREN=32
    LITERAL_BOOL=33
    LITERAL_INT=34
    LITERAL_FLOAT=35
    EQUALS=36
    MUL=37
    DIV=38
    ADD=39
    SUB=40
    OPERATOR_COMPARE=41
    OPERATOR_LOGIC=42
    EXPR_COMMENT=43
    CLOSE_CURLY=44
    EXPR_LINE_COMMENT=45

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
            self.state = 44
            _la = self._input.LA(1)
            if not(_la==34 or _la==35):
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

        def check_type(self):
            print(f"is LITERAL_STRING {self.LITERAL_STRING() is not None}")
            print(f"is LITERAL_INT {self.LITERAL_INT() is not None }")
            print(f"is LITERAL_BOOL{self.LITERAL_BOOL() is not None}")
            print(f"is LITERAL_FLOAT {self.LITERAL_FLOAT() is not None}")
            

        def evaluate(self):
            # self.check_type()

            if self.LITERAL_STRING() is not None:
                raw_string = str(self.LITERAL_STRING())
                print("literal string")
                return raw_string[1:-1] 
            
            elif self.LITERAL_INT() is not None:
                print("literal int")
                return str(self.LITERAL_INT())
            
            elif self.LITERAL_FLOAT() is not None:
                print("literal float")
                return str(self.LITERAL_FLOAT())
            
            # not working!
            # elif self.LITERAL_BOOL() is not None:
            #   print("literal bool")
            #  return str(self.LITERAL_BOOL())
            
            else:
                raise NotImplementedError("Unsupported literal type")
        
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
            self.state = 46
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 60666413056) != 0)):
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




    def program(self):

        localctx = ignoreParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 48
                self.function()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.match(ignoreParser.OPEN_PROGRAM)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67373066) != 0):
                self.state = 57
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 3, 18, 26]:
                    self.state = 55
                    self.block()
                    pass
                elif token in [11]:
                    self.state = 56
                    self.var()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self.match(ignoreParser.CLOSE_PROGRAM)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 63
                self.function()
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 69
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
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
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
            self.state = 75
            self.match(ignoreParser.PROPERTY_NAME)
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.state = 76
                self.wrapped_expr()
                pass
            elif token in [19]:
                self.state = 77
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
            self.state = 80
            self.match(ignoreParser.CLOSE_TAG)
            self.state = 81
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
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.match(ignoreParser.OPEN_TAG)
                self.state = 84
                self.match(ignoreParser.END_TAG)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.match(ignoreParser.OPEN_TAG)
                self.state = 87 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 86
                    self.property_()
                    self.state = 89 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==25):
                        break

                self.state = 91
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
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.startTag()
                self.state = 96
                self.wrapped_expr()
                self.state = 97
                self.endTag()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.wrapped_expr()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 100
                self.function()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 101
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
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.match(ignoreParser.NAME)
                self.state = 105
                self.match(ignoreParser.OPEN_PAREN)
                self.state = 108
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 106
                    self.expr(0)
                    pass

                elif la_ == 2:
                    self.state = 107
                    self.literal()
                    pass


                self.state = 110
                self.match(ignoreParser.CLOSE_PAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.match(ignoreParser.NAME)
                self.state = 113
                self.match(ignoreParser.OPEN_PAREN)
                self.state = 114
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
            self.state = 117
            self.match(ignoreParser.FUNCTION_TAG_OPEN)
            self.state = 118
            self.match(ignoreParser.FUNCTION_NAME)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 119
                self.match(ignoreParser.FUNCTION_PARAM)
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 125
            self.match(ignoreParser.FUNCTION_RET_TYPE)
            self.state = 126
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
            self.state = 128
            self.functionStart()
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67371018) != 0):
                self.state = 129
                self.block()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 135
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

        def getRuleIndex(self):
            return ignoreParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)




    def varDecl(self):

        localctx = ignoreParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(ignoreParser.VAR_DECL)
            self.state = 138
            self.match(ignoreParser.FUNCTION_NAME)
            self.state = 139
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




    def var(self):

        localctx = ignoreParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.varDecl()
            self.state = 142
            self.wrapped_expr()
            self.state = 143
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
        self.enterRule(localctx, 26, self.RULE_condition)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.expr(0)
                self.state = 146
                self.match(ignoreParser.OPERATOR_LOGIC)
                self.state = 147
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
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
        self.enterRule(localctx, 28, self.RULE_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(ignoreParser.IF_TAG)
            self.state = 154
            self.match(ignoreParser.CONDITION_EQ)
            self.state = 155
            self.match(ignoreParser.OPEN_CURLY)

            self.state = 156
            self.condition()
            self.state = 157
            self.match(ignoreParser.CLOSE_CURLY)
            self.state = 158
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
        self.enterRule(localctx, 30, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.if_()
            self.state = 161
            self.statement()
            self.state = 162
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
        self.enterRule(localctx, 32, self.RULE_elif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(ignoreParser.ELIF_TAG)
            self.state = 165
            self.match(ignoreParser.CONDITION_EQ)
            self.state = 166
            self.match(ignoreParser.OPEN_CURLY)

            self.state = 167
            self.condition()
            self.state = 168
            self.match(ignoreParser.CLOSE_CURLY)
            self.state = 169
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
        self.enterRule(localctx, 34, self.RULE_elif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.elif_()
            self.state = 172
            self.statement()
            self.state = 173
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
        self.enterRule(localctx, 36, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(ignoreParser.ELSE)
            self.state = 176
            self.statement()
            self.state = 177
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
        self.enterRule(localctx, 38, self.RULE_control_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.if_statement()
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 180
                self.elif_statement()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 186
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

        def evaluate(self):
                if self.literal() is not None:
                    print("LITERAL!")
                    return self.literal().evaluate()

                elif self.functionCall() is not None:
                    print("function")
                    return self.functionCall().evaluate()

                elif self.ADD() is not None or self.SUB() is not None or self.MUL() is not None or self.DIV() is not None:
                    print("arithmetic")
                    left = self.expr(0).evaluate()
                    right = self.expr(1).evaluate()
                    if self.ADD() is not None:
                        return left + right
                    elif self.SUB() is not None:
                        return left - right
                    elif self.MUL() is not None:
                        return left * right
                    elif self.DIV() is not None:
                        return left / right  # division by zero?!
                    
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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 190
                self.match(ignoreParser.OPEN_PAREN)
                self.state = 191
                self.expr(0)
                self.state = 192
                self.match(ignoreParser.CLOSE_PAREN)
                pass

            elif la_ == 2:
                self.state = 194
                self.literal()
                pass

            elif la_ == 3:
                self.state = 195
                self.functionCall()
                pass

            elif la_ == 4:
                self.state = 196
                self.match(ignoreParser.NAME)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 213
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 211
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 199
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 200
                        _la = self._input.LA(1)
                        if not(_la==37 or _la==38):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 201
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 202
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 203
                        _la = self._input.LA(1)
                        if not(_la==39 or _la==40):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 204
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 205
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")

                        self.state = 206
                        self.match(ignoreParser.OPERATOR_COMPARE)
                        self.state = 207
                        self.expr(4)
                        pass

                    elif la_ == 4:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 208
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                        self.state = 209
                        self.match(ignoreParser.OPERATOR_LOGIC)
                        self.state = 210
                        self.expr(3)
                        pass

             
                self.state = 215
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        self.enterRule(localctx, 42, self.RULE_wrapped_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(ignoreParser.OPEN_CURLY)
            self.state = 217
            self.expr(0)
            self.state = 218
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
         




