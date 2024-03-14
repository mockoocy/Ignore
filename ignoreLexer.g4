lexer grammar ignoreLexer;

fragment DIGIT: [0-9];

COLON: ':';

OPEN_PAREN: '(';
CLOSE_PAREN: ')';

OPEN_CURLY: '{';
CLOSE_CURLY: '}';

LITERAL_BOOL: 'false' | 'true';
LITERAL_INT: DIGIT+;
LITERAL_FLOAT: DIGIT+ '.' DIGIT*;

LITERAL_STRING: '"' .*? '"'; // .*? "c"

OPERATOR_ARITHMETIC: (
		' * '
		| ' - '
		| ' + '
		| ' / '
		| ' == '
		| ' != '
		| ' >= '
		| ' > '
		| ' < '
		| ' <= '
	);
OPERATOR_LOGIC: (' && ' | ' || ');

fragment ID: [a-zA-Z_][a-zA-Z0-9_]*;
NAME: ID;
WS: [ \t\n\r]+ -> skip;
OPEN_PROGRAM: '<program>';
CLOSE_PROGRAM: '</program>';

NAME_EQ: 'name=';
RETURN_TYPE_EQ: 'returnType=';
CONDITION_EQ: 'condition=';
IF_TAG: '<if';
IF_END: '</if>';
ELIF_END: '</elif>';
ELIF_TAG: '<if';
ELSE: '<else>';
ELSE_END: '</else>';

CONDITION_START: 'condition=';

// OPERATORY
EQUALS: '=';
MUL: '*';
DIV: '/';
ADD: '+';
SUB: '-';

// TAGI
OPEN_TAG: '<';
CLOSE_TAG: '</';
END_TAG: '>';

FUNCTION_TAG_OPEN: '<function';
FUNCTION_TAG_END: '</function>';