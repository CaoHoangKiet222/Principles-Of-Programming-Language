// 2053165
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program:  EOF ;

/* arraylit_exprs 
  : expr COMMA arraylit_exprs
  | expr
  ;

expr : 'expr'
  ;

*/

// ================= Literals ===================
INT_LIT : ([1-9] [0-9]* ('_' [0-9]+)* | '0') 
    {
      self.text = self.text.replace('_', '')
    }
  ;

FLOAT_LIT 
  : (POINT_FLOAT | EXPONENT_FLOAT)
    {
      self.text = self.text.replace('_', '')
    }
  ;

fragment POINT_FLOAT
  : INT_PART? FRACTION_PART
  | INT_PART '.'
  ;

fragment EXPONENT_FLOAT
  : (POINT_FLOAT | INT_PART) EXPONENT
  ;

fragment EXPONENT
  : [eE] [+-]? [0-9]+
  ;

fragment INT_PART
  : INT_LIT 
  ;

fragment FRACTION_PART
  : '.' [0-9]*
  ;

BOOLEAN_LIT : TRUE | FALSE
  ;

STRING_LIT : '"' (ESC | STR_CHAR)* '"'
    {
      content = str(self.text) 
      self.text = content[1:-1]
    }
  ;

fragment ESC
  : '\\' ('b'|'f'|'r'|'n'|'t'|'\''|'\\')
  ;

fragment STR_CHAR
  : ~[\\\n]
  ;

/* ARRAY_LIT : '{' arraylit_exprs '}'
  ;
*/



// ================= Keywords ====================
AUTO : 'auto'
  ;

BREAK : 'break'
  ;

BOOL : 'bool'
  ;

DO : 'do'
  ;

ELSE : 'else'
  ;

IF : 'if'
  ;

FUNCTION : 'function'
  ;

FOR : 'for'
  ;

FLOAT_KQ : 'float'
  ;

FALSE : 'false'
  ;

INTEGER_KQ : 'integer'
  ;

RETURN : 'return'
  ;

STRING : 'string'
  ;

TRUE : 'true'
  ;

VOID : 'void'
  ;

CONTINUE : 'continue'
  ;

OUT : 'out'
  ;

WHILE : 'while'
  ;

OF : 'of'
  ;

INHERIT : 'inherit'
  ;

// ================= Seperators =====================
LP : '('
  ;

RP : ')'
  ;

LCB : '{'
  ;

RCB : '}'
  ;

LSB : '['
  ;

RSB : ']'
  ;

COMMA : ','
  ;

// ================= Arithmetic Operators ====================
ADD : '+'
  ; 
  
MINUS : '-'
  ; 
  
MUL : '*'
  ; 
  
DIV : '/'
  ; 
  
MOD : '%'
  ; 

// ================= Logical Operators ====================
NOT : '!'
  ;

AND : '&&'
  ;

OR : '||'
  ;

// ================= Comparison Operators ====================

NOT_EQ : '!='
  ;

EQUALS : '=='
  ;

LESS_THAN : '<'
  ;

GREATER_THAN : '>'
  ;

GT_EQ : '>='
  ;

LT_EQ : '<='
  ;

// ================= Scope Resolution Operators ==============
SCOPE_OP : '::'
  ;


// ================= Identifiers ====================
ID : [a-zA-Z_] [a-zA-Z0-9_]*
  ;

// ================= Define Comment =================
BLOCK_COMMENT
  : '/*' (.)+? '*/' -> skip
  ;

SINGLE_LINE_COMMENT
  : '//' ~[\n\r]* -> skip
  ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR
  : .
    {
      raise ErrorToken(self.text)
    }
  ;

UNCLOSE_STRING
  : '"' (STR_CHAR | ESC)* (EOF | '\n')
    {
      newline_esc = '\n'
      if self.text[-1] in newline_esc:
        raise UncloseString(self.text[1:-1])
      else:
        raise UncloseString(self.text[1:])
    }
  ;

ILLEGAL_ESCAPE: .;
