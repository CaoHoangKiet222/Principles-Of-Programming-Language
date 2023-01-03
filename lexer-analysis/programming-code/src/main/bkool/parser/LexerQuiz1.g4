lexer grammar LexerQuiz1;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

ERROR_FIRST_CHAR 
  : [0-9]
    {
      raise ErrorToken(self.text[0])  
    }
  ;

INIT 
  : FIRST_LETTER CONTINUE_CHARACTERS* 
  ;

/* doesn't make this a token when compile*/
fragment 
FIRST_LETTER 
  : [a-z] 
  ;

fragment 
CONTINUE_CHARACTERS 
  : [a-z0-9] 
  ;

WS : [ \t\r\n]+ -> skip ;

NOT_ALPHANUMERIC 
  : ~[a-z0-9]
    {
      raise ErrorToken(self.text[0])
    }
  ;

