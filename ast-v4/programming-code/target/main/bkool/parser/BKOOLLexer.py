# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("A\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\6\6\6$\n\6\r\6\16\6%\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\6\t")
        buf.write("\66\n\t\r\t\16\t\67\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f")
        buf.write("\2\2\r\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\3\2\4\3\2\62;\5\2\13\f\17\17\"\"\2B\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\3\31\3\2\2\2\5\33\3\2\2\2\7\36\3\2\2\2")
        buf.write("\t \3\2\2\2\13#\3\2\2\2\r\'\3\2\2\2\17/\3\2\2\2\21\65")
        buf.write("\3\2\2\2\23;\3\2\2\2\25=\3\2\2\2\27?\3\2\2\2\31\32\7]")
        buf.write("\2\2\32\4\3\2\2\2\33\34\7\60\2\2\34\35\7\60\2\2\35\6\3")
        buf.write("\2\2\2\36\37\7_\2\2\37\b\3\2\2\2 !\7/\2\2!\n\3\2\2\2\"")
        buf.write("$\t\2\2\2#\"\3\2\2\2$%\3\2\2\2%#\3\2\2\2%&\3\2\2\2&\f")
        buf.write("\3\2\2\2\'(\7k\2\2()\7p\2\2)*\7v\2\2*+\7g\2\2+,\7i\2\2")
        buf.write(",-\7g\2\2-.\7t\2\2.\16\3\2\2\2/\60\7t\2\2\60\61\7g\2\2")
        buf.write("\61\62\7c\2\2\62\63\7n\2\2\63\20\3\2\2\2\64\66\t\3\2\2")
        buf.write("\65\64\3\2\2\2\66\67\3\2\2\2\67\65\3\2\2\2\678\3\2\2\2")
        buf.write("89\3\2\2\29:\b\t\2\2:\22\3\2\2\2;<\13\2\2\2<\24\3\2\2")
        buf.write("\2=>\13\2\2\2>\26\3\2\2\2?@\13\2\2\2@\30\3\2\2\2\5\2%")
        buf.write("\67\3\b\2\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    INTLIT = 5
    INTTYPE = 6
    FLOATTYPE = 7
    WS = 8
    ERROR_CHAR = 9
    UNCLOSE_STRING = 10
    ILLEGAL_ESCAPE = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "'..'", "']'", "'-'", "'integer'", "'real'" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "INTTYPE", "FLOATTYPE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "INTLIT", "INTTYPE", "FLOATTYPE", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


