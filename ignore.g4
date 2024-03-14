grammar ignore;
fragment DIGIT: [0-9];

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

COMMENT: '/*' .*? '*/' -> skip;

LINE_COMMENT: '//' ~[\r\n]* -> skip;

fragment ID: [a-zA-Z_][a-zA-Z0-9_]*;
NAME: ID;
WS: [ \t\n\r]+ -> skip;
OPEN_PROGRAM: '<program>';
CLOSE_PROGRAM: '</program>';
literalNumeric: (LITERAL_INT | LITERAL_FLOAT);
literal:
	LITERAL_INT
	| LITERAL_FLOAT
	| LITERAL_STRING
	| LITERAL_BOOL;

program: (function)* OPEN_PROGRAM (block)* CLOSE_PROGRAM (
		function
	)* EOF;
statement: block | expr;
property: NAME '=' ('{' expr '}' | NAME);
openTag: '<' NAME;
startTag: openTag (property)* '>';
endTag: '</' NAME '>';
block: startTag expr endTag | function | control_statement;

//expr : LITERAL_INT | LITERAL_FLOAT | NAME | expr OPERATOR_ARITHMETIC expr | expr OPERATOR_LOGIC expr | expr (OPERATOR) expr | '(' expr ')'; //

functionCall: NAME '(' (expr | literal) ')' | NAME '()';

functionParam: NAME ':' NAME;
// paramName: type. Could change to NAME : NAME = literal for default values of params.
functionName: 'name=' NAME;
functionReturnType: 'returnType=' NAME;
functionStart:
	'<function' functionName (functionParam)* functionReturnType '>';
functionEnd: '</function>';
function: functionStart block* functionEnd;

condition: expr OPERATOR_LOGIC expr | expr | LITERAL_BOOL;
if: '<if' 'condition=' '{' (condition) '}' '>';
IF_END: '</if>';
if_statement: if statement IF_END;
elif: '<elif condition={' (condition) '} >';
ELIF_END: '</elif>';
elif_statement: elif statement ELIF_END;
else: '<else>';
ELSE_END: '</else>';
else_statement: else statement ELSE_END;

control_statement:
	if_statement (elif_statement)* (else_statement)?;
expr:
	'(' expr ')'
	| NAME
	| literal
	| functionCall
	| expr '*' expr
	| expr '+' expr
	| expr (OPERATOR_ARITHMETIC) expr
	| expr OPERATOR_LOGIC expr;

type: 'number'; // mozna pozniej dodac | 'string' | 'bool' ;
string_expr: LITERAL_STRING | expr;