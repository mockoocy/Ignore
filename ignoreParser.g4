parser grammar ignoreParser;

options {
	tokenVocab = ignoreLexer;
}

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
property: NAME EQUALS (OPEN_CURLY expr CLOSE_CURLY | NAME);
openTag: OPEN_TAG NAME;
endTag: CLOSE_TAG NAME END_TAG;
startTag: openTag (property)* END_TAG;
block: startTag expr endTag | function | control_statement;

//expr : LITERAL_INT | LITERAL_FLOAT | NAME | expr OPERATOR_ARITHMETIC expr | expr OPERATOR_LOGIC expr | expr (OPERATOR) expr | '(' expr ')'; //

functionCall:
	NAME OPEN_PAREN (expr | literal) CLOSE_PAREN
	| NAME OPEN_PAREN CLOSE_PAREN;

functionParam: NAME COLON NAME;
// paramName: type. Could change to NAME : NAME = literal for default values of params.
functionName: NAME_EQ NAME;
functionReturnType: RETURN_TYPE_EQ NAME;
functionStart:
	FUNCTION_TAG_OPEN functionName (functionParam)* functionReturnType END_TAG;
function: functionStart block* FUNCTION_TAG_END;

condition: expr OPERATOR_LOGIC expr | expr | LITERAL_BOOL;
if:
	IF_TAG CONDITION_EQ OPEN_CURLY (condition) CLOSE_CURLY END_TAG;

if_statement: if statement IF_END;
elif:
	ELIF_TAG CONDITION_START OPEN_CURLY (condition) CLOSE_CURLY END_TAG;
elif_statement: elif statement ELIF_END;
else_statement: ELSE statement ELSE_END;

control_statement:
	if_statement (elif_statement)* (else_statement)?;
expr:
	OPEN_PAREN expr CLOSE_PAREN
	| NAME
	| literal
	| functionCall
	| expr (MUL | DIV) expr
	| expr (ADD | SUB) expr
	| expr (OPERATOR_ARITHMETIC) expr
	| expr OPERATOR_LOGIC expr;

string_expr: LITERAL_STRING | expr;