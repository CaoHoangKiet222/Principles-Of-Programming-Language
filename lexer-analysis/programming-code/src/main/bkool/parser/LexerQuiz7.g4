grammar LexerQuiz7;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program : ;

SHEXA_INIT
  : SHEXA
  ;

fragment SHEXA
  : NON_ZERO_DIGIT (DIGIT | HEX_CHARACTER)* (EVEN_DIGIT | EVEN_HEX_CHARACTER)
  | '0'
  ;

fragment NON_ZERO_DIGIT
  : [1-9]
  ;

fragment DIGIT
  : [0-9]
  ;

fragment EVEN_DIGIT
  : '0' | '2' | '4' | '6' | '8'
  ;

fragment HEX_CHARACTER
  : [a-fA-F]
  ;

fragment EVEN_HEX_CHARACTER
  : 'a' | 'c' | 'e' | 'A' | 'C' | 'E'
  ;

WS : [ \t\r\n]+ -> skip ;

INVALID_SHEXA: .
    {
      raise ErrorToken(self.text[0])
    }
  ;

