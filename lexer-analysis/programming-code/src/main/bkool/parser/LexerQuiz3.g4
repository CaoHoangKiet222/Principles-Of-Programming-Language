grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program : ;

STRING_INIT
  : SINGLE_QUOTE CHAR+ SINGLE_QUOTE
  ;

fragment SINGLE_QUOTE
  : '\''
  ;

fragment CHAR
  : ~['] | '\'\''
  ;

WS : [ \t\r\n]+ -> skip ;

INVALID_STR: .
    {
      raise ErrorToken(self.text[0])
    }
  ;

