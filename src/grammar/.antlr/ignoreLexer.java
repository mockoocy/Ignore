// Generated from /home/s2i/uczelnia/kompilatory/Ignore/src/grammar/ignoreLexer.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class ignoreLexer extends Lexer {
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
		ADD=40, SUB=41, OPERATOR_COMPARE=42, OPERATOR_LOGIC=43, EXPR_COMMENT=44, 
		CLOSE_CURLY=45, EXPR_LINE_COMMENT=46;
	public static final int
		expr=1;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE", "expr"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"DIGIT", "FUNCTION_TAG_OPEN", "FUNCTION_TAG_END", "IF_TAG", "IF_END", 
			"ELIF_END", "ELIF_TAG", "ELSE", "ELSE_END", "VAR_DECL_START", "VAR_DECL_END", 
			"VAR_DECL_TYPE", "VAR_DECL", "COMMENT", "LINE_COMMENT", "ID", "WS", "OPEN_PROGRAM", 
			"CLOSE_PROGRAM", "CLOSE_TAG", "OPEN_TAG", "TAG_REFERENCE", "FUNCTION_NAME", 
			"FUNCTION_RET_TYPE", "FUNCTION_PARAM", "CONDITION_EQ", "END_TAG", "PROPERTY_NAME", 
			"OPEN_CURLY", "EXPR_WS", "LITERAL_BOOL", "NAME", "LITERAL_STRING", "COLON", 
			"OPEN_PAREN", "CLOSE_PAREN", "LITERAL_INT", "LITERAL_FLOAT", "EQUALS", 
			"MUL", "DIV", "ADD", "SUB", "OPERATOR_COMPARE", "OPERATOR_LOGIC", "EXPR_COMMENT", 
			"CLOSE_CURLY", "EXPR_LINE_COMMENT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'<function'", "'</function>'", "'<if'", "'</if>'", "'</elif>'", 
			"'<elif'", "'<else>'", "'</else>'", "'<var'", "'</var>'", null, null, 
			null, null, null, "'<program>'", "'</program>'", null, null, null, null, 
			null, null, "'condition='", "'>'", null, "'{'", null, null, null, null, 
			"':'", "'('", "')'", null, null, "'='", "'*'", "'/'", "'+'", "'-'", null, 
			null, null, "'}'"
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
			"ADD", "SUB", "OPERATOR_COMPARE", "OPERATOR_LOGIC", "EXPR_COMMENT", "CLOSE_CURLY", 
			"EXPR_LINE_COMMENT"
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


	public ignoreLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "ignoreLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000.\u019b\u0006\uffff\uffff\u0006\uffff\uffff\u0002\u0000\u0007"+
		"\u0000\u0002\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007"+
		"\u0003\u0002\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007"+
		"\u0006\u0002\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n"+
		"\u0007\n\u0002\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002"+
		"\u000e\u0007\u000e\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002"+
		"\u0011\u0007\u0011\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002"+
		"\u0014\u0007\u0014\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002"+
		"\u0017\u0007\u0017\u0002\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002"+
		"\u001a\u0007\u001a\u0002\u001b\u0007\u001b\u0002\u001c\u0007\u001c\u0002"+
		"\u001d\u0007\u001d\u0002\u001e\u0007\u001e\u0002\u001f\u0007\u001f\u0002"+
		" \u0007 \u0002!\u0007!\u0002\"\u0007\"\u0002#\u0007#\u0002$\u0007$\u0002"+
		"%\u0007%\u0002&\u0007&\u0002\'\u0007\'\u0002(\u0007(\u0002)\u0007)\u0002"+
		"*\u0007*\u0002+\u0007+\u0002,\u0007,\u0002-\u0007-\u0002.\u0007.\u0002"+
		"/\u0007/\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001"+
		"\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r\u0005\r\u00bd\b\r\n\r\f\r\u00c0"+
		"\t\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0005\u000e\u00cb\b\u000e\n\u000e\f\u000e\u00ce\t\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0005\u000f\u00d4\b\u000f"+
		"\n\u000f\f\u000f\u00d7\t\u000f\u0001\u000f\u0003\u000f\u00da\b\u000f\u0001"+
		"\u0010\u0004\u0010\u00dd\b\u0010\u000b\u0010\f\u0010\u00de\u0001\u0010"+
		"\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u001a\u0001\u001a\u0001\u001b"+
		"\u0001\u001b\u0001\u001b\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c"+
		"\u0001\u001d\u0004\u001d\u0131\b\u001d\u000b\u001d\f\u001d\u0132\u0001"+
		"\u001d\u0001\u001d\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0003\u001e\u0140"+
		"\b\u001e\u0001\u001f\u0001\u001f\u0001 \u0001 \u0005 \u0146\b \n \f \u0149"+
		"\t \u0001 \u0001 \u0001!\u0001!\u0001\"\u0001\"\u0001#\u0001#\u0001$\u0004"+
		"$\u0154\b$\u000b$\f$\u0155\u0001%\u0004%\u0159\b%\u000b%\f%\u015a\u0001"+
		"%\u0001%\u0005%\u015f\b%\n%\f%\u0162\t%\u0001&\u0001&\u0001\'\u0001\'"+
		"\u0001(\u0001(\u0001)\u0001)\u0001*\u0001*\u0001+\u0001+\u0001+\u0001"+
		"+\u0001+\u0001+\u0001+\u0001+\u0001+\u0003+\u0177\b+\u0001,\u0001,\u0001"+
		",\u0001,\u0003,\u017d\b,\u0001-\u0001-\u0001-\u0001-\u0005-\u0183\b-\n"+
		"-\f-\u0186\t-\u0001-\u0001-\u0001-\u0001-\u0001-\u0001.\u0001.\u0001."+
		"\u0001.\u0001/\u0001/\u0001/\u0001/\u0005/\u0195\b/\n/\f/\u0198\t/\u0001"+
		"/\u0001/\u0003\u00be\u0147\u0184\u00000\u0002\u0000\u0004\u0001\u0006"+
		"\u0002\b\u0003\n\u0004\f\u0005\u000e\u0006\u0010\u0007\u0012\b\u0014\t"+
		"\u0016\n\u0018\u000b\u001a\f\u001c\r\u001e\u000e \u0000\"\u000f$\u0010"+
		"&\u0011(\u0012*\u0013,\u0014.\u00150\u00162\u00174\u00186\u00198\u001a"+
		":\u001b<\u001c>\u001d@\u001eB\u001fD F!H\"J#L$N%P&R\'T(V)X*Z+\\,^-`.\u0002"+
		"\u0000\u0001\u0007\u0001\u000009\u0002\u0000\n\n\r\r\u0002\u0000AZaz\u0004"+
		"\u000009AZ__azR\u0000  \u231a\u231b\u23e9\u23ec\u23f0\u23f0\u23f3\u23f3"+
		"\u25fd\u25fe\u2614\u2615\u2648\u2653\u267f\u267f\u2693\u2693\u26a1\u26a1"+
		"\u26aa\u26ab\u26bd\u26be\u26c4\u26c5\u26ce\u26ce\u26d4\u26d4\u26ea\u26ea"+
		"\u26f2\u26f3\u26f5\u26f5\u26fa\u26fa\u26fd\u26fd\u2705\u2705\u270a\u270b"+
		"\u2728\u2728\u274c\u274c\u274e\u274e\u2753\u2755\u2757\u2757\u2795\u2797"+
		"\u27b0\u27b0\u27bf\u27bf\u2b1b\u2b1c\u2b50\u2b50\u2b55\u2b55\u8001\uf004"+
		"\u8001\uf004\u8001\uf0cf\u8001\uf0cf\u8001\uf18e\u8001\uf18e\u8001\uf191"+
		"\u8001\uf19a\u8001\uf1e6\u8001\uf1ff\u8001\uf201\u8001\uf201\u8001\uf21a"+
		"\u8001\uf21a\u8001\uf22f\u8001\uf22f\u8001\uf232\u8001\uf236\u8001\uf238"+
		"\u8001\uf23a\u8001\uf250\u8001\uf251\u8001\uf300\u8001\uf320\u8001\uf32d"+
		"\u8001\uf335\u8001\uf337\u8001\uf37c\u8001\uf37e\u8001\uf393\u8001\uf3a0"+
		"\u8001\uf3ca\u8001\uf3cf\u8001\uf3d3\u8001\uf3e0\u8001\uf3f0\u8001\uf3f4"+
		"\u8001\uf3f4\u8001\uf3f8\u8001\uf43e\u8001\uf440\u8001\uf440\u8001\uf442"+
		"\u8001\uf4fc\u8001\uf4ff\u8001\uf53d\u8001\uf54b\u8001\uf54e\u8001\uf550"+
		"\u8001\uf567\u8001\uf57a\u8001\uf57a\u8001\uf595\u8001\uf596\u8001\uf5a4"+
		"\u8001\uf5a4\u8001\uf5fb\u8001\uf64f\u8001\uf680\u8001\uf6c5\u8001\uf6cc"+
		"\u8001\uf6cc\u8001\uf6d0\u8001\uf6d2\u8001\uf6d5\u8001\uf6d7\u8001\uf6dc"+
		"\u8001\uf6df\u8001\uf6eb\u8001\uf6ec\u8001\uf6f4\u8001\uf6fc\u8001\uf7e0"+
		"\u8001\uf7eb\u8001\uf7f0\u8001\uf7f0\u8001\uf90c\u8001\uf93a\u8001\uf93c"+
		"\u8001\uf945\u8001\uf947\u8001\uf9ff\u8001\ufa70\u8001\ufa7c\u8001\ufa80"+
		"\u8001\ufa88\u8001\ufa90\u8001\ufabd\u8001\ufabf\u8001\ufac5\u8001\uface"+
		"\u8001\ufadb\u8001\ufae0\u8001\ufae8\u8001\ufaf0\u8001\ufaf8\u0003\u0000"+
		"\t\n\r\r  \u0002\u0000<<>>\u01a9\u0000\u0004\u0001\u0000\u0000\u0000\u0000"+
		"\u0006\u0001\u0000\u0000\u0000\u0000\b\u0001\u0000\u0000\u0000\u0000\n"+
		"\u0001\u0000\u0000\u0000\u0000\f\u0001\u0000\u0000\u0000\u0000\u000e\u0001"+
		"\u0000\u0000\u0000\u0000\u0010\u0001\u0000\u0000\u0000\u0000\u0012\u0001"+
		"\u0000\u0000\u0000\u0000\u0014\u0001\u0000\u0000\u0000\u0000\u0016\u0001"+
		"\u0000\u0000\u0000\u0000\u0018\u0001\u0000\u0000\u0000\u0000\u001a\u0001"+
		"\u0000\u0000\u0000\u0000\u001c\u0001\u0000\u0000\u0000\u0000\u001e\u0001"+
		"\u0000\u0000\u0000\u0000\"\u0001\u0000\u0000\u0000\u0000$\u0001\u0000"+
		"\u0000\u0000\u0000&\u0001\u0000\u0000\u0000\u0000(\u0001\u0000\u0000\u0000"+
		"\u0000*\u0001\u0000\u0000\u0000\u0000,\u0001\u0000\u0000\u0000\u0000."+
		"\u0001\u0000\u0000\u0000\u00000\u0001\u0000\u0000\u0000\u00002\u0001\u0000"+
		"\u0000\u0000\u00004\u0001\u0000\u0000\u0000\u00006\u0001\u0000\u0000\u0000"+
		"\u00008\u0001\u0000\u0000\u0000\u0000:\u0001\u0000\u0000\u0000\u0001<"+
		"\u0001\u0000\u0000\u0000\u0001>\u0001\u0000\u0000\u0000\u0001@\u0001\u0000"+
		"\u0000\u0000\u0001B\u0001\u0000\u0000\u0000\u0001D\u0001\u0000\u0000\u0000"+
		"\u0001F\u0001\u0000\u0000\u0000\u0001H\u0001\u0000\u0000\u0000\u0001J"+
		"\u0001\u0000\u0000\u0000\u0001L\u0001\u0000\u0000\u0000\u0001N\u0001\u0000"+
		"\u0000\u0000\u0001P\u0001\u0000\u0000\u0000\u0001R\u0001\u0000\u0000\u0000"+
		"\u0001T\u0001\u0000\u0000\u0000\u0001V\u0001\u0000\u0000\u0000\u0001X"+
		"\u0001\u0000\u0000\u0000\u0001Z\u0001\u0000\u0000\u0000\u0001\\\u0001"+
		"\u0000\u0000\u0000\u0001^\u0001\u0000\u0000\u0000\u0001`\u0001\u0000\u0000"+
		"\u0000\u0002b\u0001\u0000\u0000\u0000\u0004d\u0001\u0000\u0000\u0000\u0006"+
		"n\u0001\u0000\u0000\u0000\bz\u0001\u0000\u0000\u0000\n~\u0001\u0000\u0000"+
		"\u0000\f\u0084\u0001\u0000\u0000\u0000\u000e\u008c\u0001\u0000\u0000\u0000"+
		"\u0010\u0092\u0001\u0000\u0000\u0000\u0012\u0099\u0001\u0000\u0000\u0000"+
		"\u0014\u00a1\u0001\u0000\u0000\u0000\u0016\u00a6\u0001\u0000\u0000\u0000"+
		"\u0018\u00ad\u0001\u0000\u0000\u0000\u001a\u00b5\u0001\u0000\u0000\u0000"+
		"\u001c\u00b8\u0001\u0000\u0000\u0000\u001e\u00c6\u0001\u0000\u0000\u0000"+
		" \u00d9\u0001\u0000\u0000\u0000\"\u00dc\u0001\u0000\u0000\u0000$\u00e2"+
		"\u0001\u0000\u0000\u0000&\u00ec\u0001\u0000\u0000\u0000(\u00f7\u0001\u0000"+
		"\u0000\u0000*\u00fc\u0001\u0000\u0000\u0000,\u00ff\u0001\u0000\u0000\u0000"+
		".\u0101\u0001\u0000\u0000\u00000\u0109\u0001\u0000\u0000\u00002\u0117"+
		"\u0001\u0000\u0000\u00004\u011b\u0001\u0000\u0000\u00006\u0126\u0001\u0000"+
		"\u0000\u00008\u0128\u0001\u0000\u0000\u0000:\u012b\u0001\u0000\u0000\u0000"+
		"<\u0130\u0001\u0000\u0000\u0000>\u013f\u0001\u0000\u0000\u0000@\u0141"+
		"\u0001\u0000\u0000\u0000B\u0143\u0001\u0000\u0000\u0000D\u014c\u0001\u0000"+
		"\u0000\u0000F\u014e\u0001\u0000\u0000\u0000H\u0150\u0001\u0000\u0000\u0000"+
		"J\u0153\u0001\u0000\u0000\u0000L\u0158\u0001\u0000\u0000\u0000N\u0163"+
		"\u0001\u0000\u0000\u0000P\u0165\u0001\u0000\u0000\u0000R\u0167\u0001\u0000"+
		"\u0000\u0000T\u0169\u0001\u0000\u0000\u0000V\u016b\u0001\u0000\u0000\u0000"+
		"X\u0176\u0001\u0000\u0000\u0000Z\u017c\u0001\u0000\u0000\u0000\\\u017e"+
		"\u0001\u0000\u0000\u0000^\u018c\u0001\u0000\u0000\u0000`\u0190\u0001\u0000"+
		"\u0000\u0000bc\u0007\u0000\u0000\u0000c\u0003\u0001\u0000\u0000\u0000"+
		"de\u0005<\u0000\u0000ef\u0005f\u0000\u0000fg\u0005u\u0000\u0000gh\u0005"+
		"n\u0000\u0000hi\u0005c\u0000\u0000ij\u0005t\u0000\u0000jk\u0005i\u0000"+
		"\u0000kl\u0005o\u0000\u0000lm\u0005n\u0000\u0000m\u0005\u0001\u0000\u0000"+
		"\u0000no\u0005<\u0000\u0000op\u0005/\u0000\u0000pq\u0005f\u0000\u0000"+
		"qr\u0005u\u0000\u0000rs\u0005n\u0000\u0000st\u0005c\u0000\u0000tu\u0005"+
		"t\u0000\u0000uv\u0005i\u0000\u0000vw\u0005o\u0000\u0000wx\u0005n\u0000"+
		"\u0000xy\u0005>\u0000\u0000y\u0007\u0001\u0000\u0000\u0000z{\u0005<\u0000"+
		"\u0000{|\u0005i\u0000\u0000|}\u0005f\u0000\u0000}\t\u0001\u0000\u0000"+
		"\u0000~\u007f\u0005<\u0000\u0000\u007f\u0080\u0005/\u0000\u0000\u0080"+
		"\u0081\u0005i\u0000\u0000\u0081\u0082\u0005f\u0000\u0000\u0082\u0083\u0005"+
		">\u0000\u0000\u0083\u000b\u0001\u0000\u0000\u0000\u0084\u0085\u0005<\u0000"+
		"\u0000\u0085\u0086\u0005/\u0000\u0000\u0086\u0087\u0005e\u0000\u0000\u0087"+
		"\u0088\u0005l\u0000\u0000\u0088\u0089\u0005i\u0000\u0000\u0089\u008a\u0005"+
		"f\u0000\u0000\u008a\u008b\u0005>\u0000\u0000\u008b\r\u0001\u0000\u0000"+
		"\u0000\u008c\u008d\u0005<\u0000\u0000\u008d\u008e\u0005e\u0000\u0000\u008e"+
		"\u008f\u0005l\u0000\u0000\u008f\u0090\u0005i\u0000\u0000\u0090\u0091\u0005"+
		"f\u0000\u0000\u0091\u000f\u0001\u0000\u0000\u0000\u0092\u0093\u0005<\u0000"+
		"\u0000\u0093\u0094\u0005e\u0000\u0000\u0094\u0095\u0005l\u0000\u0000\u0095"+
		"\u0096\u0005s\u0000\u0000\u0096\u0097\u0005e\u0000\u0000\u0097\u0098\u0005"+
		">\u0000\u0000\u0098\u0011\u0001\u0000\u0000\u0000\u0099\u009a\u0005<\u0000"+
		"\u0000\u009a\u009b\u0005/\u0000\u0000\u009b\u009c\u0005e\u0000\u0000\u009c"+
		"\u009d\u0005l\u0000\u0000\u009d\u009e\u0005s\u0000\u0000\u009e\u009f\u0005"+
		"e\u0000\u0000\u009f\u00a0\u0005>\u0000\u0000\u00a0\u0013\u0001\u0000\u0000"+
		"\u0000\u00a1\u00a2\u0005<\u0000\u0000\u00a2\u00a3\u0005v\u0000\u0000\u00a3"+
		"\u00a4\u0005a\u0000\u0000\u00a4\u00a5\u0005r\u0000\u0000\u00a5\u0015\u0001"+
		"\u0000\u0000\u0000\u00a6\u00a7\u0005<\u0000\u0000\u00a7\u00a8\u0005/\u0000"+
		"\u0000\u00a8\u00a9\u0005v\u0000\u0000\u00a9\u00aa\u0005a\u0000\u0000\u00aa"+
		"\u00ab\u0005r\u0000\u0000\u00ab\u00ac\u0005>\u0000\u0000\u00ac\u0017\u0001"+
		"\u0000\u0000\u0000\u00ad\u00ae\u0005t\u0000\u0000\u00ae\u00af\u0005y\u0000"+
		"\u0000\u00af\u00b0\u0005p\u0000\u0000\u00b0\u00b1\u0005e\u0000\u0000\u00b1"+
		"\u00b2\u0005=\u0000\u0000\u00b2\u00b3\u0001\u0000\u0000\u0000\u00b3\u00b4"+
		"\u0003 \u000f\u0000\u00b4\u0019\u0001\u0000\u0000\u0000\u00b5\u00b6\u0003"+
		"\u0014\t\u0000\u00b6\u00b7\u0003 \u000f\u0000\u00b7\u001b\u0001\u0000"+
		"\u0000\u0000\u00b8\u00b9\u0005/\u0000\u0000\u00b9\u00ba\u0005*\u0000\u0000"+
		"\u00ba\u00be\u0001\u0000\u0000\u0000\u00bb\u00bd\t\u0000\u0000\u0000\u00bc"+
		"\u00bb\u0001\u0000\u0000\u0000\u00bd\u00c0\u0001\u0000\u0000\u0000\u00be"+
		"\u00bf\u0001\u0000\u0000\u0000\u00be\u00bc\u0001\u0000\u0000\u0000\u00bf"+
		"\u00c1\u0001\u0000\u0000\u0000\u00c0\u00be\u0001\u0000\u0000\u0000\u00c1"+
		"\u00c2\u0005*\u0000\u0000\u00c2\u00c3\u0005/\u0000\u0000\u00c3\u00c4\u0001"+
		"\u0000\u0000\u0000\u00c4\u00c5\u0006\r\u0000\u0000\u00c5\u001d\u0001\u0000"+
		"\u0000\u0000\u00c6\u00c7\u0005/\u0000\u0000\u00c7\u00c8\u0005/\u0000\u0000"+
		"\u00c8\u00cc\u0001\u0000\u0000\u0000\u00c9\u00cb\b\u0001\u0000\u0000\u00ca"+
		"\u00c9\u0001\u0000\u0000\u0000\u00cb\u00ce\u0001\u0000\u0000\u0000\u00cc"+
		"\u00ca\u0001\u0000\u0000\u0000\u00cc\u00cd\u0001\u0000\u0000\u0000\u00cd"+
		"\u00cf\u0001\u0000\u0000\u0000\u00ce\u00cc\u0001\u0000\u0000\u0000\u00cf"+
		"\u00d0\u0006\u000e\u0000\u0000\u00d0\u001f\u0001\u0000\u0000\u0000\u00d1"+
		"\u00d5\u0007\u0002\u0000\u0000\u00d2\u00d4\u0007\u0003\u0000\u0000\u00d3"+
		"\u00d2\u0001\u0000\u0000\u0000\u00d4\u00d7\u0001\u0000\u0000\u0000\u00d5"+
		"\u00d3\u0001\u0000\u0000\u0000\u00d5\u00d6\u0001\u0000\u0000\u0000\u00d6"+
		"\u00da\u0001\u0000\u0000\u0000\u00d7\u00d5\u0001\u0000\u0000\u0000\u00d8"+
		"\u00da\u0007\u0004\u0000\u0000\u00d9\u00d1\u0001\u0000\u0000\u0000\u00d9"+
		"\u00d8\u0001\u0000\u0000\u0000\u00da!\u0001\u0000\u0000\u0000\u00db\u00dd"+
		"\u0007\u0005\u0000\u0000\u00dc\u00db\u0001\u0000\u0000\u0000\u00dd\u00de"+
		"\u0001\u0000\u0000\u0000\u00de\u00dc\u0001\u0000\u0000\u0000\u00de\u00df"+
		"\u0001\u0000\u0000\u0000\u00df\u00e0\u0001\u0000\u0000\u0000\u00e0\u00e1"+
		"\u0006\u0010\u0000\u0000\u00e1#\u0001\u0000\u0000\u0000\u00e2\u00e3\u0005"+
		"<\u0000\u0000\u00e3\u00e4\u0005p\u0000\u0000\u00e4\u00e5\u0005r\u0000"+
		"\u0000\u00e5\u00e6\u0005o\u0000\u0000\u00e6\u00e7\u0005g\u0000\u0000\u00e7"+
		"\u00e8\u0005r\u0000\u0000\u00e8\u00e9\u0005a\u0000\u0000\u00e9\u00ea\u0005"+
		"m\u0000\u0000\u00ea\u00eb\u0005>\u0000\u0000\u00eb%\u0001\u0000\u0000"+
		"\u0000\u00ec\u00ed\u0005<\u0000\u0000\u00ed\u00ee\u0005/\u0000\u0000\u00ee"+
		"\u00ef\u0005p\u0000\u0000\u00ef\u00f0\u0005r\u0000\u0000\u00f0\u00f1\u0005"+
		"o\u0000\u0000\u00f1\u00f2\u0005g\u0000\u0000\u00f2\u00f3\u0005r\u0000"+
		"\u0000\u00f3\u00f4\u0005a\u0000\u0000\u00f4\u00f5\u0005m\u0000\u0000\u00f5"+
		"\u00f6\u0005>\u0000\u0000\u00f6\'\u0001\u0000\u0000\u0000\u00f7\u00f8"+
		"\u0005<\u0000\u0000\u00f8\u00f9\u0005/\u0000\u0000\u00f9\u00fa\u0001\u0000"+
		"\u0000\u0000\u00fa\u00fb\u0003 \u000f\u0000\u00fb)\u0001\u0000\u0000\u0000"+
		"\u00fc\u00fd\u0005<\u0000\u0000\u00fd\u00fe\u0003 \u000f\u0000\u00fe+"+
		"\u0001\u0000\u0000\u0000\u00ff\u0100\u0003 \u000f\u0000\u0100-\u0001\u0000"+
		"\u0000\u0000\u0101\u0102\u0005n\u0000\u0000\u0102\u0103\u0005a\u0000\u0000"+
		"\u0103\u0104\u0005m\u0000\u0000\u0104\u0105\u0005e\u0000\u0000\u0105\u0106"+
		"\u0005=\u0000\u0000\u0106\u0107\u0001\u0000\u0000\u0000\u0107\u0108\u0003"+
		" \u000f\u0000\u0108/\u0001\u0000\u0000\u0000\u0109\u010a\u0005r\u0000"+
		"\u0000\u010a\u010b\u0005e\u0000\u0000\u010b\u010c\u0005t\u0000\u0000\u010c"+
		"\u010d\u0005u\u0000\u0000\u010d\u010e\u0005r\u0000\u0000\u010e\u010f\u0005"+
		"n\u0000\u0000\u010f\u0110\u0005T\u0000\u0000\u0110\u0111\u0005y\u0000"+
		"\u0000\u0111\u0112\u0005p\u0000\u0000\u0112\u0113\u0005e\u0000\u0000\u0113"+
		"\u0114\u0005=\u0000\u0000\u0114\u0115\u0001\u0000\u0000\u0000\u0115\u0116"+
		"\u0003 \u000f\u0000\u01161\u0001\u0000\u0000\u0000\u0117\u0118\u0003 "+
		"\u000f\u0000\u0118\u0119\u0005:\u0000\u0000\u0119\u011a\u0003 \u000f\u0000"+
		"\u011a3\u0001\u0000\u0000\u0000\u011b\u011c\u0005c\u0000\u0000\u011c\u011d"+
		"\u0005o\u0000\u0000\u011d\u011e\u0005n\u0000\u0000\u011e\u011f\u0005d"+
		"\u0000\u0000\u011f\u0120\u0005i\u0000\u0000\u0120\u0121\u0005t\u0000\u0000"+
		"\u0121\u0122\u0005i\u0000\u0000\u0122\u0123\u0005o\u0000\u0000\u0123\u0124"+
		"\u0005n\u0000\u0000\u0124\u0125\u0005=\u0000\u0000\u01255\u0001\u0000"+
		"\u0000\u0000\u0126\u0127\u0005>\u0000\u0000\u01277\u0001\u0000\u0000\u0000"+
		"\u0128\u0129\u0003 \u000f\u0000\u0129\u012a\u0005=\u0000\u0000\u012a9"+
		"\u0001\u0000\u0000\u0000\u012b\u012c\u0005{\u0000\u0000\u012c\u012d\u0001"+
		"\u0000\u0000\u0000\u012d\u012e\u0006\u001c\u0001\u0000\u012e;\u0001\u0000"+
		"\u0000\u0000\u012f\u0131\u0007\u0005\u0000\u0000\u0130\u012f\u0001\u0000"+
		"\u0000\u0000\u0131\u0132\u0001\u0000\u0000\u0000\u0132\u0130\u0001\u0000"+
		"\u0000\u0000\u0132\u0133\u0001\u0000\u0000\u0000\u0133\u0134\u0001\u0000"+
		"\u0000\u0000\u0134\u0135\u0006\u001d\u0000\u0000\u0135=\u0001\u0000\u0000"+
		"\u0000\u0136\u0137\u0005F\u0000\u0000\u0137\u0138\u0005a\u0000\u0000\u0138"+
		"\u0139\u0005l\u0000\u0000\u0139\u013a\u0005s\u0000\u0000\u013a\u0140\u0005"+
		"e\u0000\u0000\u013b\u013c\u0005T\u0000\u0000\u013c\u013d\u0005r\u0000"+
		"\u0000\u013d\u013e\u0005u\u0000\u0000\u013e\u0140\u0005e\u0000\u0000\u013f"+
		"\u0136\u0001\u0000\u0000\u0000\u013f\u013b\u0001\u0000\u0000\u0000\u0140"+
		"?\u0001\u0000\u0000\u0000\u0141\u0142\u0003 \u000f\u0000\u0142A\u0001"+
		"\u0000\u0000\u0000\u0143\u0147\u0005\"\u0000\u0000\u0144\u0146\t\u0000"+
		"\u0000\u0000\u0145\u0144\u0001\u0000\u0000\u0000\u0146\u0149\u0001\u0000"+
		"\u0000\u0000\u0147\u0148\u0001\u0000\u0000\u0000\u0147\u0145\u0001\u0000"+
		"\u0000\u0000\u0148\u014a\u0001\u0000\u0000\u0000\u0149\u0147\u0001\u0000"+
		"\u0000\u0000\u014a\u014b\u0005\"\u0000\u0000\u014bC\u0001\u0000\u0000"+
		"\u0000\u014c\u014d\u0005:\u0000\u0000\u014dE\u0001\u0000\u0000\u0000\u014e"+
		"\u014f\u0005(\u0000\u0000\u014fG\u0001\u0000\u0000\u0000\u0150\u0151\u0005"+
		")\u0000\u0000\u0151I\u0001\u0000\u0000\u0000\u0152\u0154\u0003\u0002\u0000"+
		"\u0000\u0153\u0152\u0001\u0000\u0000\u0000\u0154\u0155\u0001\u0000\u0000"+
		"\u0000\u0155\u0153\u0001\u0000\u0000\u0000\u0155\u0156\u0001\u0000\u0000"+
		"\u0000\u0156K\u0001\u0000\u0000\u0000\u0157\u0159\u0003\u0002\u0000\u0000"+
		"\u0158\u0157\u0001\u0000\u0000\u0000\u0159\u015a\u0001\u0000\u0000\u0000"+
		"\u015a\u0158\u0001\u0000\u0000\u0000\u015a\u015b\u0001\u0000\u0000\u0000"+
		"\u015b\u015c\u0001\u0000\u0000\u0000\u015c\u0160\u0005.\u0000\u0000\u015d"+
		"\u015f\u0003\u0002\u0000\u0000\u015e\u015d\u0001\u0000\u0000\u0000\u015f"+
		"\u0162\u0001\u0000\u0000\u0000\u0160\u015e\u0001\u0000\u0000\u0000\u0160"+
		"\u0161\u0001\u0000\u0000\u0000\u0161M\u0001\u0000\u0000\u0000\u0162\u0160"+
		"\u0001\u0000\u0000\u0000\u0163\u0164\u0005=\u0000\u0000\u0164O\u0001\u0000"+
		"\u0000\u0000\u0165\u0166\u0005*\u0000\u0000\u0166Q\u0001\u0000\u0000\u0000"+
		"\u0167\u0168\u0005/\u0000\u0000\u0168S\u0001\u0000\u0000\u0000\u0169\u016a"+
		"\u0005+\u0000\u0000\u016aU\u0001\u0000\u0000\u0000\u016b\u016c\u0005-"+
		"\u0000\u0000\u016cW\u0001\u0000\u0000\u0000\u016d\u016e\u0005=\u0000\u0000"+
		"\u016e\u0177\u0005=\u0000\u0000\u016f\u0170\u0005!\u0000\u0000\u0170\u0177"+
		"\u0005=\u0000\u0000\u0171\u0172\u0005>\u0000\u0000\u0172\u0177\u0005="+
		"\u0000\u0000\u0173\u0177\u0007\u0006\u0000\u0000\u0174\u0175\u0005<\u0000"+
		"\u0000\u0175\u0177\u0005=\u0000\u0000\u0176\u016d\u0001\u0000\u0000\u0000"+
		"\u0176\u016f\u0001\u0000\u0000\u0000\u0176\u0171\u0001\u0000\u0000\u0000"+
		"\u0176\u0173\u0001\u0000\u0000\u0000\u0176\u0174\u0001\u0000\u0000\u0000"+
		"\u0177Y\u0001\u0000\u0000\u0000\u0178\u0179\u0005&\u0000\u0000\u0179\u017d"+
		"\u0005&\u0000\u0000\u017a\u017b\u0005|\u0000\u0000\u017b\u017d\u0005|"+
		"\u0000\u0000\u017c\u0178\u0001\u0000\u0000\u0000\u017c\u017a\u0001\u0000"+
		"\u0000\u0000\u017d[\u0001\u0000\u0000\u0000\u017e\u017f\u0005/\u0000\u0000"+
		"\u017f\u0180\u0005*\u0000\u0000\u0180\u0184\u0001\u0000\u0000\u0000\u0181"+
		"\u0183\t\u0000\u0000\u0000\u0182\u0181\u0001\u0000\u0000\u0000\u0183\u0186"+
		"\u0001\u0000\u0000\u0000\u0184\u0185\u0001\u0000\u0000\u0000\u0184\u0182"+
		"\u0001\u0000\u0000\u0000\u0185\u0187\u0001\u0000\u0000\u0000\u0186\u0184"+
		"\u0001\u0000\u0000\u0000\u0187\u0188\u0005*\u0000\u0000\u0188\u0189\u0005"+
		"/\u0000\u0000\u0189\u018a\u0001\u0000\u0000\u0000\u018a\u018b\u0006-\u0000"+
		"\u0000\u018b]\u0001\u0000\u0000\u0000\u018c\u018d\u0005}\u0000\u0000\u018d"+
		"\u018e\u0001\u0000\u0000\u0000\u018e\u018f\u0006.\u0002\u0000\u018f_\u0001"+
		"\u0000\u0000\u0000\u0190\u0191\u0005/\u0000\u0000\u0191\u0192\u0005/\u0000"+
		"\u0000\u0192\u0196\u0001\u0000\u0000\u0000\u0193\u0195\b\u0001\u0000\u0000"+
		"\u0194\u0193\u0001\u0000\u0000\u0000\u0195\u0198\u0001\u0000\u0000\u0000"+
		"\u0196\u0194\u0001\u0000\u0000\u0000\u0196\u0197\u0001\u0000\u0000\u0000"+
		"\u0197\u0199\u0001\u0000\u0000\u0000\u0198\u0196\u0001\u0000\u0000\u0000"+
		"\u0199\u019a\u0006/\u0000\u0000\u019aa\u0001\u0000\u0000\u0000\u0011\u0000"+
		"\u0001\u00be\u00cc\u00d5\u00d9\u00de\u0132\u013f\u0147\u0155\u015a\u0160"+
		"\u0176\u017c\u0184\u0196\u0003\u0006\u0000\u0000\u0005\u0001\u0000\u0005"+
		"\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}