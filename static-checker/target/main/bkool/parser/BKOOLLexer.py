# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\23")
        buf.write("c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\6\bD\n\b\r\b\16\bE\3\t\6\tI\n\t\r\t\16\tJ\3\n\3\n")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\6\17X\n\17\r")
        buf.write("\17\16\17Y\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\2\2")
        buf.write("\23\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23\3\2\5\4\2C\\c|\3\2\62")
        buf.write(";\5\2\13\f\17\17\"\"\2e\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\3%\3\2\2\2\5\'\3\2\2\2\7)\3\2\2\2")
        buf.write("\t-\3\2\2\2\13\63\3\2\2\2\r9\3\2\2\2\17C\3\2\2\2\21H\3")
        buf.write("\2\2\2\23L\3\2\2\2\25N\3\2\2\2\27P\3\2\2\2\31R\3\2\2\2")
        buf.write("\33T\3\2\2\2\35W\3\2\2\2\37]\3\2\2\2!_\3\2\2\2#a\3\2\2")
        buf.write("\2%&\7.\2\2&\4\3\2\2\2\'(\7<\2\2(\6\3\2\2\2)*\7k\2\2*")
        buf.write("+\7p\2\2+,\7v\2\2,\b\3\2\2\2-.\7h\2\2./\7n\2\2/\60\7q")
        buf.write("\2\2\60\61\7c\2\2\61\62\7v\2\2\62\n\3\2\2\2\63\64\7e\2")
        buf.write("\2\64\65\7q\2\2\65\66\7p\2\2\66\67\7u\2\2\678\7v\2\28")
        buf.write("\f\3\2\2\29:\7h\2\2:;\7w\2\2;<\7p\2\2<=\7e\2\2=>\7v\2")
        buf.write("\2>?\7k\2\2?@\7q\2\2@A\7p\2\2A\16\3\2\2\2BD\t\2\2\2CB")
        buf.write("\3\2\2\2DE\3\2\2\2EC\3\2\2\2EF\3\2\2\2F\20\3\2\2\2GI\t")
        buf.write("\3\2\2HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2JK\3\2\2\2K\22\3\2")
        buf.write("\2\2LM\7*\2\2M\24\3\2\2\2NO\7+\2\2O\26\3\2\2\2PQ\7}\2")
        buf.write("\2Q\30\3\2\2\2RS\7\177\2\2S\32\3\2\2\2TU\7=\2\2U\34\3")
        buf.write("\2\2\2VX\t\4\2\2WV\3\2\2\2XY\3\2\2\2YW\3\2\2\2YZ\3\2\2")
        buf.write("\2Z[\3\2\2\2[\\\b\17\2\2\\\36\3\2\2\2]^\13\2\2\2^ \3\2")
        buf.write("\2\2_`\13\2\2\2`\"\3\2\2\2ab\13\2\2\2b$\3\2\2\2\6\2EJ")
        buf.write("Y\3\b\2\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    INTTYPE = 3
    FLOATTYPE = 4
    CONST = 5
    FUNCTION = 6
    ID = 7
    INTLIT = 8
    LB = 9
    RB = 10
    LP = 11
    RP = 12
    SEMI = 13
    WS = 14
    ERROR_CHAR = 15
    UNCLOSE_STRING = 16
    ILLEGAL_ESCAPE = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "':'", "'int'", "'float'", "'const'", "'function'", "'('", 
            "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "FLOATTYPE", "CONST", "FUNCTION", "ID", "INTLIT", 
            "LB", "RB", "LP", "RP", "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "INTTYPE", "FLOATTYPE", "CONST", "FUNCTION", 
                  "ID", "INTLIT", "LB", "RB", "LP", "RP", "SEMI", "WS", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


