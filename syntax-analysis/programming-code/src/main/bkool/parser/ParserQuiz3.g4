grammar ParserQuiz3;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program : program_int EOF
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
  : LCB body_stats RCB
  ;

body_stats
  : (vardecl | stats) body_stats
  | (vardecl | stats)
  ;

stats
  : (assign_stat | call_stat | return_stat) SEMICOLON
  ;

assign_stat
  : ID EQUAL expr
  ;

call_stat
  : ID LB call_stat_exprs RB
  ;

call_stat_exprs
  : expr COMMA call_stat_exprs
  | expr
  ;

return_stat
  : RETURN expr
  ;

expr
  : 'expr'
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

RETURN
  : 'return'
  ;

INT
  : 'int'
  ;

FLOAT
  : 'float'
  ;

ID
  : [a-zA-Z_] [a-zA-Z0-9_]*
  ;

EQUAL
  : '='
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

LCB
  : '{'
  ;

RCB
  : '}'
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
