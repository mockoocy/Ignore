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
		LITERAL_INT=7, LITERAL_FLOAT=8, LITERAL_STRING=9, OPERATOR_ARITHMETIC=10, 
		OPERATOR_LOGIC=11, NAME=12, WS=13, OPEN_PROGRAM=14, CLOSE_PROGRAM=15, 
		NAME_EQ=16, RETURN_TYPE_EQ=17, CONDITION_EQ=18, IF_TAG=19, IF_END=20, 
		ELIF_END=21, ELIF_TAG=22, ELSE=23, ELSE_END=24, CONDITION_START=25, EQUALS=26, 
		MUL=27, DIV=28, ADD=29, SUB=30, OPEN_TAG=31, CLOSE_TAG=32, END_TAG=33, 
		FUNCTION_TAG_OPEN=34, FUNCTION_TAG_END=35;
	public static final int
		RULE_literalNumeric = 0, RULE_literal = 1, RULE_program = 2, RULE_statement = 3, 
		RULE_property = 4, RULE_openTag = 5, RULE_endTag = 6, RULE_startTag = 7, 
		RULE_block = 8, RULE_functionCall = 9, RULE_functionParam = 10, RULE_functionName = 11, 
		RULE_functionReturnType = 12, RULE_functionStart = 13, RULE_function = 14, 
		RULE_condition = 15, RULE_if = 16, RULE_if_statement = 17, RULE_elif = 18, 
		RULE_elif_statement = 19, RULE_else_statement = 20, RULE_control_statement = 21, 
		RULE_expr = 22, RULE_string_expr = 23;
	private static String[] makeRuleNames() {
		return new String[] {
			"literalNumeric", "literal", "program", "statement", "property", "openTag", 
			"endTag", "startTag", "block", "functionCall", "functionParam", "functionName", 
			"functionReturnType", "functionStart", "function", "condition", "if", 
			"if_statement", "elif", "elif_statement", "else_statement", "control_statement", 
			"expr", "string_expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "':'", "'('", "')'", "'{'", "'}'", null, null, null, null, null, 
			null, null, null, "'<program>'", "'</program>'", "'name='", "'returnType='", 
			null, null, "'</if>'", "'</elif>'", null, "'<else>'", "'</else>'", null, 
			"'='", "'*'", "'/'", "'+'", "'-'", "'<'", "'</'", "'>'", "'<function'", 
			"'</function>'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "COLON", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_CURLY", "CLOSE_CURLY", 
			"LITERAL_BOOL", "LITERAL_INT", "LITERAL_FLOAT", "LITERAL_STRING", "OPERATOR_ARITHMETIC", 
			"OPERATOR_LOGIC", "NAME", "WS", "OPEN_PROGRAM", "CLOSE_PROGRAM", "NAME_EQ", 
			"RETURN_TYPE_EQ", "CONDITION_EQ", "IF_TAG", "IF_END", "ELIF_END", "ELIF_TAG", 
			"ELSE", "ELSE_END", "CONDITION_START", "EQUALS", "MUL", "DIV", "ADD", 
			"SUB", "OPEN_TAG", "CLOSE_TAG", "END_TAG", "FUNCTION_TAG_OPEN", "FUNCTION_TAG_END"
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
			setState(48);
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
			setState(50);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 960L) != 0)) ) {
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
			setState(55);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCTION_TAG_OPEN) {
				{
				{
				setState(52);
				function();
				}
				}
				setState(57);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(58);
			match(OPEN_PROGRAM);
			setState(62);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 19327877120L) != 0)) {
				{
				{
				setState(59);
				block();
				}
				}
				setState(64);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(65);
			match(CLOSE_PROGRAM);
			setState(69);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCTION_TAG_OPEN) {
				{
				{
				setState(66);
				function();
				}
				}
				setState(71);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(72);
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
			setState(76);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IF_TAG:
			case OPEN_TAG:
			case FUNCTION_TAG_OPEN:
				enterOuterAlt(_localctx, 1);
				{
				setState(74);
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
				setState(75);
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
			setState(78);
			match(NAME);
			setState(79);
			match(EQUALS);
			setState(85);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_CURLY:
				{
				setState(80);
				match(OPEN_CURLY);
				setState(81);
				expr(0);
				setState(82);
				match(CLOSE_CURLY);
				}
				break;
			case NAME:
				{
				setState(84);
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
	public static class OpenTagContext extends ParserRuleContext {
		public TerminalNode OPEN_TAG() { return getToken(ignoreParser.OPEN_TAG, 0); }
		public TerminalNode NAME() { return getToken(ignoreParser.NAME, 0); }
		public OpenTagContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_openTag; }
	}

	public final OpenTagContext openTag() throws RecognitionException {
		OpenTagContext _localctx = new OpenTagContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_openTag);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			match(OPEN_TAG);
			setState(88);
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
		enterRule(_localctx, 12, RULE_endTag);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			match(CLOSE_TAG);
			setState(91);
			match(NAME);
			setState(92);
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
		public OpenTagContext openTag() {
			return getRuleContext(OpenTagContext.class,0);
		}
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
		enterRule(_localctx, 14, RULE_startTag);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			openTag();
			setState(98);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NAME) {
				{
				{
				setState(95);
				property();
				}
				}
				setState(100);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(101);
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
		enterRule(_localctx, 16, RULE_block);
		try {
			setState(109);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_TAG:
				enterOuterAlt(_localctx, 1);
				{
				setState(103);
				startTag();
				setState(104);
				expr(0);
				setState(105);
				endTag();
				}
				break;
			case FUNCTION_TAG_OPEN:
				enterOuterAlt(_localctx, 2);
				{
				setState(107);
				function();
				}
				break;
			case IF_TAG:
				enterOuterAlt(_localctx, 3);
				{
				setState(108);
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
		enterRule(_localctx, 18, RULE_functionCall);
		try {
			setState(122);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(111);
				match(NAME);
				setState(112);
				match(OPEN_PAREN);
				setState(115);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
				case 1:
					{
					setState(113);
					expr(0);
					}
					break;
				case 2:
					{
					setState(114);
					literal();
					}
					break;
				}
				setState(117);
				match(CLOSE_PAREN);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(119);
				match(NAME);
				setState(120);
				match(OPEN_PAREN);
				setState(121);
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
		enterRule(_localctx, 20, RULE_functionParam);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(124);
			match(NAME);
			setState(125);
			match(COLON);
			setState(126);
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
		enterRule(_localctx, 22, RULE_functionName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			match(NAME_EQ);
			setState(129);
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
		enterRule(_localctx, 24, RULE_functionReturnType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(131);
			match(RETURN_TYPE_EQ);
			setState(132);
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
		enterRule(_localctx, 26, RULE_functionStart);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(134);
			match(FUNCTION_TAG_OPEN);
			setState(135);
			functionName();
			setState(139);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NAME) {
				{
				{
				setState(136);
				functionParam();
				}
				}
				setState(141);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(142);
			functionReturnType();
			setState(143);
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
		enterRule(_localctx, 28, RULE_function);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(145);
			functionStart();
			setState(149);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 19327877120L) != 0)) {
				{
				{
				setState(146);
				block();
				}
				}
				setState(151);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(152);
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
		enterRule(_localctx, 30, RULE_condition);
		try {
			setState(160);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(154);
				expr(0);
				setState(155);
				match(OPERATOR_LOGIC);
				setState(156);
				expr(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(158);
				expr(0);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(159);
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
		enterRule(_localctx, 32, RULE_if);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(162);
			match(IF_TAG);
			setState(163);
			match(CONDITION_EQ);
			setState(164);
			match(OPEN_CURLY);
			{
			setState(165);
			condition();
			}
			setState(166);
			match(CLOSE_CURLY);
			setState(167);
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
		enterRule(_localctx, 34, RULE_if_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(169);
			if_();
			setState(170);
			statement();
			setState(171);
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
		public TerminalNode CONDITION_START() { return getToken(ignoreParser.CONDITION_START, 0); }
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
		enterRule(_localctx, 36, RULE_elif);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(173);
			match(ELIF_TAG);
			setState(174);
			match(CONDITION_START);
			setState(175);
			match(OPEN_CURLY);
			{
			setState(176);
			condition();
			}
			setState(177);
			match(CLOSE_CURLY);
			setState(178);
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
		enterRule(_localctx, 38, RULE_elif_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(180);
			elif();
			setState(181);
			statement();
			setState(182);
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
		enterRule(_localctx, 40, RULE_else_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(184);
			match(ELSE);
			setState(185);
			statement();
			setState(186);
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
		enterRule(_localctx, 42, RULE_control_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(188);
			if_statement();
			setState(192);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ELIF_TAG) {
				{
				{
				setState(189);
				elif_statement();
				}
				}
				setState(194);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(196);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(195);
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
		int _startState = 44;
		enterRecursionRule(_localctx, 44, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(206);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				{
				setState(199);
				match(OPEN_PAREN);
				setState(200);
				expr(0);
				setState(201);
				match(CLOSE_PAREN);
				}
				break;
			case 2:
				{
				setState(203);
				match(NAME);
				}
				break;
			case 3:
				{
				setState(204);
				literal();
				}
				break;
			case 4:
				{
				setState(205);
				functionCall();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(222);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(220);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(208);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(209);
						_la = _input.LA(1);
						if ( !(_la==MUL || _la==DIV) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(210);
						expr(5);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(211);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(212);
						_la = _input.LA(1);
						if ( !(_la==ADD || _la==SUB) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(213);
						expr(4);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(214);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						{
						setState(215);
						match(OPERATOR_ARITHMETIC);
						}
						setState(216);
						expr(3);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(217);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(218);
						match(OPERATOR_LOGIC);
						setState(219);
						expr(2);
						}
						break;
					}
					} 
				}
				setState(224);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
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
		enterRule(_localctx, 46, RULE_string_expr);
		try {
			setState(227);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(225);
				match(LITERAL_STRING);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(226);
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
		case 22:
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
		"\u0004\u0001#\u00e6\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0005\u00026\b\u0002\n\u0002\f\u0002"+
		"9\t\u0002\u0001\u0002\u0001\u0002\u0005\u0002=\b\u0002\n\u0002\f\u0002"+
		"@\t\u0002\u0001\u0002\u0001\u0002\u0005\u0002D\b\u0002\n\u0002\f\u0002"+
		"G\t\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0003\u0003"+
		"M\b\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0003\u0004V\b\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0001\u0007\u0005\u0007a\b\u0007\n\u0007\f\u0007d\t\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\bn"+
		"\b\b\u0001\t\u0001\t\u0001\t\u0001\t\u0003\tt\b\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0003\t{\b\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r"+
		"\u0001\r\u0005\r\u008a\b\r\n\r\f\r\u008d\t\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\u000e\u0001\u000e\u0005\u000e\u0094\b\u000e\n\u000e\f\u000e\u0097\t\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0003\u000f\u00a1\b\u000f\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0001\u0015\u0001\u0015\u0005\u0015\u00bf\b\u0015\n\u0015\f\u0015\u00c2"+
		"\t\u0015\u0001\u0015\u0003\u0015\u00c5\b\u0015\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0003\u0016\u00cf\b\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0005\u0016\u00dd\b\u0016\n\u0016\f\u0016\u00e0"+
		"\t\u0016\u0001\u0017\u0001\u0017\u0003\u0017\u00e4\b\u0017\u0001\u0017"+
		"\u0000\u0001,\u0018\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014"+
		"\u0016\u0018\u001a\u001c\u001e \"$&(*,.\u0000\u0004\u0001\u0000\u0007"+
		"\b\u0001\u0000\u0006\t\u0001\u0000\u001b\u001c\u0001\u0000\u001d\u001e"+
		"\u00e5\u00000\u0001\u0000\u0000\u0000\u00022\u0001\u0000\u0000\u0000\u0004"+
		"7\u0001\u0000\u0000\u0000\u0006L\u0001\u0000\u0000\u0000\bN\u0001\u0000"+
		"\u0000\u0000\nW\u0001\u0000\u0000\u0000\fZ\u0001\u0000\u0000\u0000\u000e"+
		"^\u0001\u0000\u0000\u0000\u0010m\u0001\u0000\u0000\u0000\u0012z\u0001"+
		"\u0000\u0000\u0000\u0014|\u0001\u0000\u0000\u0000\u0016\u0080\u0001\u0000"+
		"\u0000\u0000\u0018\u0083\u0001\u0000\u0000\u0000\u001a\u0086\u0001\u0000"+
		"\u0000\u0000\u001c\u0091\u0001\u0000\u0000\u0000\u001e\u00a0\u0001\u0000"+
		"\u0000\u0000 \u00a2\u0001\u0000\u0000\u0000\"\u00a9\u0001\u0000\u0000"+
		"\u0000$\u00ad\u0001\u0000\u0000\u0000&\u00b4\u0001\u0000\u0000\u0000("+
		"\u00b8\u0001\u0000\u0000\u0000*\u00bc\u0001\u0000\u0000\u0000,\u00ce\u0001"+
		"\u0000\u0000\u0000.\u00e3\u0001\u0000\u0000\u000001\u0007\u0000\u0000"+
		"\u00001\u0001\u0001\u0000\u0000\u000023\u0007\u0001\u0000\u00003\u0003"+
		"\u0001\u0000\u0000\u000046\u0003\u001c\u000e\u000054\u0001\u0000\u0000"+
		"\u000069\u0001\u0000\u0000\u000075\u0001\u0000\u0000\u000078\u0001\u0000"+
		"\u0000\u00008:\u0001\u0000\u0000\u000097\u0001\u0000\u0000\u0000:>\u0005"+
		"\u000e\u0000\u0000;=\u0003\u0010\b\u0000<;\u0001\u0000\u0000\u0000=@\u0001"+
		"\u0000\u0000\u0000><\u0001\u0000\u0000\u0000>?\u0001\u0000\u0000\u0000"+
		"?A\u0001\u0000\u0000\u0000@>\u0001\u0000\u0000\u0000AE\u0005\u000f\u0000"+
		"\u0000BD\u0003\u001c\u000e\u0000CB\u0001\u0000\u0000\u0000DG\u0001\u0000"+
		"\u0000\u0000EC\u0001\u0000\u0000\u0000EF\u0001\u0000\u0000\u0000FH\u0001"+
		"\u0000\u0000\u0000GE\u0001\u0000\u0000\u0000HI\u0005\u0000\u0000\u0001"+
		"I\u0005\u0001\u0000\u0000\u0000JM\u0003\u0010\b\u0000KM\u0003,\u0016\u0000"+
		"LJ\u0001\u0000\u0000\u0000LK\u0001\u0000\u0000\u0000M\u0007\u0001\u0000"+
		"\u0000\u0000NO\u0005\f\u0000\u0000OU\u0005\u001a\u0000\u0000PQ\u0005\u0004"+
		"\u0000\u0000QR\u0003,\u0016\u0000RS\u0005\u0005\u0000\u0000SV\u0001\u0000"+
		"\u0000\u0000TV\u0005\f\u0000\u0000UP\u0001\u0000\u0000\u0000UT\u0001\u0000"+
		"\u0000\u0000V\t\u0001\u0000\u0000\u0000WX\u0005\u001f\u0000\u0000XY\u0005"+
		"\f\u0000\u0000Y\u000b\u0001\u0000\u0000\u0000Z[\u0005 \u0000\u0000[\\"+
		"\u0005\f\u0000\u0000\\]\u0005!\u0000\u0000]\r\u0001\u0000\u0000\u0000"+
		"^b\u0003\n\u0005\u0000_a\u0003\b\u0004\u0000`_\u0001\u0000\u0000\u0000"+
		"ad\u0001\u0000\u0000\u0000b`\u0001\u0000\u0000\u0000bc\u0001\u0000\u0000"+
		"\u0000ce\u0001\u0000\u0000\u0000db\u0001\u0000\u0000\u0000ef\u0005!\u0000"+
		"\u0000f\u000f\u0001\u0000\u0000\u0000gh\u0003\u000e\u0007\u0000hi\u0003"+
		",\u0016\u0000ij\u0003\f\u0006\u0000jn\u0001\u0000\u0000\u0000kn\u0003"+
		"\u001c\u000e\u0000ln\u0003*\u0015\u0000mg\u0001\u0000\u0000\u0000mk\u0001"+
		"\u0000\u0000\u0000ml\u0001\u0000\u0000\u0000n\u0011\u0001\u0000\u0000"+
		"\u0000op\u0005\f\u0000\u0000ps\u0005\u0002\u0000\u0000qt\u0003,\u0016"+
		"\u0000rt\u0003\u0002\u0001\u0000sq\u0001\u0000\u0000\u0000sr\u0001\u0000"+
		"\u0000\u0000tu\u0001\u0000\u0000\u0000uv\u0005\u0003\u0000\u0000v{\u0001"+
		"\u0000\u0000\u0000wx\u0005\f\u0000\u0000xy\u0005\u0002\u0000\u0000y{\u0005"+
		"\u0003\u0000\u0000zo\u0001\u0000\u0000\u0000zw\u0001\u0000\u0000\u0000"+
		"{\u0013\u0001\u0000\u0000\u0000|}\u0005\f\u0000\u0000}~\u0005\u0001\u0000"+
		"\u0000~\u007f\u0005\f\u0000\u0000\u007f\u0015\u0001\u0000\u0000\u0000"+
		"\u0080\u0081\u0005\u0010\u0000\u0000\u0081\u0082\u0005\f\u0000\u0000\u0082"+
		"\u0017\u0001\u0000\u0000\u0000\u0083\u0084\u0005\u0011\u0000\u0000\u0084"+
		"\u0085\u0005\f\u0000\u0000\u0085\u0019\u0001\u0000\u0000\u0000\u0086\u0087"+
		"\u0005\"\u0000\u0000\u0087\u008b\u0003\u0016\u000b\u0000\u0088\u008a\u0003"+
		"\u0014\n\u0000\u0089\u0088\u0001\u0000\u0000\u0000\u008a\u008d\u0001\u0000"+
		"\u0000\u0000\u008b\u0089\u0001\u0000\u0000\u0000\u008b\u008c\u0001\u0000"+
		"\u0000\u0000\u008c\u008e\u0001\u0000\u0000\u0000\u008d\u008b\u0001\u0000"+
		"\u0000\u0000\u008e\u008f\u0003\u0018\f\u0000\u008f\u0090\u0005!\u0000"+
		"\u0000\u0090\u001b\u0001\u0000\u0000\u0000\u0091\u0095\u0003\u001a\r\u0000"+
		"\u0092\u0094\u0003\u0010\b\u0000\u0093\u0092\u0001\u0000\u0000\u0000\u0094"+
		"\u0097\u0001\u0000\u0000\u0000\u0095\u0093\u0001\u0000\u0000\u0000\u0095"+
		"\u0096\u0001\u0000\u0000\u0000\u0096\u0098\u0001\u0000\u0000\u0000\u0097"+
		"\u0095\u0001\u0000\u0000\u0000\u0098\u0099\u0005#\u0000\u0000\u0099\u001d"+
		"\u0001\u0000\u0000\u0000\u009a\u009b\u0003,\u0016\u0000\u009b\u009c\u0005"+
		"\u000b\u0000\u0000\u009c\u009d\u0003,\u0016\u0000\u009d\u00a1\u0001\u0000"+
		"\u0000\u0000\u009e\u00a1\u0003,\u0016\u0000\u009f\u00a1\u0005\u0006\u0000"+
		"\u0000\u00a0\u009a\u0001\u0000\u0000\u0000\u00a0\u009e\u0001\u0000\u0000"+
		"\u0000\u00a0\u009f\u0001\u0000\u0000\u0000\u00a1\u001f\u0001\u0000\u0000"+
		"\u0000\u00a2\u00a3\u0005\u0013\u0000\u0000\u00a3\u00a4\u0005\u0012\u0000"+
		"\u0000\u00a4\u00a5\u0005\u0004\u0000\u0000\u00a5\u00a6\u0003\u001e\u000f"+
		"\u0000\u00a6\u00a7\u0005\u0005\u0000\u0000\u00a7\u00a8\u0005!\u0000\u0000"+
		"\u00a8!\u0001\u0000\u0000\u0000\u00a9\u00aa\u0003 \u0010\u0000\u00aa\u00ab"+
		"\u0003\u0006\u0003\u0000\u00ab\u00ac\u0005\u0014\u0000\u0000\u00ac#\u0001"+
		"\u0000\u0000\u0000\u00ad\u00ae\u0005\u0016\u0000\u0000\u00ae\u00af\u0005"+
		"\u0019\u0000\u0000\u00af\u00b0\u0005\u0004\u0000\u0000\u00b0\u00b1\u0003"+
		"\u001e\u000f\u0000\u00b1\u00b2\u0005\u0005\u0000\u0000\u00b2\u00b3\u0005"+
		"!\u0000\u0000\u00b3%\u0001\u0000\u0000\u0000\u00b4\u00b5\u0003$\u0012"+
		"\u0000\u00b5\u00b6\u0003\u0006\u0003\u0000\u00b6\u00b7\u0005\u0015\u0000"+
		"\u0000\u00b7\'\u0001\u0000\u0000\u0000\u00b8\u00b9\u0005\u0017\u0000\u0000"+
		"\u00b9\u00ba\u0003\u0006\u0003\u0000\u00ba\u00bb\u0005\u0018\u0000\u0000"+
		"\u00bb)\u0001\u0000\u0000\u0000\u00bc\u00c0\u0003\"\u0011\u0000\u00bd"+
		"\u00bf\u0003&\u0013\u0000\u00be\u00bd\u0001\u0000\u0000\u0000\u00bf\u00c2"+
		"\u0001\u0000\u0000\u0000\u00c0\u00be\u0001\u0000\u0000\u0000\u00c0\u00c1"+
		"\u0001\u0000\u0000\u0000\u00c1\u00c4\u0001\u0000\u0000\u0000\u00c2\u00c0"+
		"\u0001\u0000\u0000\u0000\u00c3\u00c5\u0003(\u0014\u0000\u00c4\u00c3\u0001"+
		"\u0000\u0000\u0000\u00c4\u00c5\u0001\u0000\u0000\u0000\u00c5+\u0001\u0000"+
		"\u0000\u0000\u00c6\u00c7\u0006\u0016\uffff\uffff\u0000\u00c7\u00c8\u0005"+
		"\u0002\u0000\u0000\u00c8\u00c9\u0003,\u0016\u0000\u00c9\u00ca\u0005\u0003"+
		"\u0000\u0000\u00ca\u00cf\u0001\u0000\u0000\u0000\u00cb\u00cf\u0005\f\u0000"+
		"\u0000\u00cc\u00cf\u0003\u0002\u0001\u0000\u00cd\u00cf\u0003\u0012\t\u0000"+
		"\u00ce\u00c6\u0001\u0000\u0000\u0000\u00ce\u00cb\u0001\u0000\u0000\u0000"+
		"\u00ce\u00cc\u0001\u0000\u0000\u0000\u00ce\u00cd\u0001\u0000\u0000\u0000"+
		"\u00cf\u00de\u0001\u0000\u0000\u0000\u00d0\u00d1\n\u0004\u0000\u0000\u00d1"+
		"\u00d2\u0007\u0002\u0000\u0000\u00d2\u00dd\u0003,\u0016\u0005\u00d3\u00d4"+
		"\n\u0003\u0000\u0000\u00d4\u00d5\u0007\u0003\u0000\u0000\u00d5\u00dd\u0003"+
		",\u0016\u0004\u00d6\u00d7\n\u0002\u0000\u0000\u00d7\u00d8\u0005\n\u0000"+
		"\u0000\u00d8\u00dd\u0003,\u0016\u0003\u00d9\u00da\n\u0001\u0000\u0000"+
		"\u00da\u00db\u0005\u000b\u0000\u0000\u00db\u00dd\u0003,\u0016\u0002\u00dc"+
		"\u00d0\u0001\u0000\u0000\u0000\u00dc\u00d3\u0001\u0000\u0000\u0000\u00dc"+
		"\u00d6\u0001\u0000\u0000\u0000\u00dc\u00d9\u0001\u0000\u0000\u0000\u00dd"+
		"\u00e0\u0001\u0000\u0000\u0000\u00de\u00dc\u0001\u0000\u0000\u0000\u00de"+
		"\u00df\u0001\u0000\u0000\u0000\u00df-\u0001\u0000\u0000\u0000\u00e0\u00de"+
		"\u0001\u0000\u0000\u0000\u00e1\u00e4\u0005\t\u0000\u0000\u00e2\u00e4\u0003"+
		",\u0016\u0000\u00e3\u00e1\u0001\u0000\u0000\u0000\u00e3\u00e2\u0001\u0000"+
		"\u0000\u0000\u00e4/\u0001\u0000\u0000\u0000\u00127>ELUbmsz\u008b\u0095"+
		"\u00a0\u00c0\u00c4\u00ce\u00dc\u00de\u00e3";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}