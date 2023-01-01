grammar LexerQuiz2;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program : ;

FLOATING_POINT_INIT 
  : POINT_FLOAT | EXPONENT_FLOAT
  ;

fragment POINT_FLOAT
  : INT_PART FRACTION
  ;

fragment EXPONENT_FLOAT
  : (POINT_FLOAT | INT_PART) EXPONENT
  ;

fragment EXPONENT
  : [eE] [+-]? DIGIT+
  ;

fragment INT_PART
  : DIGIT+
  ;

fragment FRACTION 
  : DOT DIGIT+
  ;

fragment DOT 
  : '.'
  ;

fragment NON_ZERO_DIGIT
  : [1-9]
  ;

fragment DIGIT
 : [0-9]
 ;

WS : [ \t\r\n]+ -> skip ;

INVALID_FLOATING_POINT: .
    {
      raise ErrorToken(self.text[0])
    }
  ;

