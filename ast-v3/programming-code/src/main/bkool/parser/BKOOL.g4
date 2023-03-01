grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}
program: vardecl+ EOF;

vardecl: mptype ids ';' ;

mptype: INTTYPE | FLOATTYPE;

ids: ID (COMMA ID)*; 

INTTYPE: 'int';

FLOATTYPE: 'float';

ID: [a-z]+ ;

COMMA: ',';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
