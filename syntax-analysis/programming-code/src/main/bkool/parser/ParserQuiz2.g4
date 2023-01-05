grammar ParserQuiz2;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program : program_int
  ;

program_int
  : (funcdecl | vardecl) program_int
  | (funcdecl | vardecl)
  ;

vardecl
  : TYPE identifiers SEMICOLON
  ;

// parser rule is a combination of token
funcdecl
  : TYPE func_name LB func_args? RB body
  ;

body
  : 'body'
  ;

identifiers
  : ID COMMA identifiers
  | ID
  ;

func_args
  : vardecl func_args
  | TYPE identifiers
  ;

func_name
  : ID
  ;

TYPE
  : (INT | FLOAT)
  ;

ID
  : [a-zA-Z]+
  ;

INT
  : 'int'
  ;

FLOAT
  : 'float'
  ;

COMMA
  : ','
  ;

SEMICOLON
  : ';'
  ;

LB
  : '('
  ;

RB
  : ')'
  ;

WS
  : [ \t\r\n] -> skip
  ;

ERROR_CHAR
  : . 
    {
      raise ErrorToken(self.text)
    }
  ;
