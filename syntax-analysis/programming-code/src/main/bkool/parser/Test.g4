grammar Test;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program
  : declare 
  ;

declare
  : (funcdecl | vardecl) declare 
  | (funcdecl | vardecl)
  ; 

vardecl
  : TYPE variables SEMICOLON
  ;

funcdecl
  : TYPE FUNCTION_NAME LB function_params? RB body
  ;

body: 'body';

variables
  : ID COMMA variables
  | ID
  ;

function_params
  : vardecl function_params
  | TYPE variables
  ;

TYPE: (INT_TYPE | FLOAT_TYPE) ;

fragment INT_TYPE
  : 'int' 
  ;

fragment FLOAT_TYPE
  : 'float' 
  ;

SEMICOLON
  : ';' 
  ;

COMMA
  : ',' 
  ;

ID: [a-z];

FUNCTION_NAME
  : ID+
  ;

LB: '(';

RB: ')';

WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};
