// 2053165
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program:  EOF ;

// ================= Declarations =================
// Variable declarations
vardecl 
  : id_list COLON non_auto_type_decl ASSIGN expr_list? SEMI
  | id_list COLON auto_type ASSIGN expr_list SEMI
  ;

id_list returns [size]
  : ID {size += 1} COMMA id_list
  | ID {size = 0}
  ;

type_decl 
  : (int_type | float_type | boolean_type | string_type | array_type | auto_type)
  ;

non_auto_type_decl
  : (int_type | float_type | boolean_type | string_type | array_type)
  ;

// Parameters declarations
paramsdecl : OUT? ID COLON type_decl


// ================= Automic Types ===================
int_type : INTEGER
  ;

float_type : FLOAT
  ;

boolean_type : BOOLEAN
  ;

string_type : STRING
  ;

array_type : ARRAY dimensions OF element_type
  ;

dimensions 
  : INT_LIT COMMA dimensions
  | INT_LIT
  ;

element_type 
  : (int_type | float_type | boolean_type | string_type)
  ;

void_type : VOID
  ;

auto_type : AUTO
  ;

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
  : '\\' ('b' | 'f' | 'r' | 'n' | 't' | '\'' | '\\' | '"')
  | '\'"'
  ;

fragment ESC_ERR
  : '\\' ~[bfrnt'\\]
  ;

fragment STR_CHAR
  : ~[\\\n"]
  ;

array_lit : '{' expr_list '}'
  ;

expr_list
  : expr COMMA expr_list
  | expr
  ;

expr : 'expr'
  ;

// ================= Keywords ====================
AUTO : 'auto'
  ;

BREAK : 'break'
  ;

BOOLEAN : 'boolean'
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

FLOAT : 'float'
  ;

FALSE : 'false'
  ;

INTEGER : 'integer'
  ;

INT : 'int'
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

ARRAY : 'array'
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

DOT : '.'
  ;

SEMI : ';'
  ;

COLON : ':'
  ;

ASSIGN : '='
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

ILLEGAL_ESCAPE
  : '"' (STR_CHAR | ESC)* ESC_ERR
    {
      raise IllegalEscape(self.text[1:])
    }
  ;

ERROR_CHAR
  : .
    {
      raise ErrorToken(self.text)
    }
  ;
