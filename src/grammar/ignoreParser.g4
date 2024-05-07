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



functionCall:
	NAME OPEN_PAREN (expr | literal) CLOSE_PAREN
	| NAME OPEN_PAREN CLOSE_PAREN;

// paramName: type. Could change to NAME : NAME = literal for default values of params.
functionStart:
	FUNCTION_TAG_OPEN FUNCTION_NAME (FUNCTION_PARAM)* FUNCTION_RET_TYPE END_TAG;
function: functionStart block* FUNCTION_TAG_END;


varDecl: VAR_DECL FUNCTION_NAME (VAR_DECL_TYPE)? END_TAG;
var: varDecl wrapped_expr VAR_DECL_END; 
var_assign: PROPERTY_NAME wrapped_expr;
while_loop: WHILE_TAG loop_condition END_TAG block WHILE_END;
for_loop: FOR_TAG (var)? loop_condition (var_assign)? END_TAG block FOR_END;

loop_condition: CONDITION_EQ OPEN_CURLY (condition) CLOSE_CURLY;



condition: expr | LITERAL_BOOL;
if:
	IF_TAG CONDITION_EQ OPEN_CURLY (condition) CLOSE_CURLY END_TAG;

if_statement: if block IF_END;
elif:
	ELIF_TAG CONDITION_EQ OPEN_CURLY (condition) CLOSE_CURLY END_TAG;
elif_statement: elif block ELIF_END;
else_statement: ELSE block ELSE_END;

control_statement:
	if_statement (elif_statement)* (else_statement)?;


program: (function)* OPEN_PROGRAM (block| var)* CLOSE_PROGRAM (
		function
	)* EOF;
property: PROPERTY_NAME (wrapped_expr | TAG_REFERENCE);
endTag: CLOSE_TAG END_TAG;
startTag: OPEN_TAG END_TAG | OPEN_TAG (property)+ END_TAG;
statement:
	startTag wrapped_expr endTag
	| wrapped_expr
	| function
	| control_statement
	| var
	| var_assign
	| for_loop
	| while_loop;
block: (statement)+;

expr:
	OPEN_PAREN expr CLOSE_PAREN
	| literal
	| functionCall
	| NOT expr
	| expr (MUL | DIV | MOD | INT_DIV) expr
	| expr (ADD | SUB) expr
	| expr (OPERATOR_COMPARE) expr
	| expr (OPERATOR_LOGIC) expr
	| NAME;
wrapped_expr: OPEN_CURLY expr CLOSE_CURLY;