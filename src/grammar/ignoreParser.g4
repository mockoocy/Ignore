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
statement: block | wrapped_expr;
property: PROPERTY_NAME (wrapped_expr | TAG_REFERENCE);
endTag: CLOSE_TAG END_TAG;
startTag: OPEN_TAG END_TAG | OPEN_TAG (property)+ END_TAG;
block:
	startTag wrapped_expr endTag
	| wrapped_expr
	| function
	| control_statement;

functionCall:
	NAME OPEN_PAREN (expr | literal) CLOSE_PAREN
	| NAME OPEN_PAREN CLOSE_PAREN;

// paramName: type. Could change to NAME : NAME = literal for default values of params.
functionStart:
	FUNCTION_TAG_OPEN FUNCTION_NAME (FUNCTION_PARAM)* FUNCTION_RET_TYPE END_TAG;
function: functionStart block* FUNCTION_TAG_END;

condition: expr OPERATOR_LOGIC expr | expr | LITERAL_BOOL;
if:
	IF_TAG CONDITION_EQ OPEN_CURLY (condition) CLOSE_CURLY END_TAG;

if_statement: if statement IF_END;
elif:
	ELIF_TAG CONDITION_EQ OPEN_CURLY (condition) CLOSE_CURLY END_TAG;
elif_statement: elif statement ELIF_END;
else_statement: ELSE statement ELSE_END;

control_statement:
	if_statement (elif_statement)* (else_statement)?;
expr:
	OPEN_PAREN expr CLOSE_PAREN
	| literal
	| functionCall
	| expr (MUL | DIV) expr
	| expr (ADD | SUB) expr
	| expr (OPERATOR_COMPARE) expr
	| expr (OPERATOR_LOGIC) expr
	| NAME;
wrapped_expr: OPEN_CURLY expr CLOSE_CURLY;