# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01cc\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\7\2")
        buf.write("\u0086\n\2\f\2\16\2\u0089\13\2\3\2\3\2\6\2\u008d\n\2\r")
        buf.write("\2\16\2\u008e\7\2\u0091\n\2\f\2\16\2\u0094\13\2\3\2\5")
        buf.write("\2\u0097\n\2\3\2\3\2\3\3\3\3\3\3\5\3\u009e\n\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\5\3\u00a6\n\3\3\3\3\3\3\4\3\4\5\4\u00ac")
        buf.write("\n\4\3\4\6\4\u00af\n\4\r\4\16\4\u00b0\3\5\3\5\3\6\3\6")
        buf.write("\7\6\u00b7\n\6\f\6\16\6\u00ba\13\6\3\7\3\7\5\7\u00be\n")
        buf.write("\7\3\b\3\b\3\b\7\b\u00c3\n\b\f\b\16\b\u00c6\13\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\5\t\u00cf\n\t\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3\"")
        buf.write("\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3")
        buf.write("*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\38\38\38\39\39\39\3:\3:\3:\3")
        buf.write(";\3;\7;\u018e\n;\f;\16;\u0191\13;\3<\3<\3<\3<\6<\u0197")
        buf.write("\n<\r<\16<\u0198\3<\3<\3<\3<\3<\3=\3=\3=\3=\7=\u01a4\n")
        buf.write("=\f=\16=\u01a7\13=\3=\3=\3>\6>\u01ac\n>\r>\16>\u01ad\3")
        buf.write(">\3>\3?\3?\3?\7?\u01b5\n?\f?\16?\u01b8\13?\3?\5?\u01bb")
        buf.write("\n?\3?\3?\3@\3@\3@\7@\u01c2\n@\f@\16@\u01c5\13@\3@\3@")
        buf.write("\3@\3A\3A\3A\3\u0198\2B\3\3\5\4\7\2\t\2\13\2\r\5\17\6")
        buf.write("\21\2\23\2\25\2\27\7\31\b\33\t\35\n\37\13!\f#\r%\16\'")
        buf.write("\17)\20+\21-\22/\23\61\24\63\25\65\26\67\279\30;\31=\32")
        buf.write("?\33A\34C\35E\36G\37I K!M\"O#Q$S%U&W\'Y([)]*_+a,c-e.g")
        buf.write("/i\60k\61m\62o\63q\64s\65u\66w\67y8{9}:\177;\u0081<\3")
        buf.write("\2\16\3\2\63;\3\2\62;\4\2GGgg\4\2--//\n\2$$))^^ddhhpp")
        buf.write("ttvv\t\2))^^ddhhppttvv\5\2\f\f$$^^\5\2C\\aac|\6\2\62;")
        buf.write("C\\aac|\4\2\f\f\17\17\5\2\13\f\17\17\"\"\3\3\f\f\2\u01db")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2")
        buf.write("u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2")
        buf.write("\2\177\3\2\2\2\2\u0081\3\2\2\2\3\u0096\3\2\2\2\5\u00a5")
        buf.write("\3\2\2\2\7\u00a9\3\2\2\2\t\u00b2\3\2\2\2\13\u00b4\3\2")
        buf.write("\2\2\r\u00bd\3\2\2\2\17\u00bf\3\2\2\2\21\u00ce\3\2\2\2")
        buf.write("\23\u00d0\3\2\2\2\25\u00d3\3\2\2\2\27\u00d5\3\2\2\2\31")
        buf.write("\u00da\3\2\2\2\33\u00e2\3\2\2\2\35\u00ea\3\2\2\2\37\u00f0")
        buf.write("\3\2\2\2!\u00f7\3\2\2\2#\u00fd\3\2\2\2%\u0103\3\2\2\2")
        buf.write("\'\u0106\3\2\2\2)\u010b\3\2\2\2+\u010e\3\2\2\2-\u0117")
        buf.write("\3\2\2\2/\u011b\3\2\2\2\61\u0121\3\2\2\2\63\u0128\3\2")
        buf.write("\2\2\65\u012d\3\2\2\2\67\u0132\3\2\2\29\u013b\3\2\2\2")
        buf.write(";\u013f\3\2\2\2=\u0145\3\2\2\2?\u0148\3\2\2\2A\u0150\3")
        buf.write("\2\2\2C\u0152\3\2\2\2E\u0154\3\2\2\2G\u0156\3\2\2\2I\u0158")
        buf.write("\3\2\2\2K\u015a\3\2\2\2M\u015c\3\2\2\2O\u015e\3\2\2\2")
        buf.write("Q\u0160\3\2\2\2S\u0162\3\2\2\2U\u0164\3\2\2\2W\u0166\3")
        buf.write("\2\2\2Y\u0168\3\2\2\2[\u016a\3\2\2\2]\u016c\3\2\2\2_\u016e")
        buf.write("\3\2\2\2a\u0170\3\2\2\2c\u0172\3\2\2\2e\u0175\3\2\2\2")
        buf.write("g\u0178\3\2\2\2i\u017b\3\2\2\2k\u017e\3\2\2\2m\u0180\3")
        buf.write("\2\2\2o\u0182\3\2\2\2q\u0185\3\2\2\2s\u0188\3\2\2\2u\u018b")
        buf.write("\3\2\2\2w\u0192\3\2\2\2y\u019f\3\2\2\2{\u01ab\3\2\2\2")
        buf.write("}\u01b1\3\2\2\2\177\u01be\3\2\2\2\u0081\u01c9\3\2\2\2")
        buf.write("\u0083\u0087\t\2\2\2\u0084\u0086\t\3\2\2\u0085\u0084\3")
        buf.write("\2\2\2\u0086\u0089\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088")
        buf.write("\3\2\2\2\u0088\u0092\3\2\2\2\u0089\u0087\3\2\2\2\u008a")
        buf.write("\u008c\7a\2\2\u008b\u008d\t\3\2\2\u008c\u008b\3\2\2\2")
        buf.write("\u008d\u008e\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f\3")
        buf.write("\2\2\2\u008f\u0091\3\2\2\2\u0090\u008a\3\2\2\2\u0091\u0094")
        buf.write("\3\2\2\2\u0092\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093")
        buf.write("\u0097\3\2\2\2\u0094\u0092\3\2\2\2\u0095\u0097\7\62\2")
        buf.write("\2\u0096\u0083\3\2\2\2\u0096\u0095\3\2\2\2\u0097\u0098")
        buf.write("\3\2\2\2\u0098\u0099\b\2\2\2\u0099\4\3\2\2\2\u009a\u009b")
        buf.write("\5\t\5\2\u009b\u009d\5\13\6\2\u009c\u009e\5\7\4\2\u009d")
        buf.write("\u009c\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u00a6\3\2\2\2")
        buf.write("\u009f\u00a0\5\t\5\2\u00a0\u00a1\5\7\4\2\u00a1\u00a6\3")
        buf.write("\2\2\2\u00a2\u00a3\5\13\6\2\u00a3\u00a4\5\7\4\2\u00a4")
        buf.write("\u00a6\3\2\2\2\u00a5\u009a\3\2\2\2\u00a5\u009f\3\2\2\2")
        buf.write("\u00a5\u00a2\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a8\b")
        buf.write("\3\3\2\u00a8\6\3\2\2\2\u00a9\u00ab\t\4\2\2\u00aa\u00ac")
        buf.write("\t\5\2\2\u00ab\u00aa\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac")
        buf.write("\u00ae\3\2\2\2\u00ad\u00af\t\3\2\2\u00ae\u00ad\3\2\2\2")
        buf.write("\u00af\u00b0\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3")
        buf.write("\2\2\2\u00b1\b\3\2\2\2\u00b2\u00b3\5\3\2\2\u00b3\n\3\2")
        buf.write("\2\2\u00b4\u00b8\7\60\2\2\u00b5\u00b7\t\3\2\2\u00b6\u00b5")
        buf.write("\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8")
        buf.write("\u00b9\3\2\2\2\u00b9\f\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb")
        buf.write("\u00be\5\63\32\2\u00bc\u00be\5/\30\2\u00bd\u00bb\3\2\2")
        buf.write("\2\u00bd\u00bc\3\2\2\2\u00be\16\3\2\2\2\u00bf\u00c4\7")
        buf.write("$\2\2\u00c0\u00c3\5\21\t\2\u00c1\u00c3\5\25\13\2\u00c2")
        buf.write("\u00c0\3\2\2\2\u00c2\u00c1\3\2\2\2\u00c3\u00c6\3\2\2\2")
        buf.write("\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c7\3")
        buf.write("\2\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00c8\7$\2\2\u00c8\u00c9")
        buf.write("\b\b\4\2\u00c9\20\3\2\2\2\u00ca\u00cb\7^\2\2\u00cb\u00cf")
        buf.write("\t\6\2\2\u00cc\u00cd\7)\2\2\u00cd\u00cf\7$\2\2\u00ce\u00ca")
        buf.write("\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\22\3\2\2\2\u00d0\u00d1")
        buf.write("\7^\2\2\u00d1\u00d2\n\7\2\2\u00d2\24\3\2\2\2\u00d3\u00d4")
        buf.write("\n\b\2\2\u00d4\26\3\2\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7")
        buf.write("\7w\2\2\u00d7\u00d8\7v\2\2\u00d8\u00d9\7q\2\2\u00d9\30")
        buf.write("\3\2\2\2\u00da\u00db\7d\2\2\u00db\u00dc\7q\2\2\u00dc\u00dd")
        buf.write("\7q\2\2\u00dd\u00de\7n\2\2\u00de\u00df\7g\2\2\u00df\u00e0")
        buf.write("\7c\2\2\u00e0\u00e1\7p\2\2\u00e1\32\3\2\2\2\u00e2\u00e3")
        buf.write("\7k\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5\7v\2\2\u00e5\u00e6")
        buf.write("\7g\2\2\u00e6\u00e7\7i\2\2\u00e7\u00e8\7g\2\2\u00e8\u00e9")
        buf.write("\7t\2\2\u00e9\34\3\2\2\2\u00ea\u00eb\7h\2\2\u00eb\u00ec")
        buf.write("\7n\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee\7c\2\2\u00ee\u00ef")
        buf.write("\7v\2\2\u00ef\36\3\2\2\2\u00f0\u00f1\7u\2\2\u00f1\u00f2")
        buf.write("\7v\2\2\u00f2\u00f3\7t\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5")
        buf.write("\7p\2\2\u00f5\u00f6\7i\2\2\u00f6 \3\2\2\2\u00f7\u00f8")
        buf.write("\7c\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa\7t\2\2\u00fa\u00fb")
        buf.write("\7c\2\2\u00fb\u00fc\7{\2\2\u00fc\"\3\2\2\2\u00fd\u00fe")
        buf.write("\7d\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100\7g\2\2\u0100\u0101")
        buf.write("\7c\2\2\u0101\u0102\7m\2\2\u0102$\3\2\2\2\u0103\u0104")
        buf.write("\7f\2\2\u0104\u0105\7q\2\2\u0105&\3\2\2\2\u0106\u0107")
        buf.write("\7g\2\2\u0107\u0108\7n\2\2\u0108\u0109\7u\2\2\u0109\u010a")
        buf.write("\7g\2\2\u010a(\3\2\2\2\u010b\u010c\7k\2\2\u010c\u010d")
        buf.write("\7h\2\2\u010d*\3\2\2\2\u010e\u010f\7h\2\2\u010f\u0110")
        buf.write("\7w\2\2\u0110\u0111\7p\2\2\u0111\u0112\7e\2\2\u0112\u0113")
        buf.write("\7v\2\2\u0113\u0114\7k\2\2\u0114\u0115\7q\2\2\u0115\u0116")
        buf.write("\7p\2\2\u0116,\3\2\2\2\u0117\u0118\7h\2\2\u0118\u0119")
        buf.write("\7q\2\2\u0119\u011a\7t\2\2\u011a.\3\2\2\2\u011b\u011c")
        buf.write("\7h\2\2\u011c\u011d\7c\2\2\u011d\u011e\7n\2\2\u011e\u011f")
        buf.write("\7u\2\2\u011f\u0120\7g\2\2\u0120\60\3\2\2\2\u0121\u0122")
        buf.write("\7t\2\2\u0122\u0123\7g\2\2\u0123\u0124\7v\2\2\u0124\u0125")
        buf.write("\7w\2\2\u0125\u0126\7t\2\2\u0126\u0127\7p\2\2\u0127\62")
        buf.write("\3\2\2\2\u0128\u0129\7v\2\2\u0129\u012a\7t\2\2\u012a\u012b")
        buf.write("\7w\2\2\u012b\u012c\7g\2\2\u012c\64\3\2\2\2\u012d\u012e")
        buf.write("\7x\2\2\u012e\u012f\7q\2\2\u012f\u0130\7k\2\2\u0130\u0131")
        buf.write("\7f\2\2\u0131\66\3\2\2\2\u0132\u0133\7e\2\2\u0133\u0134")
        buf.write("\7q\2\2\u0134\u0135\7p\2\2\u0135\u0136\7v\2\2\u0136\u0137")
        buf.write("\7k\2\2\u0137\u0138\7p\2\2\u0138\u0139\7w\2\2\u0139\u013a")
        buf.write("\7g\2\2\u013a8\3\2\2\2\u013b\u013c\7q\2\2\u013c\u013d")
        buf.write("\7w\2\2\u013d\u013e\7v\2\2\u013e:\3\2\2\2\u013f\u0140")
        buf.write("\7y\2\2\u0140\u0141\7j\2\2\u0141\u0142\7k\2\2\u0142\u0143")
        buf.write("\7n\2\2\u0143\u0144\7g\2\2\u0144<\3\2\2\2\u0145\u0146")
        buf.write("\7q\2\2\u0146\u0147\7h\2\2\u0147>\3\2\2\2\u0148\u0149")
        buf.write("\7k\2\2\u0149\u014a\7p\2\2\u014a\u014b\7j\2\2\u014b\u014c")
        buf.write("\7g\2\2\u014c\u014d\7t\2\2\u014d\u014e\7k\2\2\u014e\u014f")
        buf.write("\7v\2\2\u014f@\3\2\2\2\u0150\u0151\7*\2\2\u0151B\3\2\2")
        buf.write("\2\u0152\u0153\7+\2\2\u0153D\3\2\2\2\u0154\u0155\7}\2")
        buf.write("\2\u0155F\3\2\2\2\u0156\u0157\7\177\2\2\u0157H\3\2\2\2")
        buf.write("\u0158\u0159\7]\2\2\u0159J\3\2\2\2\u015a\u015b\7_\2\2")
        buf.write("\u015bL\3\2\2\2\u015c\u015d\7.\2\2\u015dN\3\2\2\2\u015e")
        buf.write("\u015f\7\60\2\2\u015fP\3\2\2\2\u0160\u0161\7=\2\2\u0161")
        buf.write("R\3\2\2\2\u0162\u0163\7<\2\2\u0163T\3\2\2\2\u0164\u0165")
        buf.write("\7?\2\2\u0165V\3\2\2\2\u0166\u0167\7-\2\2\u0167X\3\2\2")
        buf.write("\2\u0168\u0169\7/\2\2\u0169Z\3\2\2\2\u016a\u016b\7,\2")
        buf.write("\2\u016b\\\3\2\2\2\u016c\u016d\7\61\2\2\u016d^\3\2\2\2")
        buf.write("\u016e\u016f\7\'\2\2\u016f`\3\2\2\2\u0170\u0171\7#\2\2")
        buf.write("\u0171b\3\2\2\2\u0172\u0173\7(\2\2\u0173\u0174\7(\2\2")
        buf.write("\u0174d\3\2\2\2\u0175\u0176\7~\2\2\u0176\u0177\7~\2\2")
        buf.write("\u0177f\3\2\2\2\u0178\u0179\7#\2\2\u0179\u017a\7?\2\2")
        buf.write("\u017ah\3\2\2\2\u017b\u017c\7?\2\2\u017c\u017d\7?\2\2")
        buf.write("\u017dj\3\2\2\2\u017e\u017f\7>\2\2\u017fl\3\2\2\2\u0180")
        buf.write("\u0181\7@\2\2\u0181n\3\2\2\2\u0182\u0183\7@\2\2\u0183")
        buf.write("\u0184\7?\2\2\u0184p\3\2\2\2\u0185\u0186\7>\2\2\u0186")
        buf.write("\u0187\7?\2\2\u0187r\3\2\2\2\u0188\u0189\7<\2\2\u0189")
        buf.write("\u018a\7<\2\2\u018at\3\2\2\2\u018b\u018f\t\t\2\2\u018c")
        buf.write("\u018e\t\n\2\2\u018d\u018c\3\2\2\2\u018e\u0191\3\2\2\2")
        buf.write("\u018f\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190v\3\2\2")
        buf.write("\2\u0191\u018f\3\2\2\2\u0192\u0193\7\61\2\2\u0193\u0194")
        buf.write("\7,\2\2\u0194\u0196\3\2\2\2\u0195\u0197\13\2\2\2\u0196")
        buf.write("\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0199\3\2\2\2")
        buf.write("\u0198\u0196\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u019b\7")
        buf.write(",\2\2\u019b\u019c\7\61\2\2\u019c\u019d\3\2\2\2\u019d\u019e")
        buf.write("\b<\5\2\u019ex\3\2\2\2\u019f\u01a0\7\61\2\2\u01a0\u01a1")
        buf.write("\7\61\2\2\u01a1\u01a5\3\2\2\2\u01a2\u01a4\n\13\2\2\u01a3")
        buf.write("\u01a2\3\2\2\2\u01a4\u01a7\3\2\2\2\u01a5\u01a3\3\2\2\2")
        buf.write("\u01a5\u01a6\3\2\2\2\u01a6\u01a8\3\2\2\2\u01a7\u01a5\3")
        buf.write("\2\2\2\u01a8\u01a9\b=\5\2\u01a9z\3\2\2\2\u01aa\u01ac\t")
        buf.write("\f\2\2\u01ab\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01ab")
        buf.write("\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01af\3\2\2\2\u01af")
        buf.write("\u01b0\b>\5\2\u01b0|\3\2\2\2\u01b1\u01b6\7$\2\2\u01b2")
        buf.write("\u01b5\5\25\13\2\u01b3\u01b5\5\21\t\2\u01b4\u01b2\3\2")
        buf.write("\2\2\u01b4\u01b3\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6\u01b4")
        buf.write("\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8")
        buf.write("\u01b6\3\2\2\2\u01b9\u01bb\t\r\2\2\u01ba\u01b9\3\2\2\2")
        buf.write("\u01bb\u01bc\3\2\2\2\u01bc\u01bd\b?\6\2\u01bd~\3\2\2\2")
        buf.write("\u01be\u01c3\7$\2\2\u01bf\u01c2\5\25\13\2\u01c0\u01c2")
        buf.write("\5\21\t\2\u01c1\u01bf\3\2\2\2\u01c1\u01c0\3\2\2\2\u01c2")
        buf.write("\u01c5\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2")
        buf.write("\u01c4\u01c6\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c6\u01c7\5")
        buf.write("\23\n\2\u01c7\u01c8\b@\7\2\u01c8\u0080\3\2\2\2\u01c9\u01ca")
        buf.write("\13\2\2\2\u01ca\u01cb\bA\b\2\u01cb\u0082\3\2\2\2\31\2")
        buf.write("\u0087\u008e\u0092\u0096\u009d\u00a5\u00ab\u00b0\u00b8")
        buf.write("\u00bd\u00c2\u00c4\u00ce\u018f\u0198\u01a5\u01ad\u01b4")
        buf.write("\u01b6\u01ba\u01c1\u01c3\t\3\2\2\3\3\3\3\b\4\b\2\2\3?")
        buf.write("\5\3@\6\3A\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT_LIT = 1
    FLOAT_LIT = 2
    BOOLEAN_LIT = 3
    STRING_LIT = 4
    AUTO = 5
    BOOLEAN = 6
    INTEGER = 7
    FLOAT = 8
    STRING = 9
    ARRAY = 10
    BREAK = 11
    DO = 12
    ELSE = 13
    IF = 14
    FUNCTION = 15
    FOR = 16
    FALSE = 17
    RETURN = 18
    TRUE = 19
    VOID = 20
    CONTINUE = 21
    OUT = 22
    WHILE = 23
    OF = 24
    INHERIT = 25
    LP = 26
    RP = 27
    LCB = 28
    RCB = 29
    LSB = 30
    RSB = 31
    COMMA = 32
    DOT = 33
    SEMI = 34
    COLON = 35
    ASSIGN = 36
    ADD = 37
    MINUS = 38
    MUL = 39
    DIV = 40
    MOD = 41
    NOT = 42
    AND = 43
    OR = 44
    NOT_EQ = 45
    EQUAL = 46
    LESS_THAN = 47
    GREATER_THAN = 48
    GT_EQ = 49
    LT_EQ = 50
    SCOPE_OP = 51
    ID = 52
    BLOCK_COMMENT = 53
    SINGLE_LINE_COMMENT = 54
    WS = 55
    UNCLOSE_STRING = 56
    ILLEGAL_ESCAPE = 57
    ERROR_CHAR = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'boolean'", "'integer'", "'float'", "'string'", "'array'", 
            "'break'", "'do'", "'else'", "'if'", "'function'", "'for'", 
            "'false'", "'return'", "'true'", "'void'", "'continue'", "'out'", 
            "'while'", "'of'", "'inherit'", "'('", "')'", "'{'", "'}'", 
            "'['", "']'", "','", "'.'", "';'", "':'", "'='", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'!='", "'=='", 
            "'<'", "'>'", "'>='", "'<='", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "INT_LIT", "FLOAT_LIT", "BOOLEAN_LIT", "STRING_LIT", "AUTO", 
            "BOOLEAN", "INTEGER", "FLOAT", "STRING", "ARRAY", "BREAK", "DO", 
            "ELSE", "IF", "FUNCTION", "FOR", "FALSE", "RETURN", "TRUE", 
            "VOID", "CONTINUE", "OUT", "WHILE", "OF", "INHERIT", "LP", "RP", 
            "LCB", "RCB", "LSB", "RSB", "COMMA", "DOT", "SEMI", "COLON", 
            "ASSIGN", "ADD", "MINUS", "MUL", "DIV", "MOD", "NOT", "AND", 
            "OR", "NOT_EQ", "EQUAL", "LESS_THAN", "GREATER_THAN", "GT_EQ", 
            "LT_EQ", "SCOPE_OP", "ID", "BLOCK_COMMENT", "SINGLE_LINE_COMMENT", 
            "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "INT_LIT", "FLOAT_LIT", "EXPONENT", "INT_PART", "FRACTION_PART", 
                  "BOOLEAN_LIT", "STRING_LIT", "ESC", "ESC_ERR", "STR_CHAR", 
                  "AUTO", "BOOLEAN", "INTEGER", "FLOAT", "STRING", "ARRAY", 
                  "BREAK", "DO", "ELSE", "IF", "FUNCTION", "FOR", "FALSE", 
                  "RETURN", "TRUE", "VOID", "CONTINUE", "OUT", "WHILE", 
                  "OF", "INHERIT", "LP", "RP", "LCB", "RCB", "LSB", "RSB", 
                  "COMMA", "DOT", "SEMI", "COLON", "ASSIGN", "ADD", "MINUS", 
                  "MUL", "DIV", "MOD", "NOT", "AND", "OR", "NOT_EQ", "EQUAL", 
                  "LESS_THAN", "GREATER_THAN", "GT_EQ", "LT_EQ", "SCOPE_OP", 
                  "ID", "BLOCK_COMMENT", "SINGLE_LINE_COMMENT", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[0] = self.INT_LIT_action 
            actions[1] = self.FLOAT_LIT_action 
            actions[6] = self.STRING_LIT_action 
            actions[61] = self.UNCLOSE_STRING_action 
            actions[62] = self.ILLEGAL_ESCAPE_action 
            actions[63] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                  self.text = self.text.replace('_', '')
                
     

    def FLOAT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                  self.text = self.text.replace('_', '')
                
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                  self.text = self.text[1:-1]
                
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                  newline_esc = '\n'
                  if self.text[-1] in newline_esc:
                    raise UncloseString(self.text[1:-1])
                  else:
                    raise UncloseString(self.text[1:])
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                  raise IllegalEscape(self.text[1:])
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                  raise ErrorToken(self.text)
                
     


