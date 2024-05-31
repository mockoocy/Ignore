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
        4,1,56,270,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,1,0,1,1,1,1,1,2,4,2,60,8,2,11,2,12,2,61,1,3,1,3,1,3,3,3,67,8,
        3,1,3,1,3,1,4,1,4,1,4,5,4,74,8,4,10,4,12,4,77,9,4,1,4,3,4,80,8,4,
        1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,3,6,93,8,6,1,6,1,6,1,
        6,1,6,3,6,99,8,6,1,6,3,6,102,8,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,9,
        1,9,1,9,1,9,1,9,1,9,1,10,1,10,3,10,119,8,10,1,10,1,10,3,10,123,8,
        10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,3,12,136,
        8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,
        1,17,1,18,1,18,5,18,166,8,18,10,18,12,18,169,9,18,1,18,3,18,172,
        8,18,1,19,5,19,175,8,19,10,19,12,19,178,9,19,1,19,1,19,1,19,5,19,
        183,8,19,10,19,12,19,186,9,19,1,19,1,19,5,19,190,8,19,10,19,12,19,
        193,9,19,1,19,1,19,1,20,1,20,1,20,3,20,200,8,20,1,21,1,21,1,21,1,
        22,1,22,1,22,1,22,4,22,209,8,22,11,22,12,22,210,1,22,1,22,3,22,215,
        8,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,
        228,8,23,1,24,1,24,1,24,4,24,233,8,24,11,24,12,24,234,1,25,1,25,
        1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,247,8,25,1,25,1,25,
        1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,5,25,261,8,25,
        10,25,12,25,264,9,25,1,26,1,26,1,26,1,26,1,26,0,1,50,27,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,
        52,0,4,1,0,42,43,3,0,36,36,38,38,42,43,2,0,45,46,49,50,1,0,47,48,
        279,0,54,1,0,0,0,2,56,1,0,0,0,4,59,1,0,0,0,6,63,1,0,0,0,8,70,1,0,
        0,0,10,85,1,0,0,0,12,101,1,0,0,0,14,103,1,0,0,0,16,107,1,0,0,0,18,
        110,1,0,0,0,20,116,1,0,0,0,22,128,1,0,0,0,24,135,1,0,0,0,26,137,
        1,0,0,0,28,144,1,0,0,0,30,148,1,0,0,0,32,155,1,0,0,0,34,159,1,0,
        0,0,36,163,1,0,0,0,38,176,1,0,0,0,40,196,1,0,0,0,42,201,1,0,0,0,
        44,214,1,0,0,0,46,227,1,0,0,0,48,232,1,0,0,0,50,246,1,0,0,0,52,265,
        1,0,0,0,54,55,7,0,0,0,55,1,1,0,0,0,56,57,7,1,0,0,57,3,1,0,0,0,58,
        60,3,50,25,0,59,58,1,0,0,0,60,61,1,0,0,0,61,59,1,0,0,0,61,62,1,0,
        0,0,62,5,1,0,0,0,63,64,5,37,0,0,64,66,5,40,0,0,65,67,3,4,2,0,66,
        65,1,0,0,0,66,67,1,0,0,0,67,68,1,0,0,0,68,69,5,41,0,0,69,7,1,0,0,
        0,70,71,5,16,0,0,71,75,5,20,0,0,72,74,5,22,0,0,73,72,1,0,0,0,74,
        77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,
        0,78,80,5,21,0,0,79,78,1,0,0,0,79,80,1,0,0,0,80,81,1,0,0,0,81,82,
        5,32,0,0,82,83,3,48,24,0,83,84,5,17,0,0,84,9,1,0,0,0,85,86,5,18,
        0,0,86,87,3,52,26,0,87,88,5,19,0,0,88,11,1,0,0,0,89,90,5,10,0,0,
        90,92,5,20,0,0,91,93,5,9,0,0,92,91,1,0,0,0,92,93,1,0,0,0,93,94,1,
        0,0,0,94,102,5,32,0,0,95,96,5,10,0,0,96,98,5,20,0,0,97,99,5,9,0,
        0,98,97,1,0,0,0,98,99,1,0,0,0,99,100,1,0,0,0,100,102,5,32,0,0,101,
        89,1,0,0,0,101,95,1,0,0,0,102,13,1,0,0,0,103,104,3,12,6,0,104,105,
        3,52,26,0,105,106,5,8,0,0,106,15,1,0,0,0,107,108,5,33,0,0,108,109,
        3,52,26,0,109,17,1,0,0,0,110,111,5,11,0,0,111,112,3,22,11,0,112,
        113,5,32,0,0,113,114,3,48,24,0,114,115,5,12,0,0,115,19,1,0,0,0,116,
        118,5,14,0,0,117,119,3,14,7,0,118,117,1,0,0,0,118,119,1,0,0,0,119,
        120,1,0,0,0,120,122,3,22,11,0,121,123,3,16,8,0,122,121,1,0,0,0,122,
        123,1,0,0,0,123,124,1,0,0,0,124,125,5,32,0,0,125,126,3,48,24,0,126,
        127,5,15,0,0,127,21,1,0,0,0,128,129,5,31,0,0,129,130,5,34,0,0,130,
        131,3,24,12,0,131,132,5,55,0,0,132,23,1,0,0,0,133,136,3,50,25,0,
        134,136,5,36,0,0,135,133,1,0,0,0,135,134,1,0,0,0,136,25,1,0,0,0,
        137,138,5,1,0,0,138,139,5,31,0,0,139,140,5,34,0,0,140,141,3,24,12,
        0,141,142,5,55,0,0,142,143,5,32,0,0,143,27,1,0,0,0,144,145,3,26,
        13,0,145,146,3,48,24,0,146,147,5,2,0,0,147,29,1,0,0,0,148,149,5,
        4,0,0,149,150,5,31,0,0,150,151,5,34,0,0,151,152,3,24,12,0,152,153,
        5,55,0,0,153,154,5,32,0,0,154,31,1,0,0,0,155,156,3,30,15,0,156,157,
        3,48,24,0,157,158,5,3,0,0,158,33,1,0,0,0,159,160,5,5,0,0,160,161,
        3,48,24,0,161,162,5,6,0,0,162,35,1,0,0,0,163,167,3,28,14,0,164,166,
        3,32,16,0,165,164,1,0,0,0,166,169,1,0,0,0,167,165,1,0,0,0,167,168,
        1,0,0,0,168,171,1,0,0,0,169,167,1,0,0,0,170,172,3,34,17,0,171,170,
        1,0,0,0,171,172,1,0,0,0,172,37,1,0,0,0,173,175,3,8,4,0,174,173,1,
        0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,179,1,
        0,0,0,178,176,1,0,0,0,179,184,5,26,0,0,180,183,3,48,24,0,181,183,
        3,14,7,0,182,180,1,0,0,0,182,181,1,0,0,0,183,186,1,0,0,0,184,182,
        1,0,0,0,184,185,1,0,0,0,185,187,1,0,0,0,186,184,1,0,0,0,187,191,
        5,27,0,0,188,190,3,8,4,0,189,188,1,0,0,0,190,193,1,0,0,0,191,189,
        1,0,0,0,191,192,1,0,0,0,192,194,1,0,0,0,193,191,1,0,0,0,194,195,
        5,0,0,1,195,39,1,0,0,0,196,199,5,33,0,0,197,200,3,52,26,0,198,200,
        5,30,0,0,199,197,1,0,0,0,199,198,1,0,0,0,200,41,1,0,0,0,201,202,
        5,28,0,0,202,203,5,32,0,0,203,43,1,0,0,0,204,205,5,29,0,0,205,215,
        5,32,0,0,206,208,5,29,0,0,207,209,3,40,20,0,208,207,1,0,0,0,209,
        210,1,0,0,0,210,208,1,0,0,0,210,211,1,0,0,0,211,212,1,0,0,0,212,
        213,5,32,0,0,213,215,1,0,0,0,214,204,1,0,0,0,214,206,1,0,0,0,215,
        45,1,0,0,0,216,217,3,44,22,0,217,218,3,52,26,0,218,219,3,42,21,0,
        219,228,1,0,0,0,220,228,3,52,26,0,221,228,3,8,4,0,222,228,3,36,18,
        0,223,228,3,14,7,0,224,228,3,16,8,0,225,228,3,20,10,0,226,228,3,
        18,9,0,227,216,1,0,0,0,227,220,1,0,0,0,227,221,1,0,0,0,227,222,1,
        0,0,0,227,223,1,0,0,0,227,224,1,0,0,0,227,225,1,0,0,0,227,226,1,
        0,0,0,228,47,1,0,0,0,229,233,3,46,23,0,230,233,3,10,5,0,231,233,
        5,13,0,0,232,229,1,0,0,0,232,230,1,0,0,0,232,231,1,0,0,0,233,234,
        1,0,0,0,234,232,1,0,0,0,234,235,1,0,0,0,235,49,1,0,0,0,236,237,6,
        25,-1,0,237,238,5,40,0,0,238,239,3,50,25,0,239,240,5,41,0,0,240,
        247,1,0,0,0,241,247,3,2,1,0,242,247,3,6,3,0,243,244,5,51,0,0,244,
        247,3,50,25,6,245,247,5,37,0,0,246,236,1,0,0,0,246,241,1,0,0,0,246,
        242,1,0,0,0,246,243,1,0,0,0,246,245,1,0,0,0,247,262,1,0,0,0,248,
        249,10,5,0,0,249,250,7,2,0,0,250,261,3,50,25,6,251,252,10,4,0,0,
        252,253,7,3,0,0,253,261,3,50,25,5,254,255,10,3,0,0,255,256,5,52,
        0,0,256,261,3,50,25,4,257,258,10,2,0,0,258,259,5,53,0,0,259,261,
        3,50,25,3,260,248,1,0,0,0,260,251,1,0,0,0,260,254,1,0,0,0,260,257,
        1,0,0,0,261,264,1,0,0,0,262,260,1,0,0,0,262,263,1,0,0,0,263,51,1,
        0,0,0,264,262,1,0,0,0,265,266,5,34,0,0,266,267,3,50,25,0,267,268,
        5,55,0,0,268,53,1,0,0,0,25,61,66,75,79,92,98,101,118,122,135,167,
        171,176,182,184,191,199,210,214,227,232,234,246,260,262
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
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "':'", "'('", "')'", "<INVALID>", "<INVALID>", "'='", 
                     "'*'", "'/'", "'+'", "'-'", "'%'", "'//'", "'!'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'}'" ]

    symbolicNames = [ "<INVALID>", "IF_TAG", "IF_END", "ELIF_END", "ELIF_TAG", 
                      "ELSE", "ELSE_END", "VAR_DECL_START", "VAR_DECL_END", 
                      "VAR_DECL_TYPE", "VAR_DECL", "WHILE_TAG", "WHILE_END", 
                      "BREAK", "FOR_TAG", "FOR_END", "FUNCTION_TAG_OPEN", 
                      "FUNCTION_TAG_END", "RETURN_TAG", "RETURN_END", "FUNCTION_NAME", 
                      "FUNCTION_RET_TYPE", "FUNCTION_PARAM", "COMMENT", 
                      "LINE_COMMENT", "WS", "OPEN_PROGRAM", "CLOSE_PROGRAM", 
                      "CLOSE_TAG", "OPEN_TAG", "TAG_REFERENCE", "CONDITION_EQ", 
                      "END_TAG", "PROPERTY_NAME", "OPEN_CURLY", "EXPR_WS", 
                      "LITERAL_BOOL", "NAME", "LITERAL_STRING", "COLON", 
                      "OPEN_PAREN", "CLOSE_PAREN", "LITERAL_INT", "LITERAL_FLOAT", 
                      "EQUALS", "MUL", "DIV", "ADD", "SUB", "MOD", "INT_DIV", 
                      "NOT", "OPERATOR_COMPARE", "OPERATOR_LOGIC", "EXPR_COMMENT", 
                      "CLOSE_CURLY", "EXPR_LINE_COMMENT" ]

    RULE_literalNumeric = 0
    RULE_literal = 1
    RULE_argumentList = 2
    RULE_functionCall = 3
    RULE_function = 4
    RULE_returnStmt = 5
    RULE_varDecl = 6
    RULE_var = 7
    RULE_var_assign = 8
    RULE_while_loop = 9
    RULE_for_loop = 10
    RULE_loop_condition = 11
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

    ruleNames =  [ "literalNumeric", "literal", "argumentList", "functionCall", 
                   "function", "returnStmt", "varDecl", "var", "var_assign", 
                   "while_loop", "for_loop", "loop_condition", "condition", 
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
    EXPR_WS=35
    LITERAL_BOOL=36
    NAME=37
    LITERAL_STRING=38
    COLON=39
    OPEN_PAREN=40
    CLOSE_PAREN=41
    LITERAL_INT=42
    LITERAL_FLOAT=43
    EQUALS=44
    MUL=45
    DIV=46
    ADD=47
    SUB=48
    MOD=49
    INT_DIV=50
    NOT=51
    OPERATOR_COMPARE=52
    OPERATOR_LOGIC=53
    EXPR_COMMENT=54
    CLOSE_CURLY=55
    EXPR_LINE_COMMENT=56

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
            if not(_la==42 or _la==43):
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
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 13537736916992) != 0)):
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
        self.enterRule(localctx, 4, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 58
                self.expr(0)
                self.state = 61 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2266574501183488) != 0)):
                    break

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

        def argumentList(self):
            return self.getTypedRuleContext(ignoreParser.ArgumentListContext,0)


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
        self.enterRule(localctx, 6, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(ignoreParser.NAME)
            self.state = 64
            self.match(ignoreParser.OPEN_PAREN)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2266574501183488) != 0):
                self.state = 65
                self.argumentList()


            self.state = 68
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
        self.enterRule(localctx, 8, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(ignoreParser.FUNCTION_TAG_OPEN)
            self.state = 71
            self.match(ignoreParser.FUNCTION_NAME)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 72
                self.match(ignoreParser.FUNCTION_PARAM)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 78
                self.match(ignoreParser.FUNCTION_RET_TYPE)


            self.state = 81
            self.match(ignoreParser.END_TAG)
            self.state = 82
            self.block()
            self.state = 83
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
        self.enterRule(localctx, 10, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(ignoreParser.RETURN_TAG)
            self.state = 86
            self.wrapped_expr()
            self.state = 87
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
        self.enterRule(localctx, 12, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.match(ignoreParser.VAR_DECL)
                self.state = 90
                self.match(ignoreParser.FUNCTION_NAME)
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 91
                    self.match(ignoreParser.VAR_DECL_TYPE)


                self.state = 94
                self.match(ignoreParser.END_TAG)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.match(ignoreParser.VAR_DECL)
                self.state = 96
                self.match(ignoreParser.FUNCTION_NAME)
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 97
                    self.match(ignoreParser.VAR_DECL_TYPE)


                self.state = 100
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
        self.enterRule(localctx, 14, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.varDecl()
            self.state = 104
            self.wrapped_expr()
            self.state = 105
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
        self.enterRule(localctx, 16, self.RULE_var_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(ignoreParser.PROPERTY_NAME)
            self.state = 108
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
        self.enterRule(localctx, 18, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(ignoreParser.WHILE_TAG)
            self.state = 111
            self.loop_condition()
            self.state = 112
            self.match(ignoreParser.END_TAG)
            self.state = 113
            self.block()
            self.state = 114
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
        self.enterRule(localctx, 20, self.RULE_for_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(ignoreParser.FOR_TAG)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 117
                self.var()


            self.state = 120
            self.loop_condition()
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 121
                self.var_assign()


            self.state = 124
            self.match(ignoreParser.END_TAG)
            self.state = 125
            self.block()
            self.state = 126
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
        self.enterRule(localctx, 22, self.RULE_loop_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(ignoreParser.CONDITION_EQ)
            self.state = 129
            self.match(ignoreParser.OPEN_CURLY)

            self.state = 130
            self.condition()
            self.state = 131
            self.match(ignoreParser.CLOSE_CURLY)
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
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
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
            self.state = 137
            self.match(ignoreParser.IF_TAG)
            self.state = 138
            self.match(ignoreParser.CONDITION_EQ)
            self.state = 139
            self.match(ignoreParser.OPEN_CURLY)

            self.state = 140
            self.condition()
            self.state = 141
            self.match(ignoreParser.CLOSE_CURLY)
            self.state = 142
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
            self.state = 144
            self.if_()
            self.state = 145
            self.block()
            self.state = 146
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
            self.state = 148
            self.match(ignoreParser.ELIF_TAG)
            self.state = 149
            self.match(ignoreParser.CONDITION_EQ)
            self.state = 150
            self.match(ignoreParser.OPEN_CURLY)

            self.state = 151
            self.condition()
            self.state = 152
            self.match(ignoreParser.CLOSE_CURLY)
            self.state = 153
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
            self.state = 155
            self.elif_()
            self.state = 156
            self.block()
            self.state = 157
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
            self.state = 159
            self.match(ignoreParser.ELSE)
            self.state = 160
            self.block()
            self.state = 161
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
            self.state = 163
            self.if_statement()
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 164
                self.elif_statement()
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 170
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
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 173
                self.function()
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 179
            self.match(ignoreParser.OPEN_PROGRAM)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 26307030018) != 0):
                self.state = 182
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 180
                    self.block()
                    pass

                elif la_ == 2:
                    self.state = 181
                    self.var()
                    pass


                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 187
            self.match(ignoreParser.CLOSE_PROGRAM)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 188
                self.function()
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 194
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
            self.state = 196
            self.match(ignoreParser.PROPERTY_NAME)
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.state = 197
                self.wrapped_expr()
                pass
            elif token in [30]:
                self.state = 198
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
            self.state = 201
            self.match(ignoreParser.CLOSE_TAG)
            self.state = 202
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
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.match(ignoreParser.OPEN_TAG)
                self.state = 205
                self.match(ignoreParser.END_TAG)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.match(ignoreParser.OPEN_TAG)
                self.state = 208 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 207
                    self.property_()
                    self.state = 210 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==33):
                        break

                self.state = 212
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
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.startTag()
                self.state = 217
                self.wrapped_expr()
                self.state = 218
                self.endTag()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.wrapped_expr()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
                self.function()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 4)
                self.state = 222
                self.control_statement()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 223
                self.var()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 6)
                self.state = 224
                self.var_assign()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 7)
                self.state = 225
                self.for_loop()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 8)
                self.state = 226
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


        def BREAK(self, i:int=None):
            if i is None:
                return self.getTokens(ignoreParser.BREAK)
            else:
                return self.getToken(ignoreParser.BREAK, i)

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
            self.state = 232 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 232
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 10, 11, 14, 16, 29, 33, 34]:
                        self.state = 229
                        self.statement()
                        pass
                    elif token in [18]:
                        self.state = 230
                        self.returnStmt()
                        pass
                    elif token in [13]:
                        self.state = 231
                        self.match(ignoreParser.BREAK)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 234 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 237
                self.match(ignoreParser.OPEN_PAREN)
                self.state = 238
                self.expr(0)
                self.state = 239
                self.match(ignoreParser.CLOSE_PAREN)
                pass

            elif la_ == 2:
                self.state = 241
                self.literal()
                pass

            elif la_ == 3:
                self.state = 242
                self.functionCall()
                pass

            elif la_ == 4:
                self.state = 243
                self.match(ignoreParser.NOT)
                self.state = 244
                self.expr(6)
                pass

            elif la_ == 5:
                self.state = 245
                self.match(ignoreParser.NAME)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 262
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 260
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 248
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 249
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1794402976530432) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 250
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 251
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 252
                        _la = self._input.LA(1)
                        if not(_la==47 or _la==48):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 253
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 254
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")

                        self.state = 255
                        self.match(ignoreParser.OPERATOR_COMPARE)
                        self.state = 256
                        self.expr(4)
                        pass

                    elif la_ == 4:
                        localctx = ignoreParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 257
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                        self.state = 258
                        self.match(ignoreParser.OPERATOR_LOGIC)
                        self.state = 259
                        self.expr(3)
                        pass

             
                self.state = 264
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
            self.state = 265
            self.match(ignoreParser.OPEN_CURLY)
            self.state = 266
            self.expr(0)
            self.state = 267
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
         




