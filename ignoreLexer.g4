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

FUNCTION_TAG_OPEN: '<function';
FUNCTION_TAG_END: '</function>';

NAME_EQ: 'name=';
RETURN_TYPE_EQ: 'returnType=';
CONDITION_EQ: 'condition=';
IF_TAG: '<if';
IF_END: '</if>';
ELIF_END: '</elif>';
ELIF_TAG: '<elif';
ELSE: '<else>';
ELSE_END: '</else>';

// TAGI
OPEN_TAG: '<' ID;
CLOSE_TAG: '</';
END_TAG: '>';

LITERAL_STRING: '"' .*? '"'; // .*? "c"

fragment ID: [a-zA-Z_][a-zA-Z0-9_]*;
NAME: ID;
WS: [ \t\n\r]+ -> skip;
OPEN_PROGRAM: '<program>';
CLOSE_PROGRAM: '</program>';

// OPERATORY
EQUALS: '=';
MUL: '*';
DIV: '/';
ADD: '+';
SUB: '-';

OPERATOR_COMPARE: ( '==' | '!=' | '>=' | '>' | '<' | '<=');
OPERATOR_LOGIC: ('&&' | '||');