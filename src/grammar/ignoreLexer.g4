lexer grammar ignoreLexer;

fragment DIGIT: [0-9];
fragment NEGATIVE_SIGN: '-';


FUNCTION_TAG_OPEN: '<function';
FUNCTION_TAG_END: '</function>';

IF_TAG: '<if';
IF_END: '</if>';
ELIF_END: '</elif>';
ELIF_TAG: '<elif';
ELSE: '<else>';
ELSE_END: '</else>';
VAR_DECL_START: '<var';
VAR_DECL_END: '</var>';
VAR_DECL_TYPE: 'type=' ID;
VAR_DECL: VAR_DECL_START ID;

COMMENT: '/*' .*? '*/' -> skip;

LINE_COMMENT: '//' ~[\r\n]* -> skip;

// IT IS VERY IMPORTANT TO USE \pEmojiPresentation=EmojiDefault instead of \p{Emoji} the latter
// matches numerous unwanted characters like '*' or digits, while the first one matches only the
// ones with have "colorful emoji presentation".
fragment ID: ([a-zA-Z] [a-zA-Z0-9_]*)
	| [\p{EmojiPresentation=EmojiDefault} ];
WS: [ \t\n\r]+ -> skip;
OPEN_PROGRAM: '<program>';
CLOSE_PROGRAM: '</program>';

// OPERATORY

// TAGI
CLOSE_TAG: '</' ID;
OPEN_TAG: '<' ID;
TAG_REFERENCE: ID;
FUNCTION_NAME: 'name=' ID;
FUNCTION_RET_TYPE: 'returnType=' ID;
FUNCTION_PARAM: ID ':' ID;
CONDITION_EQ: 'condition=';
END_TAG: '>';
PROPERTY_NAME: ID '=';

OPEN_CURLY: '{' -> pushMode(expr);
mode expr;
EXPR_WS: [ \t\n\r]+ -> skip;
LITERAL_BOOL: 'False' | 'True';
NAME: ID;

LITERAL_STRING: '"' .*? '"'; // .*? "c"
COLON: ':';

OPEN_PAREN: '(';
CLOSE_PAREN: ')';

LITERAL_INT: NEGATIVE_SIGN?DIGIT+;
LITERAL_FLOAT: NEGATIVE_SIGN? DIGIT+ '.' DIGIT*;

EQUALS: '=';
MUL: '*';
DIV: '/';
ADD: '+';
SUB: '-';
MOD: '%';
INT_DIV: '//';

OPERATOR_COMPARE: ( '==' | '!=' | '>=' | '>' | '<' | '<=');
OPERATOR_LOGIC: ('&&' | '||');

EXPR_COMMENT: '/*' .*? '*/' -> skip;

CLOSE_CURLY: '}' -> pushMode(DEFAULT_MODE);
EXPR_LINE_COMMENT: '//' ~[\r\n]* -> skip;