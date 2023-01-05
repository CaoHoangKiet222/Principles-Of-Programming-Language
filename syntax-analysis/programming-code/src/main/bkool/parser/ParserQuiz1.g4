grammar ParserQuiz1;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program : decl
  ;

decl
  : (vardecl | funcdecl) decl
  | (vardecl | funcdecl)
  ;

vardecl
  : 'vardecl' 
  ;

funcdecl
  : 'funcdecl' 
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

