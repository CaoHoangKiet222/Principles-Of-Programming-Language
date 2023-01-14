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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\27")
        buf.write("\u0099\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\7\59\n\5\f\5\16\5<\13\5\3\5")
        buf.write("\3\5\6\5@\n\5\r\5\16\5A\7\5D\n\5\f\5\16\5G\13\5\3\5\5")
        buf.write("\5J\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\3\24\3\24\7\24\u008e\n\24\f\24\16")
        buf.write("\24\u0091\13\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\2\2")
        buf.write("\27\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27\3\2")
        buf.write("\7\3\2\63;\3\2\62;\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f")
        buf.write("\17\17\"\"\2\u009d\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\3-\3\2\2\2\5/\3\2\2\2\7\61\3\2\2\2\tI\3\2\2\2\13")
        buf.write("M\3\2\2\2\rR\3\2\2\2\17X\3\2\2\2\21`\3\2\2\2\23d\3\2\2")
        buf.write("\2\25k\3\2\2\2\27s\3\2\2\2\31y\3\2\2\2\33|\3\2\2\2\35")
        buf.write("\u0081\3\2\2\2\37\u0083\3\2\2\2!\u0085\3\2\2\2#\u0087")
        buf.write("\3\2\2\2%\u0089\3\2\2\2\'\u008b\3\2\2\2)\u0092\3\2\2\2")
        buf.write("+\u0096\3\2\2\2-.\7]\2\2.\4\3\2\2\2/\60\7_\2\2\60\6\3")
        buf.write("\2\2\2\61\62\7g\2\2\62\63\7z\2\2\63\64\7r\2\2\64\65\7")
        buf.write("t\2\2\65\b\3\2\2\2\66:\t\2\2\2\679\t\3\2\28\67\3\2\2\2")
        buf.write("9<\3\2\2\2:8\3\2\2\2:;\3\2\2\2;E\3\2\2\2<:\3\2\2\2=?\7")
        buf.write("a\2\2>@\t\3\2\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2AB\3\2\2")
        buf.write("\2BD\3\2\2\2C=\3\2\2\2DG\3\2\2\2EC\3\2\2\2EF\3\2\2\2F")
        buf.write("J\3\2\2\2GE\3\2\2\2HJ\7\62\2\2I\66\3\2\2\2IH\3\2\2\2J")
        buf.write("K\3\2\2\2KL\b\5\2\2L\n\3\2\2\2MN\7c\2\2NO\7w\2\2OP\7v")
        buf.write("\2\2PQ\7q\2\2Q\f\3\2\2\2RS\7h\2\2ST\7n\2\2TU\7q\2\2UV")
        buf.write("\7c\2\2VW\7v\2\2W\16\3\2\2\2XY\7k\2\2YZ\7p\2\2Z[\7v\2")
        buf.write("\2[\\\7g\2\2\\]\7i\2\2]^\7g\2\2^_\7t\2\2_\20\3\2\2\2`")
        buf.write("a\7k\2\2ab\7p\2\2bc\7v\2\2c\22\3\2\2\2de\7u\2\2ef\7v\2")
        buf.write("\2fg\7t\2\2gh\7k\2\2hi\7p\2\2ij\7i\2\2j\24\3\2\2\2kl\7")
        buf.write("d\2\2lm\7q\2\2mn\7q\2\2no\7n\2\2op\7g\2\2pq\7c\2\2qr\7")
        buf.write("p\2\2r\26\3\2\2\2st\7c\2\2tu\7t\2\2uv\7t\2\2vw\7c\2\2")
        buf.write("wx\7{\2\2x\30\3\2\2\2yz\7q\2\2z{\7h\2\2{\32\3\2\2\2|}")
        buf.write("\7x\2\2}~\7q\2\2~\177\7k\2\2\177\u0080\7f\2\2\u0080\34")
        buf.write("\3\2\2\2\u0081\u0082\7.\2\2\u0082\36\3\2\2\2\u0083\u0084")
        buf.write("\7\60\2\2\u0084 \3\2\2\2\u0085\u0086\7=\2\2\u0086\"\3")
        buf.write("\2\2\2\u0087\u0088\7<\2\2\u0088$\3\2\2\2\u0089\u008a\7")
        buf.write("?\2\2\u008a&\3\2\2\2\u008b\u008f\t\4\2\2\u008c\u008e\t")
        buf.write("\5\2\2\u008d\u008c\3\2\2\2\u008e\u0091\3\2\2\2\u008f\u008d")
        buf.write("\3\2\2\2\u008f\u0090\3\2\2\2\u0090(\3\2\2\2\u0091\u008f")
        buf.write("\3\2\2\2\u0092\u0093\t\6\2\2\u0093\u0094\3\2\2\2\u0094")
        buf.write("\u0095\b\25\3\2\u0095*\3\2\2\2\u0096\u0097\13\2\2\2\u0097")
        buf.write("\u0098\b\26\4\2\u0098,\3\2\2\2\b\2:AEI\u008f\5\3\5\2\b")
        buf.write("\2\2\3\26\3")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    INT_LIT = 4
    AUTO = 5
    FLOAT = 6
    INTEGER = 7
    INT = 8
    STRING = 9
    BOOLEAN = 10
    ARRAY = 11
    OF = 12
    VOID = 13
    COMMA = 14
    DOT = 15
    SEMI = 16
    COLON = 17
    ASSIGN = 18
    ID = 19
    WS = 20
    ERROR_CHAR = 21

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "'expr'", "'auto'", "'float'", "'integer'", "'int'", 
            "'string'", "'boolean'", "'array'", "'of'", "'void'", "','", 
            "'.'", "';'", "':'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "INT_LIT", "AUTO", "FLOAT", "INTEGER", "INT", "STRING", "BOOLEAN", 
            "ARRAY", "OF", "VOID", "COMMA", "DOT", "SEMI", "COLON", "ASSIGN", 
            "ID", "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "INT_LIT", "AUTO", "FLOAT", "INTEGER", 
                  "INT", "STRING", "BOOLEAN", "ARRAY", "OF", "VOID", "COMMA", 
                  "DOT", "SEMI", "COLON", "ASSIGN", "ID", "WS", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[3] = self.INT_LIT_action 
            actions[20] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                  self.text = self.text.replace('_', '')
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                  raise ErrorToken(self.text)
                
     


