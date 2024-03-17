// Generated from d://Nauka//Sem4//kompilatory//Ignore//ignoreParser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ignoreParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		COLON=1, OPEN_PAREN=2, CLOSE_PAREN=3, OPEN_CURLY=4, CLOSE_CURLY=5, LITERAL_BOOL=6, 
		LITERAL_INT=7, LITERAL_FLOAT=8, OPEN_TAG=9, CLOSE_TAG=10, END_TAG=11, 
		LITERAL_STRING=12, OPERATOR_ARITHMETIC=13, OPERATOR_COMPARE=14, OPERATOR_LOGIC=15, 
		NAME=16, WS=17, OPEN_PROGRAM=18, CLOSE_PROGRAM=19, NAME_EQ=20, RETURN_TYPE_EQ=21, 
		CONDITION_EQ=22, IF_TAG=23, IF_END=24, ELIF_END=25, ELIF_TAG=26, ELSE=27, 
		ELSE_END=28, EQUALS=29, MUL=30, DIV=31, ADD=32, SUB=33, FUNCTION_TAG_OPEN=34, 
		FUNCTION_TAG_END=35;
	public static final int
		RULE_literalNumeric = 0, RULE_literal = 1, RULE_program = 2, RULE_statement = 3, 
		RULE_property = 4, RULE_endTag = 5, RULE_startTag = 6, RULE_block = 7, 
		RULE_functionCall = 8, RULE_functionParam = 9, RULE_functionName = 10, 
		RULE_functionReturnType = 11, RULE_functionStart = 12, RULE_function = 13, 
		RULE_condition = 14, RULE_if = 15, RULE_if_statement = 16, RULE_elif = 17, 
		RULE_elif_statement = 18, RULE_else_statement = 19, RULE_control_statement = 20, 
		RULE_expr = 21, RULE_string_expr = 22;
	private static String[] makeRuleNames() {
		return new String[] {
			"literalNumeric", "literal", "program", "statement", "property", "endTag", 
			"startTag", "block", "functionCall", "functionParam", "functionName", 
			"functionReturnType", "functionStart", "function", "condition", "if", 
			"if_statement", "elif", "elif_statement", "else_statement", "control_statement", 
			"expr", "string_expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "':'", "'('", "')'", "'{'", "'}'", null, null, null, null, "'</'", 
			"'>'", null, null, null, null, null, null, "'<program>'", "'</program>'", 
			"'name='", "'returnType='", "'condition='", "'<if'", "'</if>'", "'</elif>'", 
			"'<elif'", "'<else>'", "'</else>'", "'='", "'*'", "'/'", "'+'", "'-'", 
			"'<function'", "'</function>'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "COLON", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_CURLY", "CLOSE_CURLY", 
			"LITERAL_BOOL", "LITERAL_INT", "LITERAL_FLOAT", "OPEN_TAG", "CLOSE_TAG", 
			"END_TAG", "LITERAL_STRING", "OPERATOR_ARITHMETIC", "OPERATOR_COMPARE", 
			"OPERATOR_LOGIC", "NAME", "WS", "OPEN_PROGRAM", "CLOSE_PROGRAM", "NAME_EQ", 
			"RETURN_TYPE_EQ", "CONDITION_EQ", "IF_TAG", "IF_END", "ELIF_END", "ELIF_TAG", 
			"ELSE", "ELSE_END", "EQUALS", "MUL", "DIV", "ADD", "SUB", "FUNCTION_TAG_OPEN", 
			"FUNCTION_TAG_END"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "ignoreParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ignoreParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LiteralNumericContext extends ParserRuleContext {
		public TerminalNode LITERAL_INT() { return getToken(ignoreParser.LITERAL_INT, 0); }
		public TerminalNode LITERAL_FLOAT() { return getToken(ignoreParser.LITERAL_FLOAT, 0); }
		public LiteralNumericContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literalNumeric; }
	}

	public final LiteralNumericContext literalNumeric() throws RecognitionException {
		LiteralNumericContext _localctx = new LiteralNumericContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_literalNumeric);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			_la = _input.LA(1);
			if ( !(_la==LITERAL_INT || _la==LITERAL_FLOAT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LiteralContext extends ParserRuleContext {
		public TerminalNode LITERAL_INT() { return getToken(ignoreParser.LITERAL_INT, 0); }
		public TerminalNode LITERAL_FLOAT() { return getToken(ignoreParser.LITERAL_FLOAT, 0); }
		public TerminalNode LITERAL_STRING() { return getToken(ignoreParser.LITERAL_STRING, 0); }
		public TerminalNode LITERAL_BOOL() { return getToken(ignoreParser.LITERAL_BOOL, 0); }
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4544L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode OPEN_PROGRAM() { return getToken(ignoreParser.OPEN_PROGRAM, 0); }
		public TerminalNode CLOSE_PROGRAM() { return getToken(ignoreParser.CLOSE_PROGRAM, 0); }
		public TerminalNode EOF() { return getToken(ignoreParser.EOF, 0); }
		public List<FunctionContext> function() {
			return getRuleContexts(FunctionContext.class);
		}
		public FunctionContext function(int i) {
			return getRuleContext(FunctionContext.class,i);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCTION_TAG_OPEN) {
				{
				{
				setState(50);
				function();
				}
				}
				setState(55);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(56);
			match(OPEN_PROGRAM);
			setState(60);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17188258304L) != 0)) {
				{
				{
				setState(57);
				block();
				}
				}
				setState(62);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(63);
			match(CLOSE_PROGRAM);
			setState(67);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCTION_TAG_OPEN) {
				{
				{
				setState(64);
				function();
				}
				}
				setState(69);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(70);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_statement);
		try {
			setState(74);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_TAG:
			case IF_TAG:
			case FUNCTION_TAG_OPEN:
				enterOuterAlt(_localctx, 1);
				{
				setState(72);
				block();
				}
				break;
			case OPEN_PAREN:
			case LITERAL_BOOL:
			case LITERAL_INT:
			case LITERAL_FLOAT:
			case LITERAL_STRING:
			case NAME:
				enterOuterAlt(_localctx, 2);
				{
				setState(73);
				expr(0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PropertyContext extends ParserRuleContext {
		public List<TerminalNode> NAME() { return getTokens(ignoreParser.NAME); }
		public TerminalNode NAME(int i) {
			return getToken(ignoreParser.NAME, i);
		}
		public TerminalNode EQUALS() { return getToken(ignoreParser.EQUALS, 0); }
		public TerminalNode OPEN_CURLY() { return getToken(ignoreParser.OPEN_CURLY, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode CLOSE_CURLY() { return getToken(ignoreParser.CLOSE_CURLY, 0); }
		public PropertyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_property; }
	}

	public final PropertyContext property() throws RecognitionException {
		PropertyContext _localctx = new PropertyContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_property);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			match(NAME);
			setState(77);
			match(EQUALS);
			setState(83);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_CURLY:
				{
				setState(78);
				match(OPEN_CURLY);
				setState(79);
				expr(0);
				setState(80);
				match(CLOSE_CURLY);
				}
				break;
			case NAME:
				{
				setState(82);
				match(NAME);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EndTagContext extends ParserRuleContext {
		public TerminalNode CLOSE_TAG() { return getToken(ignoreParser.CLOSE_TAG, 0); }
		public TerminalNode NAME() { return getToken(ignoreParser.NAME, 0); }
		public TerminalNode END_TAG() { return getToken(ignoreParser.END_TAG, 0); }
		public EndTagContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_endTag; }
	}

	public final EndTagContext endTag() throws RecognitionException {
		EndTagContext _localctx = new EndTagContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_endTag);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			match(CLOSE_TAG);
			setState(86);
			match(NAME);
			setState(87);
			match(END_TAG);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StartTagContext extends ParserRuleContext {
		public TerminalNode OPEN_TAG() { return getToken(ignoreParser.OPEN_TAG, 0); }
		public TerminalNode END_TAG() { return getToken(ignoreParser.END_TAG, 0); }
		public List<PropertyContext> property() {
			return getRuleContexts(PropertyContext.class);
		}
		public PropertyContext property(int i) {
			return getRuleContext(PropertyContext.class,i);
		}
		public StartTagContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_startTag; }
	}

	public final StartTagContext startTag() throws RecognitionException {
		StartTagContext _localctx = new StartTagContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_startTag);
		int _la;
		try {
			setState(99);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(89);
				match(OPEN_TAG);
				setState(90);
				match(END_TAG);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(91);
				match(OPEN_TAG);
				setState(93); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(92);
					property();
					}
					}
					setState(95); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==NAME );
				setState(97);
				match(END_TAG);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ParserRuleContext {
		public StartTagContext startTag() {
			return getRuleContext(StartTagContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public EndTagContext endTag() {
			return getRuleContext(EndTagContext.class,0);
		}
		public FunctionContext function() {
			return getRuleContext(FunctionContext.class,0);
		}
		public Control_statementContext control_statement() {
			return getRuleContext(Control_statementContext.class,0);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_block);
		try {
			setState(107);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_TAG:
				enterOuterAlt(_localctx, 1);
				{
				setState(101);
				startTag();
				setState(102);
				expr(0);
				setState(103);
				endTag();
				}
				break;
			case FUNCTION_TAG_OPEN:
				enterOuterAlt(_localctx, 2);
				{
				setState(105);
				function();
				}
				break;
			case IF_TAG:
				enterOuterAlt(_localctx, 3);
				{
				setState(106);
				control_statement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallContext extends ParserRuleContext {
		public TerminalNode NAME() { return getToken(ignoreParser.NAME, 0); }
		public TerminalNode OPEN_PAREN() { return getToken(ignoreParser.OPEN_PAREN, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(ignoreParser.CLOSE_PAREN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public FunctionCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCall; }
	}

	public final FunctionCallContext functionCall() throws RecognitionException {
		FunctionCallContext _localctx = new FunctionCallContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_functionCall);
		try {
			setState(120);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(109);
				match(NAME);
				setState(110);
				match(OPEN_PAREN);
				setState(113);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
				case 1:
					{
					setState(111);
					expr(0);
					}
					break;
				case 2:
					{
					setState(112);
					literal();
					}
					break;
				}
				setState(115);
				match(CLOSE_PAREN);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(117);
				match(NAME);
				setState(118);
				match(OPEN_PAREN);
				setState(119);
				match(CLOSE_PAREN);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionParamContext extends ParserRuleContext {
		public List<TerminalNode> NAME() { return getTokens(ignoreParser.NAME); }
		public TerminalNode NAME(int i) {
			return getToken(ignoreParser.NAME, i);
		}
		public TerminalNode COLON() { return getToken(ignoreParser.COLON, 0); }
		public FunctionParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionParam; }
	}

	public final FunctionParamContext functionParam() throws RecognitionException {
		FunctionParamContext _localctx = new FunctionParamContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_functionParam);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(122);
			match(NAME);
			setState(123);
			match(COLON);
			setState(124);
			match(NAME);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionNameContext extends ParserRuleContext {
		public TerminalNode NAME_EQ() { return getToken(ignoreParser.NAME_EQ, 0); }
		public TerminalNode NAME() { return getToken(ignoreParser.NAME, 0); }
		public FunctionNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionName; }
	}

	public final FunctionNameContext functionName() throws RecognitionException {
		FunctionNameContext _localctx = new FunctionNameContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_functionName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(126);
			match(NAME_EQ);
			setState(127);
			match(NAME);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionReturnTypeContext extends ParserRuleContext {
		public TerminalNode RETURN_TYPE_EQ() { return getToken(ignoreParser.RETURN_TYPE_EQ, 0); }
		public TerminalNode NAME() { return getToken(ignoreParser.NAME, 0); }
		public FunctionReturnTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionReturnType; }
	}

	public final FunctionReturnTypeContext functionReturnType() throws RecognitionException {
		FunctionReturnTypeContext _localctx = new FunctionReturnTypeContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_functionReturnType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
			match(RETURN_TYPE_EQ);
			setState(130);
			match(NAME);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionStartContext extends ParserRuleContext {
		public TerminalNode FUNCTION_TAG_OPEN() { return getToken(ignoreParser.FUNCTION_TAG_OPEN, 0); }
		public FunctionNameContext functionName() {
			return getRuleContext(FunctionNameContext.class,0);
		}
		public FunctionReturnTypeContext functionReturnType() {
			return getRuleContext(FunctionReturnTypeContext.class,0);
		}
		public TerminalNode END_TAG() { return getToken(ignoreParser.END_TAG, 0); }
		public List<FunctionParamContext> functionParam() {
			return getRuleContexts(FunctionParamContext.class);
		}
		public FunctionParamContext functionParam(int i) {
			return getRuleContext(FunctionParamContext.class,i);
		}
		public FunctionStartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionStart; }
	}

	public final FunctionStartContext functionStart() throws RecognitionException {
		FunctionStartContext _localctx = new FunctionStartContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_functionStart);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(132);
			match(FUNCTION_TAG_OPEN);
			setState(133);
			functionName();
			setState(137);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NAME) {
				{
				{
				setState(134);
				functionParam();
				}
				}
				setState(139);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(140);
			functionReturnType();
			setState(141);
			match(END_TAG);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionContext extends ParserRuleContext {
		public FunctionStartContext functionStart() {
			return getRuleContext(FunctionStartContext.class,0);
		}
		public TerminalNode FUNCTION_TAG_END() { return getToken(ignoreParser.FUNCTION_TAG_END, 0); }
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_function);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			functionStart();
			setState(147);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17188258304L) != 0)) {
				{
				{
				setState(144);
				block();
				}
				}
				setState(149);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(150);
			match(FUNCTION_TAG_END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode OPERATOR_LOGIC() { return getToken(ignoreParser.OPERATOR_LOGIC, 0); }
		public TerminalNode LITERAL_BOOL() { return getToken(ignoreParser.LITERAL_BOOL, 0); }
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_condition);
		try {
			setState(158);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(152);
				expr(0);
				setState(153);
				match(OPERATOR_LOGIC);
				setState(154);
				expr(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(156);
				expr(0);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(157);
				match(LITERAL_BOOL);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfContext extends ParserRuleContext {
		public TerminalNode IF_TAG() { return getToken(ignoreParser.IF_TAG, 0); }
		public TerminalNode CONDITION_EQ() { return getToken(ignoreParser.CONDITION_EQ, 0); }
		public TerminalNode OPEN_CURLY() { return getToken(ignoreParser.OPEN_CURLY, 0); }
		public TerminalNode CLOSE_CURLY() { return getToken(ignoreParser.CLOSE_CURLY, 0); }
		public TerminalNode END_TAG() { return getToken(ignoreParser.END_TAG, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public IfContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if; }
	}

	public final IfContext if_() throws RecognitionException {
		IfContext _localctx = new IfContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_if);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(160);
			match(IF_TAG);
			setState(161);
			match(CONDITION_EQ);
			setState(162);
			match(OPEN_CURLY);
			{
			setState(163);
			condition();
			}
			setState(164);
			match(CLOSE_CURLY);
			setState(165);
			match(END_TAG);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class If_statementContext extends ParserRuleContext {
		public IfContext if_() {
			return getRuleContext(IfContext.class,0);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public TerminalNode IF_END() { return getToken(ignoreParser.IF_END, 0); }
		public If_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_statement; }
	}

	public final If_statementContext if_statement() throws RecognitionException {
		If_statementContext _localctx = new If_statementContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_if_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(167);
			if_();
			setState(168);
			statement();
			setState(169);
			match(IF_END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ElifContext extends ParserRuleContext {
		public TerminalNode ELIF_TAG() { return getToken(ignoreParser.ELIF_TAG, 0); }
		public TerminalNode CONDITION_EQ() { return getToken(ignoreParser.CONDITION_EQ, 0); }
		public TerminalNode OPEN_CURLY() { return getToken(ignoreParser.OPEN_CURLY, 0); }
		public TerminalNode CLOSE_CURLY() { return getToken(ignoreParser.CLOSE_CURLY, 0); }
		public TerminalNode END_TAG() { return getToken(ignoreParser.END_TAG, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public ElifContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elif; }
	}

	public final ElifContext elif() throws RecognitionException {
		ElifContext _localctx = new ElifContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_elif);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(171);
			match(ELIF_TAG);
			setState(172);
			match(CONDITION_EQ);
			setState(173);
			match(OPEN_CURLY);
			{
			setState(174);
			condition();
			}
			setState(175);
			match(CLOSE_CURLY);
			setState(176);
			match(END_TAG);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Elif_statementContext extends ParserRuleContext {
		public ElifContext elif() {
			return getRuleContext(ElifContext.class,0);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public TerminalNode ELIF_END() { return getToken(ignoreParser.ELIF_END, 0); }
		public Elif_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elif_statement; }
	}

	public final Elif_statementContext elif_statement() throws RecognitionException {
		Elif_statementContext _localctx = new Elif_statementContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_elif_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(178);
			elif();
			setState(179);
			statement();
			setState(180);
			match(ELIF_END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Else_statementContext extends ParserRuleContext {
		public TerminalNode ELSE() { return getToken(ignoreParser.ELSE, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public TerminalNode ELSE_END() { return getToken(ignoreParser.ELSE_END, 0); }
		public Else_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_else_statement; }
	}

	public final Else_statementContext else_statement() throws RecognitionException {
		Else_statementContext _localctx = new Else_statementContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_else_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(182);
			match(ELSE);
			setState(183);
			statement();
			setState(184);
			match(ELSE_END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Control_statementContext extends ParserRuleContext {
		public If_statementContext if_statement() {
			return getRuleContext(If_statementContext.class,0);
		}
		public List<Elif_statementContext> elif_statement() {
			return getRuleContexts(Elif_statementContext.class);
		}
		public Elif_statementContext elif_statement(int i) {
			return getRuleContext(Elif_statementContext.class,i);
		}
		public Else_statementContext else_statement() {
			return getRuleContext(Else_statementContext.class,0);
		}
		public Control_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_control_statement; }
	}

	public final Control_statementContext control_statement() throws RecognitionException {
		Control_statementContext _localctx = new Control_statementContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_control_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(186);
			if_statement();
			setState(190);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ELIF_TAG) {
				{
				{
				setState(187);
				elif_statement();
				}
				}
				setState(192);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(194);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(193);
				else_statement();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public TerminalNode OPEN_PAREN() { return getToken(ignoreParser.OPEN_PAREN, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode CLOSE_PAREN() { return getToken(ignoreParser.CLOSE_PAREN, 0); }
		public TerminalNode NAME() { return getToken(ignoreParser.NAME, 0); }
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public TerminalNode MUL() { return getToken(ignoreParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(ignoreParser.DIV, 0); }
		public TerminalNode ADD() { return getToken(ignoreParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(ignoreParser.SUB, 0); }
		public TerminalNode OPERATOR_ARITHMETIC() { return getToken(ignoreParser.OPERATOR_ARITHMETIC, 0); }
		public TerminalNode OPERATOR_COMPARE() { return getToken(ignoreParser.OPERATOR_COMPARE, 0); }
		public TerminalNode OPERATOR_LOGIC() { return getToken(ignoreParser.OPERATOR_LOGIC, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 42;
		enterRecursionRule(_localctx, 42, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(204);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				{
				setState(197);
				match(OPEN_PAREN);
				setState(198);
				expr(0);
				setState(199);
				match(CLOSE_PAREN);
				}
				break;
			case 2:
				{
				setState(201);
				match(NAME);
				}
				break;
			case 3:
				{
				setState(202);
				literal();
				}
				break;
			case 4:
				{
				setState(203);
				functionCall();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(223);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(221);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(206);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(207);
						_la = _input.LA(1);
						if ( !(_la==MUL || _la==DIV) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(208);
						expr(6);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(209);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(210);
						_la = _input.LA(1);
						if ( !(_la==ADD || _la==SUB) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(211);
						expr(5);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(212);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						{
						setState(213);
						match(OPERATOR_ARITHMETIC);
						}
						setState(214);
						expr(4);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(215);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						{
						setState(216);
						match(OPERATOR_COMPARE);
						}
						setState(217);
						expr(3);
						}
						break;
					case 5:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(218);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						{
						setState(219);
						match(OPERATOR_LOGIC);
						}
						setState(220);
						expr(2);
						}
						break;
					}
					} 
				}
				setState(225);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class String_exprContext extends ParserRuleContext {
		public TerminalNode LITERAL_STRING() { return getToken(ignoreParser.LITERAL_STRING, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public String_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_string_expr; }
	}

	public final String_exprContext string_expr() throws RecognitionException {
		String_exprContext _localctx = new String_exprContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_string_expr);
		try {
			setState(228);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(226);
				match(LITERAL_STRING);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(227);
				expr(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 21:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 5);
		case 1:
			return precpred(_ctx, 4);
		case 2:
			return precpred(_ctx, 3);
		case 3:
			return precpred(_ctx, 2);
		case 4:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001#\u00e7\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0002\u0005\u00024\b\u0002\n\u0002\f\u00027\t\u0002\u0001\u0002"+
		"\u0001\u0002\u0005\u0002;\b\u0002\n\u0002\f\u0002>\t\u0002\u0001\u0002"+
		"\u0001\u0002\u0005\u0002B\b\u0002\n\u0002\f\u0002E\t\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0003\u0003K\b\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0003\u0004T\b\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0004\u0006^\b\u0006"+
		"\u000b\u0006\f\u0006_\u0001\u0006\u0001\u0006\u0003\u0006d\b\u0006\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003"+
		"\u0007l\b\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0003\br\b\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0003\by\b\b\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f"+
		"\u0001\f\u0001\f\u0005\f\u0088\b\f\n\f\f\f\u008b\t\f\u0001\f\u0001\f\u0001"+
		"\f\u0001\r\u0001\r\u0005\r\u0092\b\r\n\r\f\r\u0095\t\r\u0001\r\u0001\r"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0003\u000e\u009f\b\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014"+
		"\u0005\u0014\u00bd\b\u0014\n\u0014\f\u0014\u00c0\t\u0014\u0001\u0014\u0003"+
		"\u0014\u00c3\b\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0003\u0015\u00cd\b\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0005\u0015\u00de\b\u0015\n\u0015\f\u0015"+
		"\u00e1\t\u0015\u0001\u0016\u0001\u0016\u0003\u0016\u00e5\b\u0016\u0001"+
		"\u0016\u0000\u0001*\u0017\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012"+
		"\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,\u0000\u0004\u0001\u0000\u0007"+
		"\b\u0002\u0000\u0006\b\f\f\u0001\u0000\u001e\u001f\u0001\u0000 !\u00e9"+
		"\u0000.\u0001\u0000\u0000\u0000\u00020\u0001\u0000\u0000\u0000\u00045"+
		"\u0001\u0000\u0000\u0000\u0006J\u0001\u0000\u0000\u0000\bL\u0001\u0000"+
		"\u0000\u0000\nU\u0001\u0000\u0000\u0000\fc\u0001\u0000\u0000\u0000\u000e"+
		"k\u0001\u0000\u0000\u0000\u0010x\u0001\u0000\u0000\u0000\u0012z\u0001"+
		"\u0000\u0000\u0000\u0014~\u0001\u0000\u0000\u0000\u0016\u0081\u0001\u0000"+
		"\u0000\u0000\u0018\u0084\u0001\u0000\u0000\u0000\u001a\u008f\u0001\u0000"+
		"\u0000\u0000\u001c\u009e\u0001\u0000\u0000\u0000\u001e\u00a0\u0001\u0000"+
		"\u0000\u0000 \u00a7\u0001\u0000\u0000\u0000\"\u00ab\u0001\u0000\u0000"+
		"\u0000$\u00b2\u0001\u0000\u0000\u0000&\u00b6\u0001\u0000\u0000\u0000("+
		"\u00ba\u0001\u0000\u0000\u0000*\u00cc\u0001\u0000\u0000\u0000,\u00e4\u0001"+
		"\u0000\u0000\u0000./\u0007\u0000\u0000\u0000/\u0001\u0001\u0000\u0000"+
		"\u000001\u0007\u0001\u0000\u00001\u0003\u0001\u0000\u0000\u000024\u0003"+
		"\u001a\r\u000032\u0001\u0000\u0000\u000047\u0001\u0000\u0000\u000053\u0001"+
		"\u0000\u0000\u000056\u0001\u0000\u0000\u000068\u0001\u0000\u0000\u0000"+
		"75\u0001\u0000\u0000\u00008<\u0005\u0012\u0000\u00009;\u0003\u000e\u0007"+
		"\u0000:9\u0001\u0000\u0000\u0000;>\u0001\u0000\u0000\u0000<:\u0001\u0000"+
		"\u0000\u0000<=\u0001\u0000\u0000\u0000=?\u0001\u0000\u0000\u0000><\u0001"+
		"\u0000\u0000\u0000?C\u0005\u0013\u0000\u0000@B\u0003\u001a\r\u0000A@\u0001"+
		"\u0000\u0000\u0000BE\u0001\u0000\u0000\u0000CA\u0001\u0000\u0000\u0000"+
		"CD\u0001\u0000\u0000\u0000DF\u0001\u0000\u0000\u0000EC\u0001\u0000\u0000"+
		"\u0000FG\u0005\u0000\u0000\u0001G\u0005\u0001\u0000\u0000\u0000HK\u0003"+
		"\u000e\u0007\u0000IK\u0003*\u0015\u0000JH\u0001\u0000\u0000\u0000JI\u0001"+
		"\u0000\u0000\u0000K\u0007\u0001\u0000\u0000\u0000LM\u0005\u0010\u0000"+
		"\u0000MS\u0005\u001d\u0000\u0000NO\u0005\u0004\u0000\u0000OP\u0003*\u0015"+
		"\u0000PQ\u0005\u0005\u0000\u0000QT\u0001\u0000\u0000\u0000RT\u0005\u0010"+
		"\u0000\u0000SN\u0001\u0000\u0000\u0000SR\u0001\u0000\u0000\u0000T\t\u0001"+
		"\u0000\u0000\u0000UV\u0005\n\u0000\u0000VW\u0005\u0010\u0000\u0000WX\u0005"+
		"\u000b\u0000\u0000X\u000b\u0001\u0000\u0000\u0000YZ\u0005\t\u0000\u0000"+
		"Zd\u0005\u000b\u0000\u0000[]\u0005\t\u0000\u0000\\^\u0003\b\u0004\u0000"+
		"]\\\u0001\u0000\u0000\u0000^_\u0001\u0000\u0000\u0000_]\u0001\u0000\u0000"+
		"\u0000_`\u0001\u0000\u0000\u0000`a\u0001\u0000\u0000\u0000ab\u0005\u000b"+
		"\u0000\u0000bd\u0001\u0000\u0000\u0000cY\u0001\u0000\u0000\u0000c[\u0001"+
		"\u0000\u0000\u0000d\r\u0001\u0000\u0000\u0000ef\u0003\f\u0006\u0000fg"+
		"\u0003*\u0015\u0000gh\u0003\n\u0005\u0000hl\u0001\u0000\u0000\u0000il"+
		"\u0003\u001a\r\u0000jl\u0003(\u0014\u0000ke\u0001\u0000\u0000\u0000ki"+
		"\u0001\u0000\u0000\u0000kj\u0001\u0000\u0000\u0000l\u000f\u0001\u0000"+
		"\u0000\u0000mn\u0005\u0010\u0000\u0000nq\u0005\u0002\u0000\u0000or\u0003"+
		"*\u0015\u0000pr\u0003\u0002\u0001\u0000qo\u0001\u0000\u0000\u0000qp\u0001"+
		"\u0000\u0000\u0000rs\u0001\u0000\u0000\u0000st\u0005\u0003\u0000\u0000"+
		"ty\u0001\u0000\u0000\u0000uv\u0005\u0010\u0000\u0000vw\u0005\u0002\u0000"+
		"\u0000wy\u0005\u0003\u0000\u0000xm\u0001\u0000\u0000\u0000xu\u0001\u0000"+
		"\u0000\u0000y\u0011\u0001\u0000\u0000\u0000z{\u0005\u0010\u0000\u0000"+
		"{|\u0005\u0001\u0000\u0000|}\u0005\u0010\u0000\u0000}\u0013\u0001\u0000"+
		"\u0000\u0000~\u007f\u0005\u0014\u0000\u0000\u007f\u0080\u0005\u0010\u0000"+
		"\u0000\u0080\u0015\u0001\u0000\u0000\u0000\u0081\u0082\u0005\u0015\u0000"+
		"\u0000\u0082\u0083\u0005\u0010\u0000\u0000\u0083\u0017\u0001\u0000\u0000"+
		"\u0000\u0084\u0085\u0005\"\u0000\u0000\u0085\u0089\u0003\u0014\n\u0000"+
		"\u0086\u0088\u0003\u0012\t\u0000\u0087\u0086\u0001\u0000\u0000\u0000\u0088"+
		"\u008b\u0001\u0000\u0000\u0000\u0089\u0087\u0001\u0000\u0000\u0000\u0089"+
		"\u008a\u0001\u0000\u0000\u0000\u008a\u008c\u0001\u0000\u0000\u0000\u008b"+
		"\u0089\u0001\u0000\u0000\u0000\u008c\u008d\u0003\u0016\u000b\u0000\u008d"+
		"\u008e\u0005\u000b\u0000\u0000\u008e\u0019\u0001\u0000\u0000\u0000\u008f"+
		"\u0093\u0003\u0018\f\u0000\u0090\u0092\u0003\u000e\u0007\u0000\u0091\u0090"+
		"\u0001\u0000\u0000\u0000\u0092\u0095\u0001\u0000\u0000\u0000\u0093\u0091"+
		"\u0001\u0000\u0000\u0000\u0093\u0094\u0001\u0000\u0000\u0000\u0094\u0096"+
		"\u0001\u0000\u0000\u0000\u0095\u0093\u0001\u0000\u0000\u0000\u0096\u0097"+
		"\u0005#\u0000\u0000\u0097\u001b\u0001\u0000\u0000\u0000\u0098\u0099\u0003"+
		"*\u0015\u0000\u0099\u009a\u0005\u000f\u0000\u0000\u009a\u009b\u0003*\u0015"+
		"\u0000\u009b\u009f\u0001\u0000\u0000\u0000\u009c\u009f\u0003*\u0015\u0000"+
		"\u009d\u009f\u0005\u0006\u0000\u0000\u009e\u0098\u0001\u0000\u0000\u0000"+
		"\u009e\u009c\u0001\u0000\u0000\u0000\u009e\u009d\u0001\u0000\u0000\u0000"+
		"\u009f\u001d\u0001\u0000\u0000\u0000\u00a0\u00a1\u0005\u0017\u0000\u0000"+
		"\u00a1\u00a2\u0005\u0016\u0000\u0000\u00a2\u00a3\u0005\u0004\u0000\u0000"+
		"\u00a3\u00a4\u0003\u001c\u000e\u0000\u00a4\u00a5\u0005\u0005\u0000\u0000"+
		"\u00a5\u00a6\u0005\u000b\u0000\u0000\u00a6\u001f\u0001\u0000\u0000\u0000"+
		"\u00a7\u00a8\u0003\u001e\u000f\u0000\u00a8\u00a9\u0003\u0006\u0003\u0000"+
		"\u00a9\u00aa\u0005\u0018\u0000\u0000\u00aa!\u0001\u0000\u0000\u0000\u00ab"+
		"\u00ac\u0005\u001a\u0000\u0000\u00ac\u00ad\u0005\u0016\u0000\u0000\u00ad"+
		"\u00ae\u0005\u0004\u0000\u0000\u00ae\u00af\u0003\u001c\u000e\u0000\u00af"+
		"\u00b0\u0005\u0005\u0000\u0000\u00b0\u00b1\u0005\u000b\u0000\u0000\u00b1"+
		"#\u0001\u0000\u0000\u0000\u00b2\u00b3\u0003\"\u0011\u0000\u00b3\u00b4"+
		"\u0003\u0006\u0003\u0000\u00b4\u00b5\u0005\u0019\u0000\u0000\u00b5%\u0001"+
		"\u0000\u0000\u0000\u00b6\u00b7\u0005\u001b\u0000\u0000\u00b7\u00b8\u0003"+
		"\u0006\u0003\u0000\u00b8\u00b9\u0005\u001c\u0000\u0000\u00b9\'\u0001\u0000"+
		"\u0000\u0000\u00ba\u00be\u0003 \u0010\u0000\u00bb\u00bd\u0003$\u0012\u0000"+
		"\u00bc\u00bb\u0001\u0000\u0000\u0000\u00bd\u00c0\u0001\u0000\u0000\u0000"+
		"\u00be\u00bc\u0001\u0000\u0000\u0000\u00be\u00bf\u0001\u0000\u0000\u0000"+
		"\u00bf\u00c2\u0001\u0000\u0000\u0000\u00c0\u00be\u0001\u0000\u0000\u0000"+
		"\u00c1\u00c3\u0003&\u0013\u0000\u00c2\u00c1\u0001\u0000\u0000\u0000\u00c2"+
		"\u00c3\u0001\u0000\u0000\u0000\u00c3)\u0001\u0000\u0000\u0000\u00c4\u00c5"+
		"\u0006\u0015\uffff\uffff\u0000\u00c5\u00c6\u0005\u0002\u0000\u0000\u00c6"+
		"\u00c7\u0003*\u0015\u0000\u00c7\u00c8\u0005\u0003\u0000\u0000\u00c8\u00cd"+
		"\u0001\u0000\u0000\u0000\u00c9\u00cd\u0005\u0010\u0000\u0000\u00ca\u00cd"+
		"\u0003\u0002\u0001\u0000\u00cb\u00cd\u0003\u0010\b\u0000\u00cc\u00c4\u0001"+
		"\u0000\u0000\u0000\u00cc\u00c9\u0001\u0000\u0000\u0000\u00cc\u00ca\u0001"+
		"\u0000\u0000\u0000\u00cc\u00cb\u0001\u0000\u0000\u0000\u00cd\u00df\u0001"+
		"\u0000\u0000\u0000\u00ce\u00cf\n\u0005\u0000\u0000\u00cf\u00d0\u0007\u0002"+
		"\u0000\u0000\u00d0\u00de\u0003*\u0015\u0006\u00d1\u00d2\n\u0004\u0000"+
		"\u0000\u00d2\u00d3\u0007\u0003\u0000\u0000\u00d3\u00de\u0003*\u0015\u0005"+
		"\u00d4\u00d5\n\u0003\u0000\u0000\u00d5\u00d6\u0005\r\u0000\u0000\u00d6"+
		"\u00de\u0003*\u0015\u0004\u00d7\u00d8\n\u0002\u0000\u0000\u00d8\u00d9"+
		"\u0005\u000e\u0000\u0000\u00d9\u00de\u0003*\u0015\u0003\u00da\u00db\n"+
		"\u0001\u0000\u0000\u00db\u00dc\u0005\u000f\u0000\u0000\u00dc\u00de\u0003"+
		"*\u0015\u0002\u00dd\u00ce\u0001\u0000\u0000\u0000\u00dd\u00d1\u0001\u0000"+
		"\u0000\u0000\u00dd\u00d4\u0001\u0000\u0000\u0000\u00dd\u00d7\u0001\u0000"+
		"\u0000\u0000\u00dd\u00da\u0001\u0000\u0000\u0000\u00de\u00e1\u0001\u0000"+
		"\u0000\u0000\u00df\u00dd\u0001\u0000\u0000\u0000\u00df\u00e0\u0001\u0000"+
		"\u0000\u0000\u00e0+\u0001\u0000\u0000\u0000\u00e1\u00df\u0001\u0000\u0000"+
		"\u0000\u00e2\u00e5\u0005\f\u0000\u0000\u00e3\u00e5\u0003*\u0015\u0000"+
		"\u00e4\u00e2\u0001\u0000\u0000\u0000\u00e4\u00e3\u0001\u0000\u0000\u0000"+
		"\u00e5-\u0001\u0000\u0000\u0000\u00135<CJS_ckqx\u0089\u0093\u009e\u00be"+
		"\u00c2\u00cc\u00dd\u00df\u00e4";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}