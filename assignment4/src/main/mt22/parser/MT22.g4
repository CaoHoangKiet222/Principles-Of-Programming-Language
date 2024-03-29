// 2053165
grammar MT22;

@lexer::header {
from lexererr import *
}

@parser::members {
@property
def size_id(self):
    try:
        return self._size_id
    except AttributeError:
        self._size_id = 0
        return self._size_id

@property
def assign(self):
    try:
        return self._assign
    except AttributeError:
        self._assign = False
        return self._assign

@size_id.setter
def size_id(self, value):
    self._size_id = value

@assign.setter
def assign(self, value):
    self._assign = value

def checkFullFormat(self, flag=False):
    self.size_id -= 1
    if self.assign == True:
      # a,b,c,d: float = 1+2,3,4,5,7+8; -> error
      if flag == False and self.size_id <= 0:
        raise NoViableAltException(self)

      # a,b,c,d: float = 1+2,3,4; -> error
      if flag == True and self.size_id > 0:
        raise NoViableAltException(self)
    
}

options{
	language=Python3;
}

program: decls EOF;

decls
  : decl decls
  | decl
  ;

decl
  : vardecl
  | funcdecl
  | paramdecl
  ;

// ================= Declarations =================

// Parameters declarations
paramdecl: param
  ;

// Function declarations

funcdecl
  : func_name COLON FUNCTION return_type LP param_list? RP (INHERIT ID)? body
  ;

return_type
  : type_decl | void_type
  ;

param_list
  : param COMMA param_list
  | param
  ;

param
  : INHERIT? OUT? ID COLON type_decl
  ;

body : block_stat
  ;

// Variable declarations

vardecl 
  : (id_list COLON type_decl (ASSIGN {self.assign = True} expr_list_for_valdecl)? SEMI) 
    {self.size_id = 0}
  ;

id_list
  : ID {self.size_id += 1} COMMA id_list
  | ID {self.size_id += 1}
  ;

type_decl 
  : non_auto_type_decl | auto_type
  ;

non_auto_type_decl
  : int_type | float_type | boolean_type | string_type | array_type
  ;

// ============== Automic Types ==================

int_type 
  : INTEGER
  ;

float_type : FLOAT
  ;

boolean_type : BOOLEAN
  ;

string_type : STRING
  ;

array_type 
  : ARRAY LSB dimensions RSB OF element_type
  ;

dimensions 
  : INT_LIT COMMA dimensions
  | INT_LIT
  ;

element_type 
  : int_type | float_type | boolean_type | string_type
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
  : (   
      INT_PART FRACTION_PART EXPONENT? 
      | INT_PART EXPONENT
      | FRACTION_PART EXPONENT
    )
    {
      self.text = self.text.replace('_', '')
    }
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
      self.text = self.text[1:-1]
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

array_lit : LCB expr_list? RCB
  ;

// ================= Statements =================
stat
  : assign_stat
  | if_stat
  | for_stat
  | while_stat
  | do_while_stat
  | break_stat
  | continue_stat
  | return_stat
  | call_stat
  | block_stat
  ;

assign_stat 
  : (scalar_var | ID index_op) ASSIGN expr SEMI
  ;

if_stat
  :  IF LP expr RP stat (ELSE stat)?
  ;

for_stat
  : FOR LP (scalar_var ASSIGN init_expr) COMMA condition_expr COMMA update_expr RP stat
  ;

scalar_var : ID
  ;

init_expr : expr
  ;

condition_expr : expr
  ;

update_expr : expr
  ;

while_stat
  : WHILE LP expr RP stat
  ;

do_while_stat
  : DO block_stat WHILE LP expr RP SEMI
  ;

break_stat
  : BREAK SEMI
  ;

continue_stat
  : CONTINUE SEMI
  ;

return_stat
  : RETURN expr? SEMI
  ;

call_stat
  : func_name LP expr_list? RP SEMI
  ;

func_name
  : ID
  ;

block_stat
  : LCB body_block_stat? RCB
  ;

body_block_stat
  : (vardecl | stat) body_block_stat
  | (vardecl | stat)
  ;

// ================= Expressions ================

/* use for define vardecl*/
expr_list_for_valdecl
  : expr {self.checkFullFormat()} COMMA expr_list_for_valdecl
  | expr {self.checkFullFormat(True)}
  ;

expr_list
  : expr COMMA expr_list
  | expr
  ;

expr 
  : expr1 SCOPE_OP expr1
  | expr1
  ;

expr1 
  : expr2 (EQUAL | NOT_EQ | GREATER_THAN | LESS_THAN | GT_EQ | LT_EQ) expr2
  | expr2
  ;

expr2
  : expr2 (AND | OR) expr3
  | expr3
  ;

expr3
  : expr3 (ADD | MINUS) expr4
  | expr4
  ;

expr4
  : expr4 (MUL | DIV | MOD) expr5
  | expr5
  ;

expr5
  : NOT expr5
  | expr6
  ;

expr6
  : MINUS expr6
  | expr7
  ;

expr7
  : ID index_op
  | expr8
  ;

expr8
  : operands
  | LP expr RP
  ;

func_call
  : func_name LP expr_list? RP
  ;

operands 
  : (INT_LIT | FLOAT_LIT | BOOLEAN_LIT | STRING_LIT | array_lit)
  | func_call
  | ID
  ;

index_op
  : LSB expr_list RSB
  ;

// ================= Keywords ====================

AUTO : 'auto'
  ;

BOOLEAN : 'boolean'
  ;

INTEGER : 'integer'
  ;

FLOAT : 'float'
  ;

STRING : 'string'
  ;

ARRAY : 'array'
  ;

BREAK : 'break'
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

FALSE : 'false'
  ;

RETURN : 'return'
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

// ================= Seperators ===================

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

// =========== Arithmetic Operators ================

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

// ============= Logical Operators =================

NOT : '!'
  ;

AND : '&&'
  ;

OR : '||'
  ;

// ============ Comparison Operators ===============

NOT_EQ : '!='
  ;

EQUAL : '=='
  ;

LESS_THAN : '<'
  ;

GREATER_THAN : '>'
  ;

GT_EQ : '>='
  ;

LT_EQ : '<='
  ;

// ========= Scope Resolution Operators =============
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





