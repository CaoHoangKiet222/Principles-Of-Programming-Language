grammar LexerQuiz4;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program : ;

BKNetID_INIT
  : FIRST_NAME DOT LAST_NAME OPTIONAL_STR
  ;

fragment FIRST_NAME
  : LOWERCASE_LETTER+
  ;

fragment LAST_NAME
  : LOWERCASE_LETTER+
  ;

fragment OPTIONAL_STR
  : (DOT | CHAR | UNDERSCORE)* (CHAR | UNDERSCORE)
  ;

fragment DOT
  : '.'
  ;

fragment LOWERCASE_LETTER
  : [a-z]
  ;

fragment CHAR
  : [a-z0-9]
  ;

fragment UNDERSCORE
  : '_'
  ;


WS : [ \t\r\n]+ -> skip ;

INVALID_BKNetID: .
    {
      raise ErrorToken(self.text[0])
    }
  ;

