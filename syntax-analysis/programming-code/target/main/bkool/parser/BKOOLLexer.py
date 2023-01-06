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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26")
        buf.write("\u008d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\3\2\3\2\5\2\66\n\2\3\3\3\3\7\3:\n\3\f\3\16")
        buf.write("\3=\13\3\3\3\6\3@\n\3\r\3\16\3A\5\3D\n\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\5\4K\n\4\3\5\3\5\6\5O\n\5\r\5\16\5P\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\7\fl\n\f\f\f")
        buf.write("\16\fo\13\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21")
        buf.write("\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\2\2\32\3")
        buf.write("\3\5\4\7\5\t\2\13\2\r\2\17\2\21\6\23\7\25\b\27\t\31\n")
        buf.write("\33\13\35\f\37\r!\16#\17%\20\'\21)\22+\23-\24/\25\61\26")
        buf.write("\3\2\6\3\2\62;\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17")
        buf.write("\"\"\2\u008f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\3\65\3\2\2\2\5")
        buf.write("C\3\2\2\2\7J\3\2\2\2\tL\3\2\2\2\13R\3\2\2\2\rT\3\2\2\2")
        buf.write("\17V\3\2\2\2\21X\3\2\2\2\23_\3\2\2\2\25c\3\2\2\2\27i\3")
        buf.write("\2\2\2\31p\3\2\2\2\33r\3\2\2\2\35t\3\2\2\2\37v\3\2\2\2")
        buf.write("!x\3\2\2\2#z\3\2\2\2%|\3\2\2\2\'~\3\2\2\2)\u0080\3\2\2")
        buf.write("\2+\u0082\3\2\2\2-\u0084\3\2\2\2/\u0086\3\2\2\2\61\u008a")
        buf.write("\3\2\2\2\63\66\5\23\n\2\64\66\5\25\13\2\65\63\3\2\2\2")
        buf.write("\65\64\3\2\2\2\66\4\3\2\2\2\67;\5\17\b\28:\5\r\7\298\3")
        buf.write("\2\2\2:=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<D\3\2\2\2=;\3\2\2")
        buf.write("\2>@\7\62\2\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2AB\3\2\2\2")
        buf.write("BD\3\2\2\2C\67\3\2\2\2C?\3\2\2\2D\6\3\2\2\2EF\5\5\3\2")
        buf.write("FG\5\t\5\2GK\3\2\2\2HI\7\62\2\2IK\5\t\5\2JE\3\2\2\2JH")
        buf.write("\3\2\2\2K\b\3\2\2\2LN\5\13\6\2MO\5\r\7\2NM\3\2\2\2OP\3")
        buf.write("\2\2\2PN\3\2\2\2PQ\3\2\2\2Q\n\3\2\2\2RS\7\60\2\2S\f\3")
        buf.write("\2\2\2TU\t\2\2\2U\16\3\2\2\2VW\t\2\2\2W\20\3\2\2\2XY\7")
        buf.write("t\2\2YZ\7g\2\2Z[\7v\2\2[\\\7w\2\2\\]\7t\2\2]^\7p\2\2^")
        buf.write("\22\3\2\2\2_`\7k\2\2`a\7p\2\2ab\7v\2\2b\24\3\2\2\2cd\7")
        buf.write("h\2\2de\7n\2\2ef\7q\2\2fg\7c\2\2gh\7v\2\2h\26\3\2\2\2")
        buf.write("im\t\3\2\2jl\t\4\2\2kj\3\2\2\2lo\3\2\2\2mk\3\2\2\2mn\3")
        buf.write("\2\2\2n\30\3\2\2\2om\3\2\2\2pq\7?\2\2q\32\3\2\2\2rs\7")
        buf.write("-\2\2s\34\3\2\2\2tu\7/\2\2u\36\3\2\2\2vw\7,\2\2w \3\2")
        buf.write("\2\2xy\7\61\2\2y\"\3\2\2\2z{\7.\2\2{$\3\2\2\2|}\7=\2\2")
        buf.write("}&\3\2\2\2~\177\7*\2\2\177(\3\2\2\2\u0080\u0081\7+\2\2")
        buf.write("\u0081*\3\2\2\2\u0082\u0083\7}\2\2\u0083,\3\2\2\2\u0084")
        buf.write("\u0085\7\177\2\2\u0085.\3\2\2\2\u0086\u0087\t\5\2\2\u0087")
        buf.write("\u0088\3\2\2\2\u0088\u0089\b\30\2\2\u0089\60\3\2\2\2\u008a")
        buf.write("\u008b\13\2\2\2\u008b\u008c\b\31\3\2\u008c\62\3\2\2\2")
        buf.write("\n\2\65;ACJPm\4\b\2\2\3\31\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TYPE = 1
    INT_LITERAL = 2
    FLOAT_LITERAL = 3
    RETURN = 4
    INT = 5
    FLOAT = 6
    ID = 7
    EQUAL = 8
    ADD = 9
    SUB = 10
    MUL = 11
    DIV = 12
    COMMA = 13
    SEMICOLON = 14
    LB = 15
    RB = 16
    LCB = 17
    RCB = 18
    WS = 19
    ERROR_CHAR = 20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'return'", "'int'", "'float'", "'='", "'+'", "'-'", "'*'", 
            "'/'", "','", "';'", "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "TYPE", "INT_LITERAL", "FLOAT_LITERAL", "RETURN", "INT", "FLOAT", 
            "ID", "EQUAL", "ADD", "SUB", "MUL", "DIV", "COMMA", "SEMICOLON", 
            "LB", "RB", "LCB", "RCB", "WS", "ERROR_CHAR" ]

    ruleNames = [ "TYPE", "INT_LITERAL", "FLOAT_LITERAL", "FRACTION", "DOT", 
                  "DIGIT", "NON_ZERO_DIGIT", "RETURN", "INT", "FLOAT", "ID", 
                  "EQUAL", "ADD", "SUB", "MUL", "DIV", "COMMA", "SEMICOLON", 
                  "LB", "RB", "LCB", "RCB", "WS", "ERROR_CHAR" ]

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
            actions[23] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                  raise ErrorToken(self.text)
                
     


