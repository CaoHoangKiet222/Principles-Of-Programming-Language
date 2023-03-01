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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("^\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\6\4!\n\4\r\4\16\4\"\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\5\5.\n\5\3\6\3\6\3\6\3\6\3\6\5\6\65")
        buf.write("\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7A\n\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\bK\n\b\3\t\6\tN\n\t")
        buf.write("\r\t\16\tO\3\n\6\nS\n\n\r\n\16\nT\3\n\3\n\3\13\3\13\3")
        buf.write("\f\3\f\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\3\2\6\3\2\62;\4\2>>@@\3\2c|\5")
        buf.write("\2\13\f\17\17\"\"\2j\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\3\33\3\2\2\2\5\35\3\2\2\2\7 \3\2\2\2\t-\3\2\2")
        buf.write("\2\13\64\3\2\2\2\r@\3\2\2\2\17J\3\2\2\2\21M\3\2\2\2\23")
        buf.write("R\3\2\2\2\25X\3\2\2\2\27Z\3\2\2\2\31\\\3\2\2\2\33\34\7")
        buf.write("*\2\2\34\4\3\2\2\2\35\36\7+\2\2\36\6\3\2\2\2\37!\t\2\2")
        buf.write("\2 \37\3\2\2\2!\"\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#\b\3\2")
        buf.write("\2\2$%\7V\2\2%&\7t\2\2&\'\7w\2\2\'.\7g\2\2()\7H\2\2)*")
        buf.write("\7c\2\2*+\7n\2\2+,\7u\2\2,.\7g\2\2-$\3\2\2\2-(\3\2\2\2")
        buf.write(".\n\3\2\2\2/\60\7c\2\2\60\61\7p\2\2\61\65\7f\2\2\62\63")
        buf.write("\7q\2\2\63\65\7t\2\2\64/\3\2\2\2\64\62\3\2\2\2\65\f\3")
        buf.write("\2\2\2\66\67\7-\2\2\67A\7?\2\289\7/\2\29A\7?\2\2:;\7(")
        buf.write("\2\2;A\7?\2\2<=\7~\2\2=A\7?\2\2>?\7<\2\2?A\7?\2\2@\66")
        buf.write("\3\2\2\2@8\3\2\2\2@:\3\2\2\2@<\3\2\2\2@>\3\2\2\2A\16\3")
        buf.write("\2\2\2BK\7?\2\2CD\7>\2\2DK\7@\2\2EF\7@\2\2FK\7?\2\2GH")
        buf.write("\7>\2\2HK\7?\2\2IK\t\3\2\2JB\3\2\2\2JC\3\2\2\2JE\3\2\2")
        buf.write("\2JG\3\2\2\2JI\3\2\2\2K\20\3\2\2\2LN\t\4\2\2ML\3\2\2\2")
        buf.write("NO\3\2\2\2OM\3\2\2\2OP\3\2\2\2P\22\3\2\2\2QS\t\5\2\2R")
        buf.write("Q\3\2\2\2ST\3\2\2\2TR\3\2\2\2TU\3\2\2\2UV\3\2\2\2VW\b")
        buf.write("\n\2\2W\24\3\2\2\2XY\13\2\2\2Y\26\3\2\2\2Z[\13\2\2\2[")
        buf.write("\30\3\2\2\2\\]\13\2\2\2]\32\3\2\2\2\n\2\"-\64@JOT\3\b")
        buf.write("\2\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    INTLIT = 3
    BOOLIT = 4
    ANDOR = 5
    ASSIGN = 6
    COMPARE = 7
    ID = 8
    WS = 9
    ERROR_CHAR = 10
    UNCLOSE_STRING = 11
    ILLEGAL_ESCAPE = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "BOOLIT", "ANDOR", "ASSIGN", "COMPARE", "ID", "WS", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "INTLIT", "BOOLIT", "ANDOR", "ASSIGN", 
                  "COMPARE", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


