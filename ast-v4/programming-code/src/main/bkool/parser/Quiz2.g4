grammar Quiz2;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: mptype EOF;

arraytype:  primtype dimen | arraytype dimen  ;

mptype: primtype | arraytype;

primtype: INTTYPE | FLOATTYPE; 

dimen: '[' num '..' num ']';

num: '-'? INTLIT;

INTLIT: [0-9]+ ;

INTTYPE: 'integer';

FLOATTYPE: 'real';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
