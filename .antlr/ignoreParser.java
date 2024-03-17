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
		FUNCTION_TAG_OPEN=1, FUNCTION_TAG_END=2, IF_TAG=3, IF_END=4, ELIF_END=5, 
		ELIF_TAG=6, ELSE=7, ELSE_END=8, COMMENT=9, LINE_COMMENT=10, WS=11, OPEN_PROGRAM=12, 
		CLOSE_PROGRAM=13, CLOSE_TAG=14, OPEN_TAG=15, TAG_REFERENCE=16, FUNCTION_NAME=17, 
		FUNCTION_RET_TYPE=18, FUNCTION_PARAM=19, CONDITION_EQ=20, END_TAG=21, 
		PROPERTY_NAME=22, OPEN_CURLY=23, NAME=24, EXPR_WS=25, LITERAL_STRING=26, 
		COLON=27, OPEN_PAREN=28, CLOSE_PAREN=29, LITERAL_BOOL=30, LITERAL_INT=31, 
		LITERAL_FLOAT=32, EQUALS=33, MUL=34, DIV=35, ADD=36, SUB=37, OPERATOR_COMPARE=38, 
		OPERATOR_LOGIC=39, EXPR_COMMENT=40, CLOSE_CURLY=41, EXPR_LINE_COMMENT=42;
	public static final int
		RULE_literalNumeric = 0, RULE_literal = 1, RULE_program = 2, RULE_statement = 3, 
		RULE_property = 4, RULE_endTag = 5, RULE_startTag = 6, RULE_block = 7, 
		RULE_functionCall = 8, RULE_functionStart = 9, RULE_function = 10, RULE_condition = 11, 
		RULE_if = 12, RULE_if_statement = 13, RULE_elif = 14, RULE_elif_statement = 15, 
		RULE_else_statement = 16, RULE_control_statement = 17, RULE_expr = 18, 
		RULE_wrapped_expr = 19;
	private static String[] makeRuleNames() {
		return new String[] {
			"literalNumeric", "literal", "program", "statement", "property", "endTag", 
			"startTag", "block", "functionCall", "functionStart", "function", "condition", 
			"if", "if_statement", "elif", "elif_statement", "else_statement", "control_statement", 
			"expr", "wrapped_expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'<function'", "'</function>'", "'<if'", "'</if>'", "'</elif>'", 
			"'<elif'", "'<else>'", "'</else>'", null, null, null, "'<program>'", 
			"'</program>'", null, null, null, null, null, null, "'condition='", "'>'", 
			null, "'{'", null, null, null, "':'", "'('", "')'", null, null, null, 
			"'='", "'*'", "'/'", "'+'", "'-'", null, null, null, "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "FUNCTION_TAG_OPEN", "FUNCTION_TAG_END", "IF_TAG", "IF_END", "ELIF_END", 
			"ELIF_TAG", "ELSE", "ELSE_END", "COMMENT", "LINE_COMMENT", "WS", "OPEN_PROGRAM", 
			"CLOSE_PROGRAM", "CLOSE_TAG", "OPEN_TAG", "TAG_REFERENCE", "FUNCTION_NAME", 
			"FUNCTION_RET_TYPE", "FUNCTION_PARAM", "CONDITION_EQ", "END_TAG", "PROPERTY_NAME", 
			"OPEN_CURLY", "NAME", "EXPR_WS", "LITERAL_STRING", "COLON", "OPEN_PAREN", 
			"CLOSE_PAREN", "LITERAL_BOOL", "LITERAL_INT", "LITERAL_FLOAT", "EQUALS", 
			"MUL", "DIV", "ADD", "SUB", "OPERATOR_COMPARE", "OPERATOR_LOGIC", "EXPR_COMMENT", 
			"CLOSE_CURLY", "EXPR_LINE_COMMENT"
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
			setState(40);
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
			setState(42);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 7583301632L) != 0)) ) {
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
			setState(47);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCTION_TAG_OPEN) {
				{
				{
				setState(44);
				function();
				}
				}
				setState(49);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(50);
			match(OPEN_PROGRAM);
			setState(54);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 32778L) != 0)) {
				{
				{
				setState(51);
				block();
				}
				}
				setState(56);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(57);
			match(CLOSE_PROGRAM);
			setState(61);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCTION_TAG_OPEN) {
				{
				{
				setState(58);
				function();
				}
				}
				setState(63);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(64);
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
		public Wrapped_exprContext wrapped_expr() {
			return getRuleContext(Wrapped_exprContext.class,0);
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
			setState(68);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FUNCTION_TAG_OPEN:
			case IF_TAG:
			case OPEN_TAG:
				enterOuterAlt(_localctx, 1);
				{
				setState(66);
				block();
				}
				break;
			case OPEN_CURLY:
				enterOuterAlt(_localctx, 2);
				{
				setState(67);
				wrapped_expr();
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
		public TerminalNode PROPERTY_NAME() { return getToken(ignoreParser.PROPERTY_NAME, 0); }
		public Wrapped_exprContext wrapped_expr() {
			return getRuleContext(Wrapped_exprContext.class,0);
		}
		public TerminalNode TAG_REFERENCE() { return getToken(ignoreParser.TAG_REFERENCE, 0); }
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
			setState(70);
			match(PROPERTY_NAME);
			setState(73);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_CURLY:
				{
				setState(71);
				wrapped_expr();
				}
				break;
			case TAG_REFERENCE:
				{
				setState(72);
				match(TAG_REFERENCE);
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
			setState(75);
			match(CLOSE_TAG);
			setState(76);
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
			setState(88);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(78);
				match(OPEN_TAG);
				setState(79);
				match(END_TAG);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(80);
				match(OPEN_TAG);
				setState(82); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(81);
					property();
					}
					}
					setState(84); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==PROPERTY_NAME );
				setState(86);
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
		public Wrapped_exprContext wrapped_expr() {
			return getRuleContext(Wrapped_exprContext.class,0);
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
			setState(96);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_TAG:
				enterOuterAlt(_localctx, 1);
				{
				setState(90);
				startTag();
				setState(91);
				wrapped_expr();
				setState(92);
				endTag();
				}
				break;
			case FUNCTION_TAG_OPEN:
				enterOuterAlt(_localctx, 2);
				{
				setState(94);
				function();
				}
				break;
			case IF_TAG:
				enterOuterAlt(_localctx, 3);
				{
				setState(95);
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
			setState(109);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(98);
				match(NAME);
				setState(99);
				match(OPEN_PAREN);
				setState(102);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
				case 1:
					{
					setState(100);
					expr(0);
					}
					break;
				case 2:
					{
					setState(101);
					literal();
					}
					break;
				}
				setState(104);
				match(CLOSE_PAREN);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(106);
				match(NAME);
				setState(107);
				match(OPEN_PAREN);
				setState(108);
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
	public static class FunctionStartContext extends ParserRuleContext {
		public TerminalNode FUNCTION_TAG_OPEN() { return getToken(ignoreParser.FUNCTION_TAG_OPEN, 0); }
		public TerminalNode FUNCTION_NAME() { return getToken(ignoreParser.FUNCTION_NAME, 0); }
		public TerminalNode FUNCTION_RET_TYPE() { return getToken(ignoreParser.FUNCTION_RET_TYPE, 0); }
		public TerminalNode END_TAG() { return getToken(ignoreParser.END_TAG, 0); }
		public List<TerminalNode> FUNCTION_PARAM() { return getTokens(ignoreParser.FUNCTION_PARAM); }
		public TerminalNode FUNCTION_PARAM(int i) {
			return getToken(ignoreParser.FUNCTION_PARAM, i);
		}
		public FunctionStartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionStart; }
	}

	public final FunctionStartContext functionStart() throws RecognitionException {
		FunctionStartContext _localctx = new FunctionStartContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_functionStart);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			match(FUNCTION_TAG_OPEN);
			setState(112);
			match(FUNCTION_NAME);
			setState(116);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCTION_PARAM) {
				{
				{
				setState(113);
				match(FUNCTION_PARAM);
				}
				}
				setState(118);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(119);
			match(FUNCTION_RET_TYPE);
			setState(120);
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
		enterRule(_localctx, 20, RULE_function);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(122);
			functionStart();
			setState(126);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 32778L) != 0)) {
				{
				{
				setState(123);
				block();
				}
				}
				setState(128);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(129);
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
		enterRule(_localctx, 22, RULE_condition);
		try {
			setState(137);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(131);
				expr(0);
				setState(132);
				match(OPERATOR_LOGIC);
				setState(133);
				expr(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(135);
				expr(0);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(136);
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
		enterRule(_localctx, 24, RULE_if);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(139);
			match(IF_TAG);
			setState(140);
			match(CONDITION_EQ);
			setState(141);
			match(OPEN_CURLY);
			{
			setState(142);
			condition();
			}
			setState(143);
			match(CLOSE_CURLY);
			setState(144);
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
		enterRule(_localctx, 26, RULE_if_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(146);
			if_();
			setState(147);
			statement();
			setState(148);
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
		enterRule(_localctx, 28, RULE_elif);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(150);
			match(ELIF_TAG);
			setState(151);
			match(CONDITION_EQ);
			setState(152);
			match(OPEN_CURLY);
			{
			setState(153);
			condition();
			}
			setState(154);
			match(CLOSE_CURLY);
			setState(155);
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
		enterRule(_localctx, 30, RULE_elif_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(157);
			elif();
			setState(158);
			statement();
			setState(159);
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
		enterRule(_localctx, 32, RULE_else_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(161);
			match(ELSE);
			setState(162);
			statement();
			setState(163);
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
		enterRule(_localctx, 34, RULE_control_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(165);
			if_statement();
			setState(169);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ELIF_TAG) {
				{
				{
				setState(166);
				elif_statement();
				}
				}
				setState(171);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(173);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(172);
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
		int _startState = 36;
		enterRecursionRule(_localctx, 36, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(183);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				{
				setState(176);
				match(OPEN_PAREN);
				setState(177);
				expr(0);
				setState(178);
				match(CLOSE_PAREN);
				}
				break;
			case 2:
				{
				setState(180);
				match(NAME);
				}
				break;
			case 3:
				{
				setState(181);
				literal();
				}
				break;
			case 4:
				{
				setState(182);
				functionCall();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(199);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(197);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(185);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(186);
						_la = _input.LA(1);
						if ( !(_la==MUL || _la==DIV) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(187);
						expr(5);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(188);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(189);
						_la = _input.LA(1);
						if ( !(_la==ADD || _la==SUB) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(190);
						expr(4);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(191);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						{
						setState(192);
						match(OPERATOR_COMPARE);
						}
						setState(193);
						expr(3);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(194);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						{
						setState(195);
						match(OPERATOR_LOGIC);
						}
						setState(196);
						expr(2);
						}
						break;
					}
					} 
				}
				setState(201);
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
	public static class Wrapped_exprContext extends ParserRuleContext {
		public TerminalNode OPEN_CURLY() { return getToken(ignoreParser.OPEN_CURLY, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode CLOSE_CURLY() { return getToken(ignoreParser.CLOSE_CURLY, 0); }
		public Wrapped_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_wrapped_expr; }
	}

	public final Wrapped_exprContext wrapped_expr() throws RecognitionException {
		Wrapped_exprContext _localctx = new Wrapped_exprContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_wrapped_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(202);
			match(OPEN_CURLY);
			setState(203);
			expr(0);
			setState(204);
			match(CLOSE_CURLY);
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
		case 18:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 4);
		case 1:
			return precpred(_ctx, 3);
		case 2:
			return precpred(_ctx, 2);
		case 3:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001*\u00cf\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0002\u0005\u0002.\b\u0002\n\u0002\f\u00021\t\u0002\u0001\u0002"+
		"\u0001\u0002\u0005\u00025\b\u0002\n\u0002\f\u00028\t\u0002\u0001\u0002"+
		"\u0001\u0002\u0005\u0002<\b\u0002\n\u0002\f\u0002?\t\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0003\u0003E\b\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0003\u0004J\b\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0004\u0006"+
		"S\b\u0006\u000b\u0006\f\u0006T\u0001\u0006\u0001\u0006\u0003\u0006Y\b"+
		"\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0003\u0007a\b\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0003\bg\b"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\bn\b\b\u0001\t\u0001"+
		"\t\u0001\t\u0005\ts\b\t\n\t\f\tv\t\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001"+
		"\n\u0005\n}\b\n\n\n\f\n\u0080\t\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0003\u000b\u008a\b\u000b"+
		"\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001"+
		"\u0011\u0005\u0011\u00a8\b\u0011\n\u0011\f\u0011\u00ab\t\u0011\u0001\u0011"+
		"\u0003\u0011\u00ae\b\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0003\u0012\u00b8\b\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0005\u0012\u00c6\b\u0012\n\u0012\f\u0012\u00c9\t\u0012\u0001\u0013\u0001"+
		"\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0000\u0001$\u0014\u0000\u0002"+
		"\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e"+
		" \"$&\u0000\u0004\u0001\u0000\u001f \u0002\u0000\u001a\u001a\u001e \u0001"+
		"\u0000\"#\u0001\u0000$%\u00d2\u0000(\u0001\u0000\u0000\u0000\u0002*\u0001"+
		"\u0000\u0000\u0000\u0004/\u0001\u0000\u0000\u0000\u0006D\u0001\u0000\u0000"+
		"\u0000\bF\u0001\u0000\u0000\u0000\nK\u0001\u0000\u0000\u0000\fX\u0001"+
		"\u0000\u0000\u0000\u000e`\u0001\u0000\u0000\u0000\u0010m\u0001\u0000\u0000"+
		"\u0000\u0012o\u0001\u0000\u0000\u0000\u0014z\u0001\u0000\u0000\u0000\u0016"+
		"\u0089\u0001\u0000\u0000\u0000\u0018\u008b\u0001\u0000\u0000\u0000\u001a"+
		"\u0092\u0001\u0000\u0000\u0000\u001c\u0096\u0001\u0000\u0000\u0000\u001e"+
		"\u009d\u0001\u0000\u0000\u0000 \u00a1\u0001\u0000\u0000\u0000\"\u00a5"+
		"\u0001\u0000\u0000\u0000$\u00b7\u0001\u0000\u0000\u0000&\u00ca\u0001\u0000"+
		"\u0000\u0000()\u0007\u0000\u0000\u0000)\u0001\u0001\u0000\u0000\u0000"+
		"*+\u0007\u0001\u0000\u0000+\u0003\u0001\u0000\u0000\u0000,.\u0003\u0014"+
		"\n\u0000-,\u0001\u0000\u0000\u0000.1\u0001\u0000\u0000\u0000/-\u0001\u0000"+
		"\u0000\u0000/0\u0001\u0000\u0000\u000002\u0001\u0000\u0000\u00001/\u0001"+
		"\u0000\u0000\u000026\u0005\f\u0000\u000035\u0003\u000e\u0007\u000043\u0001"+
		"\u0000\u0000\u000058\u0001\u0000\u0000\u000064\u0001\u0000\u0000\u0000"+
		"67\u0001\u0000\u0000\u000079\u0001\u0000\u0000\u000086\u0001\u0000\u0000"+
		"\u00009=\u0005\r\u0000\u0000:<\u0003\u0014\n\u0000;:\u0001\u0000\u0000"+
		"\u0000<?\u0001\u0000\u0000\u0000=;\u0001\u0000\u0000\u0000=>\u0001\u0000"+
		"\u0000\u0000>@\u0001\u0000\u0000\u0000?=\u0001\u0000\u0000\u0000@A\u0005"+
		"\u0000\u0000\u0001A\u0005\u0001\u0000\u0000\u0000BE\u0003\u000e\u0007"+
		"\u0000CE\u0003&\u0013\u0000DB\u0001\u0000\u0000\u0000DC\u0001\u0000\u0000"+
		"\u0000E\u0007\u0001\u0000\u0000\u0000FI\u0005\u0016\u0000\u0000GJ\u0003"+
		"&\u0013\u0000HJ\u0005\u0010\u0000\u0000IG\u0001\u0000\u0000\u0000IH\u0001"+
		"\u0000\u0000\u0000J\t\u0001\u0000\u0000\u0000KL\u0005\u000e\u0000\u0000"+
		"LM\u0005\u0015\u0000\u0000M\u000b\u0001\u0000\u0000\u0000NO\u0005\u000f"+
		"\u0000\u0000OY\u0005\u0015\u0000\u0000PR\u0005\u000f\u0000\u0000QS\u0003"+
		"\b\u0004\u0000RQ\u0001\u0000\u0000\u0000ST\u0001\u0000\u0000\u0000TR\u0001"+
		"\u0000\u0000\u0000TU\u0001\u0000\u0000\u0000UV\u0001\u0000\u0000\u0000"+
		"VW\u0005\u0015\u0000\u0000WY\u0001\u0000\u0000\u0000XN\u0001\u0000\u0000"+
		"\u0000XP\u0001\u0000\u0000\u0000Y\r\u0001\u0000\u0000\u0000Z[\u0003\f"+
		"\u0006\u0000[\\\u0003&\u0013\u0000\\]\u0003\n\u0005\u0000]a\u0001\u0000"+
		"\u0000\u0000^a\u0003\u0014\n\u0000_a\u0003\"\u0011\u0000`Z\u0001\u0000"+
		"\u0000\u0000`^\u0001\u0000\u0000\u0000`_\u0001\u0000\u0000\u0000a\u000f"+
		"\u0001\u0000\u0000\u0000bc\u0005\u0018\u0000\u0000cf\u0005\u001c\u0000"+
		"\u0000dg\u0003$\u0012\u0000eg\u0003\u0002\u0001\u0000fd\u0001\u0000\u0000"+
		"\u0000fe\u0001\u0000\u0000\u0000gh\u0001\u0000\u0000\u0000hi\u0005\u001d"+
		"\u0000\u0000in\u0001\u0000\u0000\u0000jk\u0005\u0018\u0000\u0000kl\u0005"+
		"\u001c\u0000\u0000ln\u0005\u001d\u0000\u0000mb\u0001\u0000\u0000\u0000"+
		"mj\u0001\u0000\u0000\u0000n\u0011\u0001\u0000\u0000\u0000op\u0005\u0001"+
		"\u0000\u0000pt\u0005\u0011\u0000\u0000qs\u0005\u0013\u0000\u0000rq\u0001"+
		"\u0000\u0000\u0000sv\u0001\u0000\u0000\u0000tr\u0001\u0000\u0000\u0000"+
		"tu\u0001\u0000\u0000\u0000uw\u0001\u0000\u0000\u0000vt\u0001\u0000\u0000"+
		"\u0000wx\u0005\u0012\u0000\u0000xy\u0005\u0015\u0000\u0000y\u0013\u0001"+
		"\u0000\u0000\u0000z~\u0003\u0012\t\u0000{}\u0003\u000e\u0007\u0000|{\u0001"+
		"\u0000\u0000\u0000}\u0080\u0001\u0000\u0000\u0000~|\u0001\u0000\u0000"+
		"\u0000~\u007f\u0001\u0000\u0000\u0000\u007f\u0081\u0001\u0000\u0000\u0000"+
		"\u0080~\u0001\u0000\u0000\u0000\u0081\u0082\u0005\u0002\u0000\u0000\u0082"+
		"\u0015\u0001\u0000\u0000\u0000\u0083\u0084\u0003$\u0012\u0000\u0084\u0085"+
		"\u0005\'\u0000\u0000\u0085\u0086\u0003$\u0012\u0000\u0086\u008a\u0001"+
		"\u0000\u0000\u0000\u0087\u008a\u0003$\u0012\u0000\u0088\u008a\u0005\u001e"+
		"\u0000\u0000\u0089\u0083\u0001\u0000\u0000\u0000\u0089\u0087\u0001\u0000"+
		"\u0000\u0000\u0089\u0088\u0001\u0000\u0000\u0000\u008a\u0017\u0001\u0000"+
		"\u0000\u0000\u008b\u008c\u0005\u0003\u0000\u0000\u008c\u008d\u0005\u0014"+
		"\u0000\u0000\u008d\u008e\u0005\u0017\u0000\u0000\u008e\u008f\u0003\u0016"+
		"\u000b\u0000\u008f\u0090\u0005)\u0000\u0000\u0090\u0091\u0005\u0015\u0000"+
		"\u0000\u0091\u0019\u0001\u0000\u0000\u0000\u0092\u0093\u0003\u0018\f\u0000"+
		"\u0093\u0094\u0003\u0006\u0003\u0000\u0094\u0095\u0005\u0004\u0000\u0000"+
		"\u0095\u001b\u0001\u0000\u0000\u0000\u0096\u0097\u0005\u0006\u0000\u0000"+
		"\u0097\u0098\u0005\u0014\u0000\u0000\u0098\u0099\u0005\u0017\u0000\u0000"+
		"\u0099\u009a\u0003\u0016\u000b\u0000\u009a\u009b\u0005)\u0000\u0000\u009b"+
		"\u009c\u0005\u0015\u0000\u0000\u009c\u001d\u0001\u0000\u0000\u0000\u009d"+
		"\u009e\u0003\u001c\u000e\u0000\u009e\u009f\u0003\u0006\u0003\u0000\u009f"+
		"\u00a0\u0005\u0005\u0000\u0000\u00a0\u001f\u0001\u0000\u0000\u0000\u00a1"+
		"\u00a2\u0005\u0007\u0000\u0000\u00a2\u00a3\u0003\u0006\u0003\u0000\u00a3"+
		"\u00a4\u0005\b\u0000\u0000\u00a4!\u0001\u0000\u0000\u0000\u00a5\u00a9"+
		"\u0003\u001a\r\u0000\u00a6\u00a8\u0003\u001e\u000f\u0000\u00a7\u00a6\u0001"+
		"\u0000\u0000\u0000\u00a8\u00ab\u0001\u0000\u0000\u0000\u00a9\u00a7\u0001"+
		"\u0000\u0000\u0000\u00a9\u00aa\u0001\u0000\u0000\u0000\u00aa\u00ad\u0001"+
		"\u0000\u0000\u0000\u00ab\u00a9\u0001\u0000\u0000\u0000\u00ac\u00ae\u0003"+
		" \u0010\u0000\u00ad\u00ac\u0001\u0000\u0000\u0000\u00ad\u00ae\u0001\u0000"+
		"\u0000\u0000\u00ae#\u0001\u0000\u0000\u0000\u00af\u00b0\u0006\u0012\uffff"+
		"\uffff\u0000\u00b0\u00b1\u0005\u001c\u0000\u0000\u00b1\u00b2\u0003$\u0012"+
		"\u0000\u00b2\u00b3\u0005\u001d\u0000\u0000\u00b3\u00b8\u0001\u0000\u0000"+
		"\u0000\u00b4\u00b8\u0005\u0018\u0000\u0000\u00b5\u00b8\u0003\u0002\u0001"+
		"\u0000\u00b6\u00b8\u0003\u0010\b\u0000\u00b7\u00af\u0001\u0000\u0000\u0000"+
		"\u00b7\u00b4\u0001\u0000\u0000\u0000\u00b7\u00b5\u0001\u0000\u0000\u0000"+
		"\u00b7\u00b6\u0001\u0000\u0000\u0000\u00b8\u00c7\u0001\u0000\u0000\u0000"+
		"\u00b9\u00ba\n\u0004\u0000\u0000\u00ba\u00bb\u0007\u0002\u0000\u0000\u00bb"+
		"\u00c6\u0003$\u0012\u0005\u00bc\u00bd\n\u0003\u0000\u0000\u00bd\u00be"+
		"\u0007\u0003\u0000\u0000\u00be\u00c6\u0003$\u0012\u0004\u00bf\u00c0\n"+
		"\u0002\u0000\u0000\u00c0\u00c1\u0005&\u0000\u0000\u00c1\u00c6\u0003$\u0012"+
		"\u0003\u00c2\u00c3\n\u0001\u0000\u0000\u00c3\u00c4\u0005\'\u0000\u0000"+
		"\u00c4\u00c6\u0003$\u0012\u0002\u00c5\u00b9\u0001\u0000\u0000\u0000\u00c5"+
		"\u00bc\u0001\u0000\u0000\u0000\u00c5\u00bf\u0001\u0000\u0000\u0000\u00c5"+
		"\u00c2\u0001\u0000\u0000\u0000\u00c6\u00c9\u0001\u0000\u0000\u0000\u00c7"+
		"\u00c5\u0001\u0000\u0000\u0000\u00c7\u00c8\u0001\u0000\u0000\u0000\u00c8"+
		"%\u0001\u0000\u0000\u0000\u00c9\u00c7\u0001\u0000\u0000\u0000\u00ca\u00cb"+
		"\u0005\u0017\u0000\u0000\u00cb\u00cc\u0003$\u0012\u0000\u00cc\u00cd\u0005"+
		")\u0000\u0000\u00cd\'\u0001\u0000\u0000\u0000\u0012/6=DITX`fmt~\u0089"+
		"\u00a9\u00ad\u00b7\u00c5\u00c7";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}