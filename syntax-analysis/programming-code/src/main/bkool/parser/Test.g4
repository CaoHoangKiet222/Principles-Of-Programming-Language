grammar Test;

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
def size_expr(self):
    try:
        return self._size_expr
    except AttributeError:
        self._size_expr = 0
        return self._size_expr

@size_id.setter
def size_id(self, value):
    self._size_id = value

@size_expr.setter
def size_expr(self, value):
    self._size_expr = value
}

options {
	language=Python3;
}

program : program_int EOF
  ;

program_int
  : vardecl program_int
  | vardecl
  ;

vardecl 
  : (({assign = False} id_list COLON non_auto_type_decl 
      ((ASSIGN expr_list) {assign = True})? SEMI)
{
if assign == True and self.size_id != self.size_expr:
  print("SOMETHING WENT WRONG!!!")
}

  | (id_list COLON auto_type ASSIGN expr_list SEMI)
{
if self.size_id != self.size_expr:
  print("SOMETHING WENT WRONG!!!")
}) 
{
print(f'size_id: {self.size_id}')
print(f'size_expr: {self.size_expr}')
self.size_id = 0
self.size_expr = 0
}
  ;

id_list
  : ID {self.size_id += 1} COMMA id_list
  | ID {self.size_id += 1}
  ;

non_auto_type_decl
  : (int_type | float_type | boolean_type | string_type | array_type | void_type)
  ;

int_type : INTEGER | INT
  ;

float_type : FLOAT
  ;

boolean_type : BOOLEAN
  ;

string_type : STRING
  ;

array_type : ARRAY '[' dimensions ']' OF element_type
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

expr_list
  : expr {self.size_expr += 1} COMMA expr_list
  | expr {self.size_expr += 1}
  ;

INT_LIT : ([1-9] [0-9]* ('_' [0-9]+)* | '0') 
    {
      self.text = self.text.replace('_', '')
    }
  ;

expr : 'expr'
  ;

AUTO : 'auto'
  ;

FLOAT : 'float'
  ;

INTEGER : 'integer'
  ;

INT : 'int'
  ;

FLOAT : 'float'
  ;

STRING : 'string'
  ;

BOOLEAN : 'boolean'
  ;

ARRAY : 'array'
  ;

OF : 'of'
  ;

VOID : 'void'
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

ID : [a-zA-Z_] [a-zA-Z0-9_]*
  ;


WS
  : [ \t\r\n] -> skip
  ;

ERROR_CHAR
  : .
    {
      raise ErrorToken(self.text)
    }
  ;
