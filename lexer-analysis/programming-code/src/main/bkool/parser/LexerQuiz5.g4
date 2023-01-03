lexer grammar LexerQuiz5;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

IPv4_INIT
  :  X DOT X DOT X DOT X
  ;

///  X is an octet and must be a decimal value between 0 and 255
fragment X 
  : '0'
  | NON_ZERO_DIGIT DIGIT?
  | '1' DIGIT? DIGIT?
  | '2' [0-4]? DIGIT?
  | '25' [0-5]?
  ;

fragment DOT
  : '.'
  ;

fragment DIGIT
  : [0-9]
  ;

fragment NON_ZERO_DIGIT
  : [1-9]
  ;

WS : [ \t\r\n]+ -> skip ;

INVALID_IPv4: .
    {
      raise ErrorToken(self.text[0])
    }
  ;

