lexer grammar Test;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

STRING_LIT : '"' (ESC | ~[\\"])* '"';

fragment ESC
  : '\\' ('b'|'f'|'r'|'n'|'t'|'\''|'\\')
  ;

WS : [ \t\b\f\r\n]+ -> skip ; // skip spaces, tabs, backspace, form feed, carriage return, newlines

ERROR_CHAR
  : .
    {
      raise ErrorToken(self.text)
    }
  ;
