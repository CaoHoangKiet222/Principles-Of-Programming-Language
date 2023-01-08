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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\67")
        buf.write("\u01aa\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\3\2\3\2\7\2~\n\2\f\2\16\2\u0081\13")
        buf.write("\2\3\2\3\2\6\2\u0085\n\2\r\2\16\2\u0086\7\2\u0089\n\2")
        buf.write("\f\2\16\2\u008c\13\2\3\2\5\2\u008f\n\2\3\2\3\2\3\3\3\3")
        buf.write("\5\3\u0095\n\3\3\3\3\3\3\4\5\4\u009a\n\4\3\4\3\4\3\4\3")
        buf.write("\4\5\4\u00a0\n\4\3\5\3\5\5\5\u00a4\n\5\3\5\3\5\3\6\3\6")
        buf.write("\5\6\u00aa\n\6\3\6\6\6\u00ad\n\6\r\6\16\6\u00ae\3\7\3")
        buf.write("\7\3\b\3\b\7\b\u00b5\n\b\f\b\16\b\u00b8\13\b\3\t\3\t\5")
        buf.write("\t\u00bc\n\t\3\n\3\n\3\n\7\n\u00c1\n\n\f\n\16\n\u00c4")
        buf.write("\13\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3\"")
        buf.write("\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3")
        buf.write("*\3+\3+\3,\3,\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3")
        buf.write("\61\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\67\3\67\7\67\u0175\n\67\f")
        buf.write("\67\16\67\u0178\13\67\38\38\38\38\68\u017e\n8\r8\168\u017f")
        buf.write("\38\38\38\38\38\39\39\39\39\79\u018b\n9\f9\169\u018e\13")
        buf.write("9\39\39\3:\6:\u0193\n:\r:\16:\u0194\3:\3:\3;\3;\3;\3<")
        buf.write("\3<\3<\7<\u019f\n<\f<\16<\u01a2\13<\3<\5<\u01a5\n<\3<")
        buf.write("\3<\3=\3=\3\u017f\2>\3\3\5\4\7\2\t\2\13\2\r\2\17\2\21")
        buf.write("\5\23\6\25\2\27\2\31\7\33\b\35\t\37\n!\13#\f%\r\'\16)")
        buf.write("\17+\20-\21/\22\61\23\63\24\65\25\67\269\27;\30=\31?\32")
        buf.write("A\33C\34E\35G\36I\37K M!O\"Q#S$U%W&Y\'[(])_*a+c,e-g.i")
        buf.write("/k\60m\61o\62q\63s\64u\65w\66y\67\3\2\r\3\2\63;\3\2\62")
        buf.write(";\4\2GGgg\4\2--//\t\2))^^ddhhppttvv\4\2\f\f^^\5\2C\\a")
        buf.write("ac|\6\2\62;C\\aac|\4\2\f\f\17\17\5\2\13\f\17\17\"\"\3")
        buf.write("\3\f\f\2\u01b6\2\3\3\2\2\2\2\5\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2")
        buf.write("\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\3\u008e\3\2\2\2\5\u0094")
        buf.write("\3\2\2\2\7\u009f\3\2\2\2\t\u00a3\3\2\2\2\13\u00a7\3\2")
        buf.write("\2\2\r\u00b0\3\2\2\2\17\u00b2\3\2\2\2\21\u00bb\3\2\2\2")
        buf.write("\23\u00bd\3\2\2\2\25\u00c8\3\2\2\2\27\u00cb\3\2\2\2\31")
        buf.write("\u00cd\3\2\2\2\33\u00d2\3\2\2\2\35\u00d8\3\2\2\2\37\u00dd")
        buf.write("\3\2\2\2!\u00e0\3\2\2\2#\u00e5\3\2\2\2%\u00e8\3\2\2\2")
        buf.write("\'\u00f1\3\2\2\2)\u00f5\3\2\2\2+\u00fb\3\2\2\2-\u0101")
        buf.write("\3\2\2\2/\u0109\3\2\2\2\61\u0110\3\2\2\2\63\u0117\3\2")
        buf.write("\2\2\65\u011c\3\2\2\2\67\u0121\3\2\2\29\u012a\3\2\2\2")
        buf.write(";\u012e\3\2\2\2=\u0134\3\2\2\2?\u0137\3\2\2\2A\u013f\3")
        buf.write("\2\2\2C\u0141\3\2\2\2E\u0143\3\2\2\2G\u0145\3\2\2\2I\u0147")
        buf.write("\3\2\2\2K\u0149\3\2\2\2M\u014b\3\2\2\2O\u014d\3\2\2\2")
        buf.write("Q\u014f\3\2\2\2S\u0151\3\2\2\2U\u0153\3\2\2\2W\u0155\3")
        buf.write("\2\2\2Y\u0157\3\2\2\2[\u0159\3\2\2\2]\u015c\3\2\2\2_\u015f")
        buf.write("\3\2\2\2a\u0162\3\2\2\2c\u0165\3\2\2\2e\u0167\3\2\2\2")
        buf.write("g\u0169\3\2\2\2i\u016c\3\2\2\2k\u016f\3\2\2\2m\u0172\3")
        buf.write("\2\2\2o\u0179\3\2\2\2q\u0186\3\2\2\2s\u0192\3\2\2\2u\u0198")
        buf.write("\3\2\2\2w\u019b\3\2\2\2y\u01a8\3\2\2\2{\177\t\2\2\2|~")
        buf.write("\t\3\2\2}|\3\2\2\2~\u0081\3\2\2\2\177}\3\2\2\2\177\u0080")
        buf.write("\3\2\2\2\u0080\u008a\3\2\2\2\u0081\177\3\2\2\2\u0082\u0084")
        buf.write("\7a\2\2\u0083\u0085\t\3\2\2\u0084\u0083\3\2\2\2\u0085")
        buf.write("\u0086\3\2\2\2\u0086\u0084\3\2\2\2\u0086\u0087\3\2\2\2")
        buf.write("\u0087\u0089\3\2\2\2\u0088\u0082\3\2\2\2\u0089\u008c\3")
        buf.write("\2\2\2\u008a\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008f")
        buf.write("\3\2\2\2\u008c\u008a\3\2\2\2\u008d\u008f\7\62\2\2\u008e")
        buf.write("{\3\2\2\2\u008e\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090")
        buf.write("\u0091\b\2\2\2\u0091\4\3\2\2\2\u0092\u0095\5\7\4\2\u0093")
        buf.write("\u0095\5\t\5\2\u0094\u0092\3\2\2\2\u0094\u0093\3\2\2\2")
        buf.write("\u0095\u0096\3\2\2\2\u0096\u0097\b\3\3\2\u0097\6\3\2\2")
        buf.write("\2\u0098\u009a\5\r\7\2\u0099\u0098\3\2\2\2\u0099\u009a")
        buf.write("\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u00a0\5\17\b\2\u009c")
        buf.write("\u009d\5\r\7\2\u009d\u009e\7\60\2\2\u009e\u00a0\3\2\2")
        buf.write("\2\u009f\u0099\3\2\2\2\u009f\u009c\3\2\2\2\u00a0\b\3\2")
        buf.write("\2\2\u00a1\u00a4\5\7\4\2\u00a2\u00a4\5\r\7\2\u00a3\u00a1")
        buf.write("\3\2\2\2\u00a3\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5")
        buf.write("\u00a6\5\13\6\2\u00a6\n\3\2\2\2\u00a7\u00a9\t\4\2\2\u00a8")
        buf.write("\u00aa\t\5\2\2\u00a9\u00a8\3\2\2\2\u00a9\u00aa\3\2\2\2")
        buf.write("\u00aa\u00ac\3\2\2\2\u00ab\u00ad\t\3\2\2\u00ac\u00ab\3")
        buf.write("\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af")
        buf.write("\3\2\2\2\u00af\f\3\2\2\2\u00b0\u00b1\5\3\2\2\u00b1\16")
        buf.write("\3\2\2\2\u00b2\u00b6\7\60\2\2\u00b3\u00b5\t\3\2\2\u00b4")
        buf.write("\u00b3\3\2\2\2\u00b5\u00b8\3\2\2\2\u00b6\u00b4\3\2\2\2")
        buf.write("\u00b6\u00b7\3\2\2\2\u00b7\20\3\2\2\2\u00b8\u00b6\3\2")
        buf.write("\2\2\u00b9\u00bc\5\63\32\2\u00ba\u00bc\5+\26\2\u00bb\u00b9")
        buf.write("\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc\22\3\2\2\2\u00bd\u00c2")
        buf.write("\7$\2\2\u00be\u00c1\5\25\13\2\u00bf\u00c1\5\27\f\2\u00c0")
        buf.write("\u00be\3\2\2\2\u00c0\u00bf\3\2\2\2\u00c1\u00c4\3\2\2\2")
        buf.write("\u00c2\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c5\3")
        buf.write("\2\2\2\u00c4\u00c2\3\2\2\2\u00c5\u00c6\7$\2\2\u00c6\u00c7")
        buf.write("\b\n\4\2\u00c7\24\3\2\2\2\u00c8\u00c9\7^\2\2\u00c9\u00ca")
        buf.write("\t\6\2\2\u00ca\26\3\2\2\2\u00cb\u00cc\n\7\2\2\u00cc\30")
        buf.write("\3\2\2\2\u00cd\u00ce\7c\2\2\u00ce\u00cf\7w\2\2\u00cf\u00d0")
        buf.write("\7v\2\2\u00d0\u00d1\7q\2\2\u00d1\32\3\2\2\2\u00d2\u00d3")
        buf.write("\7d\2\2\u00d3\u00d4\7t\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6")
        buf.write("\7c\2\2\u00d6\u00d7\7m\2\2\u00d7\34\3\2\2\2\u00d8\u00d9")
        buf.write("\7d\2\2\u00d9\u00da\7q\2\2\u00da\u00db\7q\2\2\u00db\u00dc")
        buf.write("\7n\2\2\u00dc\36\3\2\2\2\u00dd\u00de\7f\2\2\u00de\u00df")
        buf.write("\7q\2\2\u00df \3\2\2\2\u00e0\u00e1\7g\2\2\u00e1\u00e2")
        buf.write("\7n\2\2\u00e2\u00e3\7u\2\2\u00e3\u00e4\7g\2\2\u00e4\"")
        buf.write("\3\2\2\2\u00e5\u00e6\7k\2\2\u00e6\u00e7\7h\2\2\u00e7$")
        buf.write("\3\2\2\2\u00e8\u00e9\7h\2\2\u00e9\u00ea\7w\2\2\u00ea\u00eb")
        buf.write("\7p\2\2\u00eb\u00ec\7e\2\2\u00ec\u00ed\7v\2\2\u00ed\u00ee")
        buf.write("\7k\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0\7p\2\2\u00f0&\3")
        buf.write("\2\2\2\u00f1\u00f2\7h\2\2\u00f2\u00f3\7q\2\2\u00f3\u00f4")
        buf.write("\7t\2\2\u00f4(\3\2\2\2\u00f5\u00f6\7h\2\2\u00f6\u00f7")
        buf.write("\7n\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9\7c\2\2\u00f9\u00fa")
        buf.write("\7v\2\2\u00fa*\3\2\2\2\u00fb\u00fc\7h\2\2\u00fc\u00fd")
        buf.write("\7c\2\2\u00fd\u00fe\7n\2\2\u00fe\u00ff\7u\2\2\u00ff\u0100")
        buf.write("\7g\2\2\u0100,\3\2\2\2\u0101\u0102\7k\2\2\u0102\u0103")
        buf.write("\7p\2\2\u0103\u0104\7v\2\2\u0104\u0105\7g\2\2\u0105\u0106")
        buf.write("\7i\2\2\u0106\u0107\7g\2\2\u0107\u0108\7t\2\2\u0108.\3")
        buf.write("\2\2\2\u0109\u010a\7t\2\2\u010a\u010b\7g\2\2\u010b\u010c")
        buf.write("\7v\2\2\u010c\u010d\7w\2\2\u010d\u010e\7t\2\2\u010e\u010f")
        buf.write("\7p\2\2\u010f\60\3\2\2\2\u0110\u0111\7u\2\2\u0111\u0112")
        buf.write("\7v\2\2\u0112\u0113\7t\2\2\u0113\u0114\7k\2\2\u0114\u0115")
        buf.write("\7p\2\2\u0115\u0116\7i\2\2\u0116\62\3\2\2\2\u0117\u0118")
        buf.write("\7v\2\2\u0118\u0119\7t\2\2\u0119\u011a\7w\2\2\u011a\u011b")
        buf.write("\7g\2\2\u011b\64\3\2\2\2\u011c\u011d\7x\2\2\u011d\u011e")
        buf.write("\7q\2\2\u011e\u011f\7k\2\2\u011f\u0120\7f\2\2\u0120\66")
        buf.write("\3\2\2\2\u0121\u0122\7e\2\2\u0122\u0123\7q\2\2\u0123\u0124")
        buf.write("\7p\2\2\u0124\u0125\7v\2\2\u0125\u0126\7k\2\2\u0126\u0127")
        buf.write("\7p\2\2\u0127\u0128\7w\2\2\u0128\u0129\7g\2\2\u01298\3")
        buf.write("\2\2\2\u012a\u012b\7q\2\2\u012b\u012c\7w\2\2\u012c\u012d")
        buf.write("\7v\2\2\u012d:\3\2\2\2\u012e\u012f\7y\2\2\u012f\u0130")
        buf.write("\7j\2\2\u0130\u0131\7k\2\2\u0131\u0132\7n\2\2\u0132\u0133")
        buf.write("\7g\2\2\u0133<\3\2\2\2\u0134\u0135\7q\2\2\u0135\u0136")
        buf.write("\7h\2\2\u0136>\3\2\2\2\u0137\u0138\7k\2\2\u0138\u0139")
        buf.write("\7p\2\2\u0139\u013a\7j\2\2\u013a\u013b\7g\2\2\u013b\u013c")
        buf.write("\7t\2\2\u013c\u013d\7k\2\2\u013d\u013e\7v\2\2\u013e@\3")
        buf.write("\2\2\2\u013f\u0140\7*\2\2\u0140B\3\2\2\2\u0141\u0142\7")
        buf.write("+\2\2\u0142D\3\2\2\2\u0143\u0144\7}\2\2\u0144F\3\2\2\2")
        buf.write("\u0145\u0146\7\177\2\2\u0146H\3\2\2\2\u0147\u0148\7]\2")
        buf.write("\2\u0148J\3\2\2\2\u0149\u014a\7_\2\2\u014aL\3\2\2\2\u014b")
        buf.write("\u014c\7.\2\2\u014cN\3\2\2\2\u014d\u014e\7-\2\2\u014e")
        buf.write("P\3\2\2\2\u014f\u0150\7/\2\2\u0150R\3\2\2\2\u0151\u0152")
        buf.write("\7,\2\2\u0152T\3\2\2\2\u0153\u0154\7\61\2\2\u0154V\3\2")
        buf.write("\2\2\u0155\u0156\7\'\2\2\u0156X\3\2\2\2\u0157\u0158\7")
        buf.write("#\2\2\u0158Z\3\2\2\2\u0159\u015a\7(\2\2\u015a\u015b\7")
        buf.write("(\2\2\u015b\\\3\2\2\2\u015c\u015d\7~\2\2\u015d\u015e\7")
        buf.write("~\2\2\u015e^\3\2\2\2\u015f\u0160\7#\2\2\u0160\u0161\7")
        buf.write("?\2\2\u0161`\3\2\2\2\u0162\u0163\7?\2\2\u0163\u0164\7")
        buf.write("?\2\2\u0164b\3\2\2\2\u0165\u0166\7>\2\2\u0166d\3\2\2\2")
        buf.write("\u0167\u0168\7@\2\2\u0168f\3\2\2\2\u0169\u016a\7@\2\2")
        buf.write("\u016a\u016b\7?\2\2\u016bh\3\2\2\2\u016c\u016d\7>\2\2")
        buf.write("\u016d\u016e\7?\2\2\u016ej\3\2\2\2\u016f\u0170\7<\2\2")
        buf.write("\u0170\u0171\7<\2\2\u0171l\3\2\2\2\u0172\u0176\t\b\2\2")
        buf.write("\u0173\u0175\t\t\2\2\u0174\u0173\3\2\2\2\u0175\u0178\3")
        buf.write("\2\2\2\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177n")
        buf.write("\3\2\2\2\u0178\u0176\3\2\2\2\u0179\u017a\7\61\2\2\u017a")
        buf.write("\u017b\7,\2\2\u017b\u017d\3\2\2\2\u017c\u017e\13\2\2\2")
        buf.write("\u017d\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0180\3")
        buf.write("\2\2\2\u017f\u017d\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0182")
        buf.write("\7,\2\2\u0182\u0183\7\61\2\2\u0183\u0184\3\2\2\2\u0184")
        buf.write("\u0185\b8\5\2\u0185p\3\2\2\2\u0186\u0187\7\61\2\2\u0187")
        buf.write("\u0188\7\61\2\2\u0188\u018c\3\2\2\2\u0189\u018b\n\n\2")
        buf.write("\2\u018a\u0189\3\2\2\2\u018b\u018e\3\2\2\2\u018c\u018a")
        buf.write("\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018f\3\2\2\2\u018e")
        buf.write("\u018c\3\2\2\2\u018f\u0190\b9\5\2\u0190r\3\2\2\2\u0191")
        buf.write("\u0193\t\13\2\2\u0192\u0191\3\2\2\2\u0193\u0194\3\2\2")
        buf.write("\2\u0194\u0192\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0196")
        buf.write("\3\2\2\2\u0196\u0197\b:\5\2\u0197t\3\2\2\2\u0198\u0199")
        buf.write("\13\2\2\2\u0199\u019a\b;\6\2\u019av\3\2\2\2\u019b\u01a0")
        buf.write("\7$\2\2\u019c\u019f\5\27\f\2\u019d\u019f\5\25\13\2\u019e")
        buf.write("\u019c\3\2\2\2\u019e\u019d\3\2\2\2\u019f\u01a2\3\2\2\2")
        buf.write("\u01a0\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a4\3")
        buf.write("\2\2\2\u01a2\u01a0\3\2\2\2\u01a3\u01a5\t\f\2\2\u01a4\u01a3")
        buf.write("\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a7\b<\7\2\u01a7")
        buf.write("x\3\2\2\2\u01a8\u01a9\13\2\2\2\u01a9z\3\2\2\2\30\2\177")
        buf.write("\u0086\u008a\u008e\u0094\u0099\u009f\u00a3\u00a9\u00ae")
        buf.write("\u00b6\u00bb\u00c0\u00c2\u0176\u017f\u018c\u0194\u019e")
        buf.write("\u01a0\u01a4\b\3\2\2\3\3\3\3\n\4\b\2\2\3;\5\3<\6")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT_LIT = 1
    FLOAT_LIT = 2
    BOOLEAN_LIT = 3
    STRING_LIT = 4
    AUTO = 5
    BREAK = 6
    BOOL = 7
    DO = 8
    ELSE = 9
    IF = 10
    FUNCTION = 11
    FOR = 12
    FLOAT_KQ = 13
    FALSE = 14
    INTEGER_KQ = 15
    RETURN = 16
    STRING = 17
    TRUE = 18
    VOID = 19
    CONTINUE = 20
    OUT = 21
    WHILE = 22
    OF = 23
    INHERIT = 24
    LP = 25
    RP = 26
    LCB = 27
    RCB = 28
    LSB = 29
    RSB = 30
    COMMA = 31
    ADD = 32
    MINUS = 33
    MUL = 34
    DIV = 35
    MOD = 36
    NOT = 37
    AND = 38
    OR = 39
    NOT_EQ = 40
    EQUALS = 41
    LESS_THAN = 42
    GREATER_THAN = 43
    GT_EQ = 44
    LT_EQ = 45
    SCOPE_OP = 46
    ID = 47
    BLOCK_COMMENT = 48
    SINGLE_LINE_COMMENT = 49
    WS = 50
    ERROR_CHAR = 51
    UNCLOSE_STRING = 52
    ILLEGAL_ESCAPE = 53

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'bool'", "'do'", "'else'", "'if'", "'function'", 
            "'for'", "'float'", "'false'", "'integer'", "'return'", "'string'", 
            "'true'", "'void'", "'continue'", "'out'", "'while'", "'of'", 
            "'inherit'", "'('", "')'", "'{'", "'}'", "'['", "']'", "','", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'!='", 
            "'=='", "'<'", "'>'", "'>='", "'<='", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "INT_LIT", "FLOAT_LIT", "BOOLEAN_LIT", "STRING_LIT", "AUTO", 
            "BREAK", "BOOL", "DO", "ELSE", "IF", "FUNCTION", "FOR", "FLOAT_KQ", 
            "FALSE", "INTEGER_KQ", "RETURN", "STRING", "TRUE", "VOID", "CONTINUE", 
            "OUT", "WHILE", "OF", "INHERIT", "LP", "RP", "LCB", "RCB", "LSB", 
            "RSB", "COMMA", "ADD", "MINUS", "MUL", "DIV", "MOD", "NOT", 
            "AND", "OR", "NOT_EQ", "EQUALS", "LESS_THAN", "GREATER_THAN", 
            "GT_EQ", "LT_EQ", "SCOPE_OP", "ID", "BLOCK_COMMENT", "SINGLE_LINE_COMMENT", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INT_LIT", "FLOAT_LIT", "POINT_FLOAT", "EXPONENT_FLOAT", 
                  "EXPONENT", "INT_PART", "FRACTION_PART", "BOOLEAN_LIT", 
                  "STRING_LIT", "ESC", "STR_CHAR", "AUTO", "BREAK", "BOOL", 
                  "DO", "ELSE", "IF", "FUNCTION", "FOR", "FLOAT_KQ", "FALSE", 
                  "INTEGER_KQ", "RETURN", "STRING", "TRUE", "VOID", "CONTINUE", 
                  "OUT", "WHILE", "OF", "INHERIT", "LP", "RP", "LCB", "RCB", 
                  "LSB", "RSB", "COMMA", "ADD", "MINUS", "MUL", "DIV", "MOD", 
                  "NOT", "AND", "OR", "NOT_EQ", "EQUALS", "LESS_THAN", "GREATER_THAN", 
                  "GT_EQ", "LT_EQ", "SCOPE_OP", "ID", "BLOCK_COMMENT", "SINGLE_LINE_COMMENT", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[8] = self.STRING_LIT_action 
            actions[57] = self.ERROR_CHAR_action 
            actions[58] = self.UNCLOSE_STRING_action 
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

                  content = str(self.text) 
                  self.text = content[1:-1]
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                  raise ErrorToken(self.text)
                
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                  newline_esc = '\n'
                  if self.text[-1] in newline_esc:
                    raise UncloseString(self.text[1:-1])
                  else:
                    raise UncloseString(self.text[1:])
                
     


