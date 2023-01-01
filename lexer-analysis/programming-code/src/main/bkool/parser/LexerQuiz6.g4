grammar LexerQuiz6;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program : ;

/// an action is executed after a rule has been matched
/// also can define RULE: X {} | Y {};
PHP_INTERGER
  : INTERGER
    {
      self.text = self.text.replace("_", '');
    }
  ;

fragment INTERGER
  : NON_ZERO_DIGIT (UNDERSCORE | DIGIT)*
  | '0'
  ;

fragment DIGIT
  : [0-9]
  ;

fragment NON_ZERO_DIGIT
  : [1-9]
  ;

fragment UNDERSCORE
  : '_'
  ;


WS : [ \t\r\n]+ -> skip ;

INVALID_PHP_INTERGER: .
    {
      raise ErrorToken(self.text[0])
    }
  ;

