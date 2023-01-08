# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\67")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\2\2\3\5\3\3\2\2\2\2")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'auto'", "'break'", "'bool'", "'do'", 
                     "'else'", "'if'", "'function'", "'for'", "'float'", 
                     "'false'", "'integer'", "'return'", "'string'", "'true'", 
                     "'void'", "'continue'", "'out'", "'while'", "'of'", 
                     "'inherit'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "','", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
                     "'||'", "'!='", "'=='", "'<'", "'>'", "'>='", "'<='", 
                     "'::'" ]

    symbolicNames = [ "<INVALID>", "INT_LIT", "FLOAT_LIT", "BOOLEAN_LIT", 
                      "STRING_LIT", "AUTO", "BREAK", "BOOL", "DO", "ELSE", 
                      "IF", "FUNCTION", "FOR", "FLOAT_KQ", "FALSE", "INTEGER_KQ", 
                      "RETURN", "STRING", "TRUE", "VOID", "CONTINUE", "OUT", 
                      "WHILE", "OF", "INHERIT", "LP", "RP", "LCB", "RCB", 
                      "LSB", "RSB", "COMMA", "ADD", "MINUS", "MUL", "DIV", 
                      "MOD", "NOT", "AND", "OR", "NOT_EQ", "EQUALS", "LESS_THAN", 
                      "GREATER_THAN", "GT_EQ", "LT_EQ", "SCOPE_OP", "ID", 
                      "BLOCK_COMMENT", "SINGLE_LINE_COMMENT", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    INT_LIT=1
    FLOAT_LIT=2
    BOOLEAN_LIT=3
    STRING_LIT=4
    AUTO=5
    BREAK=6
    BOOL=7
    DO=8
    ELSE=9
    IF=10
    FUNCTION=11
    FOR=12
    FLOAT_KQ=13
    FALSE=14
    INTEGER_KQ=15
    RETURN=16
    STRING=17
    TRUE=18
    VOID=19
    CONTINUE=20
    OUT=21
    WHILE=22
    OF=23
    INHERIT=24
    LP=25
    RP=26
    LCB=27
    RCB=28
    LSB=29
    RSB=30
    COMMA=31
    ADD=32
    MINUS=33
    MUL=34
    DIV=35
    MOD=36
    NOT=37
    AND=38
    OR=39
    NOT_EQ=40
    EQUALS=41
    LESS_THAN=42
    GREATER_THAN=43
    GT_EQ=44
    LT_EQ=45
    SCOPE_OP=46
    ID=47
    BLOCK_COMMENT=48
    SINGLE_LINE_COMMENT=49
    WS=50
    ERROR_CHAR=51
    UNCLOSE_STRING=52
    ILLEGAL_ESCAPE=53

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





