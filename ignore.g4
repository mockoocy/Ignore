grammar ignore;

fragment DIGIT: [0-9];

LITERAL_BOOL: 'false' | 'true';
LITERAL_INT: DIGIT+;
LITERAL_FLOAT: DIGIT+ '.' DIGIT*;

LITERAL_STRING: '"' .* '"';

OPERATOR_ARITHMETIC: ('*' | '-' | '+' | '/' | '==' | '!=');
OPERATOR_LOGIC: ('&&' | '||');

ID: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\n\r]+ -> skip;
OPEN_PROGRAM: '<program>';
CLOSE_PROGRAM: '</program>';

literalNumeric: (LITERAL_INT | LITERAL_FLOAT);
literal:
	LITERAL_INT
	| LITERAL_FLOAT
	| LITERAL_STRING
	| LITERAL_BOOL;

// TU SĄ TOKENY!!!!!!!!!!!!!!!!!!!!!!!! TOKENY NA GÓRZE A STARA JAKUBA SPOCEŃCA KULTURALNEGO POD
// STOŁEM (ROBI MI LODA) <3

program: OPEN_PROGRAM block CLOSE_PROGRAM EOF;
block: statement+; //block ma zero lub wiecej statementów
keyword: ioStmt | varDecl;
statement: keyword | expr;
OPEN_IO: '<io>';
CLOSE_IO: '</io>';
//expr : LITERAL_INT | LITERAL_FLOAT | ID | expr OPERATOR_ARITHMETIC expr | expr OPERATOR_LOGIC expr | expr (OPERATOR) expr | '(' expr ')'; //

function_call: ID '(' (expr | literal) ')' | ID '()';
expr:
	'(' expr ')'
	| ID
	| literal
	| function_call
	| expr '*' expr
	| expr '+' expr
	// | expr (OPERATOR_ARITHMETIC) expr
	| expr OPERATOR_LOGIC expr;

//IF_TAG: '<if>'; ENDIF_TAG: '</if>';

//function : ID'('  ')';
varDecl:
	'<var' 'name' '=' LITERAL_STRING 'type' '=' type '>' expr '</var>';

ioStmt: OPEN_IO expr CLOSE_IO;
type: 'number'; // mozna pozniej dodac | 'string' | 'bool' ;
string_expr: LITERAL_STRING | expr;

/*
 
 >>>> condition: expression OPERATOR_LOGIC expression | expression;
 control_statement:
 'if' '('
 condition ')' statement (
 'else if' '(' condition ')' statement
 )* 'else' statement
 | 'if' '('
 condition ')' statement;
 */