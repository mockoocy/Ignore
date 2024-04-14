// Generated from /home/s2i/uczelnia/kompilatory/Ignore/src/grammar/ignoreParser.g4 by ANTLR 4.13.1
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
		ELIF_TAG=6, ELSE=7, ELSE_END=8, VAR_DECL_START=9, VAR_DECL_END=10, VAR_DECL_TYPE=11, 
		VAR_DECL=12, COMMENT=13, LINE_COMMENT=14, WS=15, OPEN_PROGRAM=16, CLOSE_PROGRAM=17, 
		CLOSE_TAG=18, OPEN_TAG=19, TAG_REFERENCE=20, FUNCTION_NAME=21, FUNCTION_RET_TYPE=22, 
		FUNCTION_PARAM=23, CONDITION_EQ=24, END_TAG=25, PROPERTY_NAME=26, OPEN_CURLY=27, 
		EXPR_WS=28, LITERAL_BOOL=29, NAME=30, LITERAL_STRING=31, COLON=32, OPEN_PAREN=33, 
		CLOSE_PAREN=34, LITERAL_INT=35, LITERAL_FLOAT=36, EQUALS=37, MUL=38, DIV=39, 
		ADD=40, SUB=41, MOD=42, INT_DIV=43, OPERATOR_COMPARE=44, OPERATOR_LOGIC=45, 
		EXPR_COMMENT=46, CLOSE_CURLY=47, EXPR_LINE_COMMENT=48;
	public static final int
		RULE_literalNumeric = 0, RULE_literal = 1, RULE_program = 2, RULE_statement = 3, 
		RULE_property = 4, RULE_endTag = 5, RULE_startTag = 6, RULE_block = 7, 
		RULE_functionCall = 8, RULE_functionStart = 9, RULE_function = 10, RULE_varDecl = 11, 
		RULE_var = 12, RULE_condition = 13, RULE_if = 14, RULE_if_statement = 15, 
		RULE_elif = 16, RULE_elif_statement = 17, RULE_else_statement = 18, RULE_control_statement = 19, 
		RULE_expr = 20, RULE_wrapped_expr = 21;
	private static String[] makeRuleNames() {
		return new String[] {
			"literalNumeric", "literal", "program", "statement", "property", "endTag", 
			"startTag", "block", "functionCall", "functionStart", "function", "varDecl", 
			"var", "condition", "if", "if_statement", "elif", "elif_statement", "else_statement", 
			"control_statement", "expr", "wrapped_expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'<function'", "'</function>'", "'<if'", "'</if>'", "'</elif>'", 
			"'<elif'", "'<else>'", "'</else>'", "'<var'", "'</var>'", null, null, 
			null, null, null, "'<program>'", "'</program>'", null, null, null, null, 
			null, null, "'condition='", "'>'", null, "'{'", null, null, null, null, 
			"':'", "'('", "')'", null, null, "'='", "'*'", "'/'", "'+'", "'-'", "'%'", 
			"'//'", null, null, null, "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "FUNCTION_TAG_OPEN", "FUNCTION_TAG_END", "IF_TAG", "IF_END", "ELIF_END", 
			"ELIF_TAG", "ELSE", "ELSE_END", "VAR_DECL_START", "VAR_DECL_END", "VAR_DECL_TYPE", 
			"VAR_DECL", "COMMENT", "LINE_COMMENT", "WS", "OPEN_PROGRAM", "CLOSE_PROGRAM", 
			"CLOSE_TAG", "OPEN_TAG", "TAG_REFERENCE", "FUNCTION_NAME", "FUNCTION_RET_TYPE", 
			"FUNCTION_PARAM", "CONDITION_EQ", "END_TAG", "PROPERTY_NAME", "OPEN_CURLY", 
			"EXPR_WS", "LITERAL_BOOL", "NAME", "LITERAL_STRING", "COLON", "OPEN_PAREN", 
			"CLOSE_PAREN", "LITERAL_INT", "LITERAL_FLOAT", "EQUALS", "MUL", "DIV", 
			"ADD", "SUB", "MOD", "INT_DIV", "OPERATOR_COMPARE", "OPERATOR_LOGIC", 
			"EXPR_COMMENT", "CLOSE_CURLY", "EXPR_LINE_COMMENT"
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
			setState(44);
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
			setState(46);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 105763569664L) != 0)) ) {
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
		public List<VarContext> var() {
			return getRuleContexts(VarContext.class);
		}
		public VarContext var(int i) {
			return getRuleContext(VarContext.class,i);
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
			setState(51);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCTION_TAG_OPEN) {
				{
				{
				setState(48);
				function();
				}
				}
				setState(53);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(54);
			match(OPEN_PROGRAM);
			setState(59);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 134746122L) != 0)) {
				{
				setState(57);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case FUNCTION_TAG_OPEN:
				case IF_TAG:
				case OPEN_TAG:
				case OPEN_CURLY:
					{
					setState(55);
					block();
					}
					break;
				case VAR_DECL:
					{
					setState(56);
					var();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(61);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(62);
			match(CLOSE_PROGRAM);
			setState(66);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCTION_TAG_OPEN) {
				{
				{
				setState(63);
				function();
				}
				}
				setState(68);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(69);
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
			setState(73);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(71);
				block();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(72);
				wrapped_expr();
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
			setState(75);
			match(PROPERTY_NAME);
			setState(78);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_CURLY:
				{
				setState(76);
				wrapped_expr();
				}
				break;
			case TAG_REFERENCE:
				{
				setState(77);
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
			setState(80);
			match(CLOSE_TAG);
			setState(81);
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
			setState(93);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(83);
				match(OPEN_TAG);
				setState(84);
				match(END_TAG);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(85);
				match(OPEN_TAG);
				setState(87); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(86);
					property();
					}
					}
					setState(89); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==PROPERTY_NAME );
				setState(91);
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
			setState(102);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_TAG:
				enterOuterAlt(_localctx, 1);
				{
				setState(95);
				startTag();
				setState(96);
				wrapped_expr();
				setState(97);
				endTag();
				}
				break;
			case OPEN_CURLY:
				enterOuterAlt(_localctx, 2);
				{
				setState(99);
				wrapped_expr();
				}
				break;
			case FUNCTION_TAG_OPEN:
				enterOuterAlt(_localctx, 3);
				{
				setState(100);
				function();
				}
				break;
			case IF_TAG:
				enterOuterAlt(_localctx, 4);
				{
				setState(101);
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
			setState(115);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(104);
				match(NAME);
				setState(105);
				match(OPEN_PAREN);
				setState(108);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
				case 1:
					{
					setState(106);
					expr(0);
					}
					break;
				case 2:
					{
					setState(107);
					literal();
					}
					break;
				}
				setState(110);
				match(CLOSE_PAREN);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(112);
				match(NAME);
				setState(113);
				match(OPEN_PAREN);
				setState(114);
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
			setState(117);
			match(FUNCTION_TAG_OPEN);
			setState(118);
			match(FUNCTION_NAME);
			setState(122);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCTION_PARAM) {
				{
				{
				setState(119);
				match(FUNCTION_PARAM);
				}
				}
				setState(124);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(125);
			match(FUNCTION_RET_TYPE);
			setState(126);
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
			setState(128);
			functionStart();
			setState(132);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 134742026L) != 0)) {
				{
				{
				setState(129);
				block();
				}
				}
				setState(134);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(135);
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
	public static class VarDeclContext extends ParserRuleContext {
		public TerminalNode VAR_DECL() { return getToken(ignoreParser.VAR_DECL, 0); }
		public TerminalNode FUNCTION_NAME() { return getToken(ignoreParser.FUNCTION_NAME, 0); }
		public TerminalNode END_TAG() { return getToken(ignoreParser.END_TAG, 0); }
		public TerminalNode VAR_DECL_TYPE() { return getToken(ignoreParser.VAR_DECL_TYPE, 0); }
		public VarDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDecl; }
	}

	public final VarDeclContext varDecl() throws RecognitionException {
		VarDeclContext _localctx = new VarDeclContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_varDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(137);
			match(VAR_DECL);
			setState(138);
			match(FUNCTION_NAME);
			setState(140);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VAR_DECL_TYPE) {
				{
				setState(139);
				match(VAR_DECL_TYPE);
				}
			}

			setState(142);
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
	public static class VarContext extends ParserRuleContext {
		public VarDeclContext varDecl() {
			return getRuleContext(VarDeclContext.class,0);
		}
		public Wrapped_exprContext wrapped_expr() {
			return getRuleContext(Wrapped_exprContext.class,0);
		}
		public TerminalNode VAR_DECL_END() { return getToken(ignoreParser.VAR_DECL_END, 0); }
		public VarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var; }
	}

	public final VarContext var() throws RecognitionException {
		VarContext _localctx = new VarContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_var);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(144);
			varDecl();
			setState(145);
			wrapped_expr();
			setState(146);
			match(VAR_DECL_END);
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
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode LITERAL_BOOL() { return getToken(ignoreParser.LITERAL_BOOL, 0); }
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_condition);
		try {
			setState(150);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(148);
				expr(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(149);
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
		enterRule(_localctx, 28, RULE_if);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(152);
			match(IF_TAG);
			setState(153);
			match(CONDITION_EQ);
			setState(154);
			match(OPEN_CURLY);
			{
			setState(155);
			condition();
			}
			setState(156);
			match(CLOSE_CURLY);
			setState(157);
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
		enterRule(_localctx, 30, RULE_if_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(159);
			if_();
			setState(160);
			statement();
			setState(161);
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
		enterRule(_localctx, 32, RULE_elif);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(163);
			match(ELIF_TAG);
			setState(164);
			match(CONDITION_EQ);
			setState(165);
			match(OPEN_CURLY);
			{
			setState(166);
			condition();
			}
			setState(167);
			match(CLOSE_CURLY);
			setState(168);
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
		enterRule(_localctx, 34, RULE_elif_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(170);
			elif();
			setState(171);
			statement();
			setState(172);
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
		enterRule(_localctx, 36, RULE_else_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(174);
			match(ELSE);
			setState(175);
			statement();
			setState(176);
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
		enterRule(_localctx, 38, RULE_control_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(178);
			if_statement();
			setState(182);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ELIF_TAG) {
				{
				{
				setState(179);
				elif_statement();
				}
				}
				setState(184);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(186);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(185);
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
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public TerminalNode NAME() { return getToken(ignoreParser.NAME, 0); }
		public TerminalNode MUL() { return getToken(ignoreParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(ignoreParser.DIV, 0); }
		public TerminalNode MOD() { return getToken(ignoreParser.MOD, 0); }
		public TerminalNode INT_DIV() { return getToken(ignoreParser.INT_DIV, 0); }
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
		int _startState = 40;
		enterRecursionRule(_localctx, 40, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(196);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				{
				setState(189);
				match(OPEN_PAREN);
				setState(190);
				expr(0);
				setState(191);
				match(CLOSE_PAREN);
				}
				break;
			case 2:
				{
				setState(193);
				literal();
				}
				break;
			case 3:
				{
				setState(194);
				functionCall();
				}
				break;
			case 4:
				{
				setState(195);
				match(NAME);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(212);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(210);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(198);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(199);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 14018773254144L) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(200);
						expr(6);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(201);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(202);
						_la = _input.LA(1);
						if ( !(_la==ADD || _la==SUB) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(203);
						expr(5);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(204);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						{
						setState(205);
						match(OPERATOR_COMPARE);
						}
						setState(206);
						expr(4);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(207);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						{
						setState(208);
						match(OPERATOR_LOGIC);
						}
						setState(209);
						expr(3);
						}
						break;
					}
					} 
				}
				setState(214);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
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
		enterRule(_localctx, 42, RULE_wrapped_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(215);
			match(OPEN_CURLY);
			setState(216);
			expr(0);
			setState(217);
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
		case 20:
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
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u00010\u00dc\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0005\u0002"+
		"2\b\u0002\n\u0002\f\u00025\t\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0005\u0002:\b\u0002\n\u0002\f\u0002=\t\u0002\u0001\u0002\u0001\u0002"+
		"\u0005\u0002A\b\u0002\n\u0002\f\u0002D\t\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0003\u0001\u0003\u0003\u0003J\b\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0003\u0004O\b\u0004\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0004\u0006X\b\u0006"+
		"\u000b\u0006\f\u0006Y\u0001\u0006\u0001\u0006\u0003\u0006^\b\u0006\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0003\u0007g\b\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0003\bm\b"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\bt\b\b\u0001\t\u0001"+
		"\t\u0001\t\u0005\ty\b\t\n\t\f\t|\t\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001"+
		"\n\u0005\n\u0083\b\n\n\n\f\n\u0086\t\n\u0001\n\u0001\n\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0003\u000b\u008d\b\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0003\r\u0097\b\r\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0013\u0001\u0013\u0005\u0013\u00b5\b\u0013\n\u0013"+
		"\f\u0013\u00b8\t\u0013\u0001\u0013\u0003\u0013\u00bb\b\u0013\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0003\u0014\u00c5\b\u0014\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0005\u0014\u00d3\b\u0014\n\u0014"+
		"\f\u0014\u00d6\t\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015"+
		"\u0001\u0015\u0000\u0001(\u0016\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010"+
		"\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*\u0000\u0004\u0001\u0000"+
		"#$\u0003\u0000\u001d\u001d\u001f\u001f#$\u0002\u0000&\'*+\u0001\u0000"+
		"()\u00df\u0000,\u0001\u0000\u0000\u0000\u0002.\u0001\u0000\u0000\u0000"+
		"\u00043\u0001\u0000\u0000\u0000\u0006I\u0001\u0000\u0000\u0000\bK\u0001"+
		"\u0000\u0000\u0000\nP\u0001\u0000\u0000\u0000\f]\u0001\u0000\u0000\u0000"+
		"\u000ef\u0001\u0000\u0000\u0000\u0010s\u0001\u0000\u0000\u0000\u0012u"+
		"\u0001\u0000\u0000\u0000\u0014\u0080\u0001\u0000\u0000\u0000\u0016\u0089"+
		"\u0001\u0000\u0000\u0000\u0018\u0090\u0001\u0000\u0000\u0000\u001a\u0096"+
		"\u0001\u0000\u0000\u0000\u001c\u0098\u0001\u0000\u0000\u0000\u001e\u009f"+
		"\u0001\u0000\u0000\u0000 \u00a3\u0001\u0000\u0000\u0000\"\u00aa\u0001"+
		"\u0000\u0000\u0000$\u00ae\u0001\u0000\u0000\u0000&\u00b2\u0001\u0000\u0000"+
		"\u0000(\u00c4\u0001\u0000\u0000\u0000*\u00d7\u0001\u0000\u0000\u0000,"+
		"-\u0007\u0000\u0000\u0000-\u0001\u0001\u0000\u0000\u0000./\u0007\u0001"+
		"\u0000\u0000/\u0003\u0001\u0000\u0000\u000002\u0003\u0014\n\u000010\u0001"+
		"\u0000\u0000\u000025\u0001\u0000\u0000\u000031\u0001\u0000\u0000\u0000"+
		"34\u0001\u0000\u0000\u000046\u0001\u0000\u0000\u000053\u0001\u0000\u0000"+
		"\u00006;\u0005\u0010\u0000\u00007:\u0003\u000e\u0007\u00008:\u0003\u0018"+
		"\f\u000097\u0001\u0000\u0000\u000098\u0001\u0000\u0000\u0000:=\u0001\u0000"+
		"\u0000\u0000;9\u0001\u0000\u0000\u0000;<\u0001\u0000\u0000\u0000<>\u0001"+
		"\u0000\u0000\u0000=;\u0001\u0000\u0000\u0000>B\u0005\u0011\u0000\u0000"+
		"?A\u0003\u0014\n\u0000@?\u0001\u0000\u0000\u0000AD\u0001\u0000\u0000\u0000"+
		"B@\u0001\u0000\u0000\u0000BC\u0001\u0000\u0000\u0000CE\u0001\u0000\u0000"+
		"\u0000DB\u0001\u0000\u0000\u0000EF\u0005\u0000\u0000\u0001F\u0005\u0001"+
		"\u0000\u0000\u0000GJ\u0003\u000e\u0007\u0000HJ\u0003*\u0015\u0000IG\u0001"+
		"\u0000\u0000\u0000IH\u0001\u0000\u0000\u0000J\u0007\u0001\u0000\u0000"+
		"\u0000KN\u0005\u001a\u0000\u0000LO\u0003*\u0015\u0000MO\u0005\u0014\u0000"+
		"\u0000NL\u0001\u0000\u0000\u0000NM\u0001\u0000\u0000\u0000O\t\u0001\u0000"+
		"\u0000\u0000PQ\u0005\u0012\u0000\u0000QR\u0005\u0019\u0000\u0000R\u000b"+
		"\u0001\u0000\u0000\u0000ST\u0005\u0013\u0000\u0000T^\u0005\u0019\u0000"+
		"\u0000UW\u0005\u0013\u0000\u0000VX\u0003\b\u0004\u0000WV\u0001\u0000\u0000"+
		"\u0000XY\u0001\u0000\u0000\u0000YW\u0001\u0000\u0000\u0000YZ\u0001\u0000"+
		"\u0000\u0000Z[\u0001\u0000\u0000\u0000[\\\u0005\u0019\u0000\u0000\\^\u0001"+
		"\u0000\u0000\u0000]S\u0001\u0000\u0000\u0000]U\u0001\u0000\u0000\u0000"+
		"^\r\u0001\u0000\u0000\u0000_`\u0003\f\u0006\u0000`a\u0003*\u0015\u0000"+
		"ab\u0003\n\u0005\u0000bg\u0001\u0000\u0000\u0000cg\u0003*\u0015\u0000"+
		"dg\u0003\u0014\n\u0000eg\u0003&\u0013\u0000f_\u0001\u0000\u0000\u0000"+
		"fc\u0001\u0000\u0000\u0000fd\u0001\u0000\u0000\u0000fe\u0001\u0000\u0000"+
		"\u0000g\u000f\u0001\u0000\u0000\u0000hi\u0005\u001e\u0000\u0000il\u0005"+
		"!\u0000\u0000jm\u0003(\u0014\u0000km\u0003\u0002\u0001\u0000lj\u0001\u0000"+
		"\u0000\u0000lk\u0001\u0000\u0000\u0000mn\u0001\u0000\u0000\u0000no\u0005"+
		"\"\u0000\u0000ot\u0001\u0000\u0000\u0000pq\u0005\u001e\u0000\u0000qr\u0005"+
		"!\u0000\u0000rt\u0005\"\u0000\u0000sh\u0001\u0000\u0000\u0000sp\u0001"+
		"\u0000\u0000\u0000t\u0011\u0001\u0000\u0000\u0000uv\u0005\u0001\u0000"+
		"\u0000vz\u0005\u0015\u0000\u0000wy\u0005\u0017\u0000\u0000xw\u0001\u0000"+
		"\u0000\u0000y|\u0001\u0000\u0000\u0000zx\u0001\u0000\u0000\u0000z{\u0001"+
		"\u0000\u0000\u0000{}\u0001\u0000\u0000\u0000|z\u0001\u0000\u0000\u0000"+
		"}~\u0005\u0016\u0000\u0000~\u007f\u0005\u0019\u0000\u0000\u007f\u0013"+
		"\u0001\u0000\u0000\u0000\u0080\u0084\u0003\u0012\t\u0000\u0081\u0083\u0003"+
		"\u000e\u0007\u0000\u0082\u0081\u0001\u0000\u0000\u0000\u0083\u0086\u0001"+
		"\u0000\u0000\u0000\u0084\u0082\u0001\u0000\u0000\u0000\u0084\u0085\u0001"+
		"\u0000\u0000\u0000\u0085\u0087\u0001\u0000\u0000\u0000\u0086\u0084\u0001"+
		"\u0000\u0000\u0000\u0087\u0088\u0005\u0002\u0000\u0000\u0088\u0015\u0001"+
		"\u0000\u0000\u0000\u0089\u008a\u0005\f\u0000\u0000\u008a\u008c\u0005\u0015"+
		"\u0000\u0000\u008b\u008d\u0005\u000b\u0000\u0000\u008c\u008b\u0001\u0000"+
		"\u0000\u0000\u008c\u008d\u0001\u0000\u0000\u0000\u008d\u008e\u0001\u0000"+
		"\u0000\u0000\u008e\u008f\u0005\u0019\u0000\u0000\u008f\u0017\u0001\u0000"+
		"\u0000\u0000\u0090\u0091\u0003\u0016\u000b\u0000\u0091\u0092\u0003*\u0015"+
		"\u0000\u0092\u0093\u0005\n\u0000\u0000\u0093\u0019\u0001\u0000\u0000\u0000"+
		"\u0094\u0097\u0003(\u0014\u0000\u0095\u0097\u0005\u001d\u0000\u0000\u0096"+
		"\u0094\u0001\u0000\u0000\u0000\u0096\u0095\u0001\u0000\u0000\u0000\u0097"+
		"\u001b\u0001\u0000\u0000\u0000\u0098\u0099\u0005\u0003\u0000\u0000\u0099"+
		"\u009a\u0005\u0018\u0000\u0000\u009a\u009b\u0005\u001b\u0000\u0000\u009b"+
		"\u009c\u0003\u001a\r\u0000\u009c\u009d\u0005/\u0000\u0000\u009d\u009e"+
		"\u0005\u0019\u0000\u0000\u009e\u001d\u0001\u0000\u0000\u0000\u009f\u00a0"+
		"\u0003\u001c\u000e\u0000\u00a0\u00a1\u0003\u0006\u0003\u0000\u00a1\u00a2"+
		"\u0005\u0004\u0000\u0000\u00a2\u001f\u0001\u0000\u0000\u0000\u00a3\u00a4"+
		"\u0005\u0006\u0000\u0000\u00a4\u00a5\u0005\u0018\u0000\u0000\u00a5\u00a6"+
		"\u0005\u001b\u0000\u0000\u00a6\u00a7\u0003\u001a\r\u0000\u00a7\u00a8\u0005"+
		"/\u0000\u0000\u00a8\u00a9\u0005\u0019\u0000\u0000\u00a9!\u0001\u0000\u0000"+
		"\u0000\u00aa\u00ab\u0003 \u0010\u0000\u00ab\u00ac\u0003\u0006\u0003\u0000"+
		"\u00ac\u00ad\u0005\u0005\u0000\u0000\u00ad#\u0001\u0000\u0000\u0000\u00ae"+
		"\u00af\u0005\u0007\u0000\u0000\u00af\u00b0\u0003\u0006\u0003\u0000\u00b0"+
		"\u00b1\u0005\b\u0000\u0000\u00b1%\u0001\u0000\u0000\u0000\u00b2\u00b6"+
		"\u0003\u001e\u000f\u0000\u00b3\u00b5\u0003\"\u0011\u0000\u00b4\u00b3\u0001"+
		"\u0000\u0000\u0000\u00b5\u00b8\u0001\u0000\u0000\u0000\u00b6\u00b4\u0001"+
		"\u0000\u0000\u0000\u00b6\u00b7\u0001\u0000\u0000\u0000\u00b7\u00ba\u0001"+
		"\u0000\u0000\u0000\u00b8\u00b6\u0001\u0000\u0000\u0000\u00b9\u00bb\u0003"+
		"$\u0012\u0000\u00ba\u00b9\u0001\u0000\u0000\u0000\u00ba\u00bb\u0001\u0000"+
		"\u0000\u0000\u00bb\'\u0001\u0000\u0000\u0000\u00bc\u00bd\u0006\u0014\uffff"+
		"\uffff\u0000\u00bd\u00be\u0005!\u0000\u0000\u00be\u00bf\u0003(\u0014\u0000"+
		"\u00bf\u00c0\u0005\"\u0000\u0000\u00c0\u00c5\u0001\u0000\u0000\u0000\u00c1"+
		"\u00c5\u0003\u0002\u0001\u0000\u00c2\u00c5\u0003\u0010\b\u0000\u00c3\u00c5"+
		"\u0005\u001e\u0000\u0000\u00c4\u00bc\u0001\u0000\u0000\u0000\u00c4\u00c1"+
		"\u0001\u0000\u0000\u0000\u00c4\u00c2\u0001\u0000\u0000\u0000\u00c4\u00c3"+
		"\u0001\u0000\u0000\u0000\u00c5\u00d4\u0001\u0000\u0000\u0000\u00c6\u00c7"+
		"\n\u0005\u0000\u0000\u00c7\u00c8\u0007\u0002\u0000\u0000\u00c8\u00d3\u0003"+
		"(\u0014\u0006\u00c9\u00ca\n\u0004\u0000\u0000\u00ca\u00cb\u0007\u0003"+
		"\u0000\u0000\u00cb\u00d3\u0003(\u0014\u0005\u00cc\u00cd\n\u0003\u0000"+
		"\u0000\u00cd\u00ce\u0005,\u0000\u0000\u00ce\u00d3\u0003(\u0014\u0004\u00cf"+
		"\u00d0\n\u0002\u0000\u0000\u00d0\u00d1\u0005-\u0000\u0000\u00d1\u00d3"+
		"\u0003(\u0014\u0003\u00d2\u00c6\u0001\u0000\u0000\u0000\u00d2\u00c9\u0001"+
		"\u0000\u0000\u0000\u00d2\u00cc\u0001\u0000\u0000\u0000\u00d2\u00cf\u0001"+
		"\u0000\u0000\u0000\u00d3\u00d6\u0001\u0000\u0000\u0000\u00d4\u00d2\u0001"+
		"\u0000\u0000\u0000\u00d4\u00d5\u0001\u0000\u0000\u0000\u00d5)\u0001\u0000"+
		"\u0000\u0000\u00d6\u00d4\u0001\u0000\u0000\u0000\u00d7\u00d8\u0005\u001b"+
		"\u0000\u0000\u00d8\u00d9\u0003(\u0014\u0000\u00d9\u00da\u0005/\u0000\u0000"+
		"\u00da+\u0001\u0000\u0000\u0000\u001439;BINY]flsz\u0084\u008c\u0096\u00b6"+
		"\u00ba\u00c4\u00d2\u00d4";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}