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
        buf.write("\u01d6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\3\2\3\2\7\2\u008a\n\2\f\2\16\2\u008d\13\2\3\2\3\2\6")
        buf.write("\2\u0091\n\2\r\2\16\2\u0092\7\2\u0095\n\2\f\2\16\2\u0098")
        buf.write("\13\2\3\2\5\2\u009b\n\2\3\2\3\2\3\3\3\3\5\3\u00a1\n\3")
        buf.write("\3\3\3\3\3\4\5\4\u00a6\n\4\3\4\3\4\3\4\3\4\5\4\u00ac\n")
        buf.write("\4\3\5\3\5\5\5\u00b0\n\5\3\5\3\5\3\6\3\6\5\6\u00b6\n\6")
        buf.write("\3\6\6\6\u00b9\n\6\r\6\16\6\u00ba\3\7\3\7\3\b\3\b\7\b")
        buf.write("\u00c1\n\b\f\b\16\b\u00c4\13\b\3\t\3\t\5\t\u00c8\n\t\3")
        buf.write("\n\3\n\3\n\7\n\u00cd\n\n\f\n\16\n\u00d0\13\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\5\13\u00d9\n\13\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3")
        buf.write("$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3")
        buf.write(",\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\38\38\39\39\3:\3:\3:\3;\3;\3;\3<\3<\3<\3=\3")
        buf.write("=\7=\u0198\n=\f=\16=\u019b\13=\3>\3>\3>\3>\6>\u01a1\n")
        buf.write(">\r>\16>\u01a2\3>\3>\3>\3>\3>\3?\3?\3?\3?\7?\u01ae\n?")
        buf.write("\f?\16?\u01b1\13?\3?\3?\3@\6@\u01b6\n@\r@\16@\u01b7\3")
        buf.write("@\3@\3A\3A\3A\7A\u01bf\nA\fA\16A\u01c2\13A\3A\5A\u01c5")
        buf.write("\nA\3A\3A\3B\3B\3B\7B\u01cc\nB\fB\16B\u01cf\13B\3B\3B")
        buf.write("\3B\3C\3C\3C\3\u01a2\2D\3\3\5\4\7\2\t\2\13\2\r\2\17\2")
        buf.write("\21\5\23\6\25\2\27\2\31\2\33\7\35\b\37\t!\n#\13%\f\'\r")
        buf.write(")\16+\17-\20/\21\61\22\63\23\65\24\67\259\26;\27=\30?")
        buf.write("\31A\32C\33E\34G\35I\36K\37M O!Q\"S#U$W%Y&[\'](_)a*c+")
        buf.write("e,g-i.k/m\60o\61q\62s\63u\64w\65y\66{\67}8\1779\u0081")
        buf.write(":\u0083;\u0085<\3\2\16\3\2\63;\3\2\62;\4\2GGgg\4\2--/")
        buf.write("/\n\2$$))^^ddhhppttvv\t\2))^^ddhhppttvv\5\2\f\f$$^^\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\4\2\f\f\17\17\5\2\13\f\17\17")
        buf.write("\"\"\3\3\f\f\2\u01e4\2\3\3\2\2\2\2\5\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2")
        buf.write("\3\u009a\3\2\2\2\5\u00a0\3\2\2\2\7\u00ab\3\2\2\2\t\u00af")
        buf.write("\3\2\2\2\13\u00b3\3\2\2\2\r\u00bc\3\2\2\2\17\u00be\3\2")
        buf.write("\2\2\21\u00c7\3\2\2\2\23\u00c9\3\2\2\2\25\u00d8\3\2\2")
        buf.write("\2\27\u00da\3\2\2\2\31\u00dd\3\2\2\2\33\u00df\3\2\2\2")
        buf.write("\35\u00e4\3\2\2\2\37\u00ec\3\2\2\2!\u00f4\3\2\2\2#\u00fa")
        buf.write("\3\2\2\2%\u0101\3\2\2\2\'\u0107\3\2\2\2)\u010d\3\2\2\2")
        buf.write("+\u0110\3\2\2\2-\u0115\3\2\2\2/\u0118\3\2\2\2\61\u0121")
        buf.write("\3\2\2\2\63\u0125\3\2\2\2\65\u012b\3\2\2\2\67\u0132\3")
        buf.write("\2\2\29\u0137\3\2\2\2;\u013c\3\2\2\2=\u0145\3\2\2\2?\u0149")
        buf.write("\3\2\2\2A\u014f\3\2\2\2C\u0152\3\2\2\2E\u015a\3\2\2\2")
        buf.write("G\u015c\3\2\2\2I\u015e\3\2\2\2K\u0160\3\2\2\2M\u0162\3")
        buf.write("\2\2\2O\u0164\3\2\2\2Q\u0166\3\2\2\2S\u0168\3\2\2\2U\u016a")
        buf.write("\3\2\2\2W\u016c\3\2\2\2Y\u016e\3\2\2\2[\u0170\3\2\2\2")
        buf.write("]\u0172\3\2\2\2_\u0174\3\2\2\2a\u0176\3\2\2\2c\u0178\3")
        buf.write("\2\2\2e\u017a\3\2\2\2g\u017c\3\2\2\2i\u017f\3\2\2\2k\u0182")
        buf.write("\3\2\2\2m\u0185\3\2\2\2o\u0188\3\2\2\2q\u018a\3\2\2\2")
        buf.write("s\u018c\3\2\2\2u\u018f\3\2\2\2w\u0192\3\2\2\2y\u0195\3")
        buf.write("\2\2\2{\u019c\3\2\2\2}\u01a9\3\2\2\2\177\u01b5\3\2\2\2")
        buf.write("\u0081\u01bb\3\2\2\2\u0083\u01c8\3\2\2\2\u0085\u01d3\3")
        buf.write("\2\2\2\u0087\u008b\t\2\2\2\u0088\u008a\t\3\2\2\u0089\u0088")
        buf.write("\3\2\2\2\u008a\u008d\3\2\2\2\u008b\u0089\3\2\2\2\u008b")
        buf.write("\u008c\3\2\2\2\u008c\u0096\3\2\2\2\u008d\u008b\3\2\2\2")
        buf.write("\u008e\u0090\7a\2\2\u008f\u0091\t\3\2\2\u0090\u008f\3")
        buf.write("\2\2\2\u0091\u0092\3\2\2\2\u0092\u0090\3\2\2\2\u0092\u0093")
        buf.write("\3\2\2\2\u0093\u0095\3\2\2\2\u0094\u008e\3\2\2\2\u0095")
        buf.write("\u0098\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2")
        buf.write("\u0097\u009b\3\2\2\2\u0098\u0096\3\2\2\2\u0099\u009b\7")
        buf.write("\62\2\2\u009a\u0087\3\2\2\2\u009a\u0099\3\2\2\2\u009b")
        buf.write("\u009c\3\2\2\2\u009c\u009d\b\2\2\2\u009d\4\3\2\2\2\u009e")
        buf.write("\u00a1\5\7\4\2\u009f\u00a1\5\t\5\2\u00a0\u009e\3\2\2\2")
        buf.write("\u00a0\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\b")
        buf.write("\3\3\2\u00a3\6\3\2\2\2\u00a4\u00a6\5\r\7\2\u00a5\u00a4")
        buf.write("\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7")
        buf.write("\u00ac\5\17\b\2\u00a8\u00a9\5\r\7\2\u00a9\u00aa\7\60\2")
        buf.write("\2\u00aa\u00ac\3\2\2\2\u00ab\u00a5\3\2\2\2\u00ab\u00a8")
        buf.write("\3\2\2\2\u00ac\b\3\2\2\2\u00ad\u00b0\5\7\4\2\u00ae\u00b0")
        buf.write("\5\r\7\2\u00af\u00ad\3\2\2\2\u00af\u00ae\3\2\2\2\u00b0")
        buf.write("\u00b1\3\2\2\2\u00b1\u00b2\5\13\6\2\u00b2\n\3\2\2\2\u00b3")
        buf.write("\u00b5\t\4\2\2\u00b4\u00b6\t\5\2\2\u00b5\u00b4\3\2\2\2")
        buf.write("\u00b5\u00b6\3\2\2\2\u00b6\u00b8\3\2\2\2\u00b7\u00b9\t")
        buf.write("\3\2\2\u00b8\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00b8")
        buf.write("\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\f\3\2\2\2\u00bc\u00bd")
        buf.write("\5\3\2\2\u00bd\16\3\2\2\2\u00be\u00c2\7\60\2\2\u00bf\u00c1")
        buf.write("\t\3\2\2\u00c0\u00bf\3\2\2\2\u00c1\u00c4\3\2\2\2\u00c2")
        buf.write("\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\20\3\2\2\2\u00c4")
        buf.write("\u00c2\3\2\2\2\u00c5\u00c8\5\67\34\2\u00c6\u00c8\5\63")
        buf.write("\32\2\u00c7\u00c5\3\2\2\2\u00c7\u00c6\3\2\2\2\u00c8\22")
        buf.write("\3\2\2\2\u00c9\u00ce\7$\2\2\u00ca\u00cd\5\25\13\2\u00cb")
        buf.write("\u00cd\5\31\r\2\u00cc\u00ca\3\2\2\2\u00cc\u00cb\3\2\2")
        buf.write("\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf")
        buf.write("\3\2\2\2\u00cf\u00d1\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1")
        buf.write("\u00d2\7$\2\2\u00d2\u00d3\b\n\4\2\u00d3\24\3\2\2\2\u00d4")
        buf.write("\u00d5\7^\2\2\u00d5\u00d9\t\6\2\2\u00d6\u00d7\7)\2\2\u00d7")
        buf.write("\u00d9\7$\2\2\u00d8\u00d4\3\2\2\2\u00d8\u00d6\3\2\2\2")
        buf.write("\u00d9\26\3\2\2\2\u00da\u00db\7^\2\2\u00db\u00dc\n\7\2")
        buf.write("\2\u00dc\30\3\2\2\2\u00dd\u00de\n\b\2\2\u00de\32\3\2\2")
        buf.write("\2\u00df\u00e0\7c\2\2\u00e0\u00e1\7w\2\2\u00e1\u00e2\7")
        buf.write("v\2\2\u00e2\u00e3\7q\2\2\u00e3\34\3\2\2\2\u00e4\u00e5")
        buf.write("\7d\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8")
        buf.write("\7n\2\2\u00e8\u00e9\7g\2\2\u00e9\u00ea\7c\2\2\u00ea\u00eb")
        buf.write("\7p\2\2\u00eb\36\3\2\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee")
        buf.write("\7p\2\2\u00ee\u00ef\7v\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1")
        buf.write("\7i\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3\7t\2\2\u00f3 \3")
        buf.write("\2\2\2\u00f4\u00f5\7h\2\2\u00f5\u00f6\7n\2\2\u00f6\u00f7")
        buf.write("\7q\2\2\u00f7\u00f8\7c\2\2\u00f8\u00f9\7v\2\2\u00f9\"")
        buf.write("\3\2\2\2\u00fa\u00fb\7u\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd")
        buf.write("\7t\2\2\u00fd\u00fe\7k\2\2\u00fe\u00ff\7p\2\2\u00ff\u0100")
        buf.write("\7i\2\2\u0100$\3\2\2\2\u0101\u0102\7c\2\2\u0102\u0103")
        buf.write("\7t\2\2\u0103\u0104\7t\2\2\u0104\u0105\7c\2\2\u0105\u0106")
        buf.write("\7{\2\2\u0106&\3\2\2\2\u0107\u0108\7d\2\2\u0108\u0109")
        buf.write("\7t\2\2\u0109\u010a\7g\2\2\u010a\u010b\7c\2\2\u010b\u010c")
        buf.write("\7m\2\2\u010c(\3\2\2\2\u010d\u010e\7f\2\2\u010e\u010f")
        buf.write("\7q\2\2\u010f*\3\2\2\2\u0110\u0111\7g\2\2\u0111\u0112")
        buf.write("\7n\2\2\u0112\u0113\7u\2\2\u0113\u0114\7g\2\2\u0114,\3")
        buf.write("\2\2\2\u0115\u0116\7k\2\2\u0116\u0117\7h\2\2\u0117.\3")
        buf.write("\2\2\2\u0118\u0119\7h\2\2\u0119\u011a\7w\2\2\u011a\u011b")
        buf.write("\7p\2\2\u011b\u011c\7e\2\2\u011c\u011d\7v\2\2\u011d\u011e")
        buf.write("\7k\2\2\u011e\u011f\7q\2\2\u011f\u0120\7p\2\2\u0120\60")
        buf.write("\3\2\2\2\u0121\u0122\7h\2\2\u0122\u0123\7q\2\2\u0123\u0124")
        buf.write("\7t\2\2\u0124\62\3\2\2\2\u0125\u0126\7h\2\2\u0126\u0127")
        buf.write("\7c\2\2\u0127\u0128\7n\2\2\u0128\u0129\7u\2\2\u0129\u012a")
        buf.write("\7g\2\2\u012a\64\3\2\2\2\u012b\u012c\7t\2\2\u012c\u012d")
        buf.write("\7g\2\2\u012d\u012e\7v\2\2\u012e\u012f\7w\2\2\u012f\u0130")
        buf.write("\7t\2\2\u0130\u0131\7p\2\2\u0131\66\3\2\2\2\u0132\u0133")
        buf.write("\7v\2\2\u0133\u0134\7t\2\2\u0134\u0135\7w\2\2\u0135\u0136")
        buf.write("\7g\2\2\u01368\3\2\2\2\u0137\u0138\7x\2\2\u0138\u0139")
        buf.write("\7q\2\2\u0139\u013a\7k\2\2\u013a\u013b\7f\2\2\u013b:\3")
        buf.write("\2\2\2\u013c\u013d\7e\2\2\u013d\u013e\7q\2\2\u013e\u013f")
        buf.write("\7p\2\2\u013f\u0140\7v\2\2\u0140\u0141\7k\2\2\u0141\u0142")
        buf.write("\7p\2\2\u0142\u0143\7w\2\2\u0143\u0144\7g\2\2\u0144<\3")
        buf.write("\2\2\2\u0145\u0146\7q\2\2\u0146\u0147\7w\2\2\u0147\u0148")
        buf.write("\7v\2\2\u0148>\3\2\2\2\u0149\u014a\7y\2\2\u014a\u014b")
        buf.write("\7j\2\2\u014b\u014c\7k\2\2\u014c\u014d\7n\2\2\u014d\u014e")
        buf.write("\7g\2\2\u014e@\3\2\2\2\u014f\u0150\7q\2\2\u0150\u0151")
        buf.write("\7h\2\2\u0151B\3\2\2\2\u0152\u0153\7k\2\2\u0153\u0154")
        buf.write("\7p\2\2\u0154\u0155\7j\2\2\u0155\u0156\7g\2\2\u0156\u0157")
        buf.write("\7t\2\2\u0157\u0158\7k\2\2\u0158\u0159\7v\2\2\u0159D\3")
        buf.write("\2\2\2\u015a\u015b\7*\2\2\u015bF\3\2\2\2\u015c\u015d\7")
        buf.write("+\2\2\u015dH\3\2\2\2\u015e\u015f\7}\2\2\u015fJ\3\2\2\2")
        buf.write("\u0160\u0161\7\177\2\2\u0161L\3\2\2\2\u0162\u0163\7]\2")
        buf.write("\2\u0163N\3\2\2\2\u0164\u0165\7_\2\2\u0165P\3\2\2\2\u0166")
        buf.write("\u0167\7.\2\2\u0167R\3\2\2\2\u0168\u0169\7\60\2\2\u0169")
        buf.write("T\3\2\2\2\u016a\u016b\7=\2\2\u016bV\3\2\2\2\u016c\u016d")
        buf.write("\7<\2\2\u016dX\3\2\2\2\u016e\u016f\7?\2\2\u016fZ\3\2\2")
        buf.write("\2\u0170\u0171\7-\2\2\u0171\\\3\2\2\2\u0172\u0173\7/\2")
        buf.write("\2\u0173^\3\2\2\2\u0174\u0175\7,\2\2\u0175`\3\2\2\2\u0176")
        buf.write("\u0177\7\61\2\2\u0177b\3\2\2\2\u0178\u0179\7\'\2\2\u0179")
        buf.write("d\3\2\2\2\u017a\u017b\7#\2\2\u017bf\3\2\2\2\u017c\u017d")
        buf.write("\7(\2\2\u017d\u017e\7(\2\2\u017eh\3\2\2\2\u017f\u0180")
        buf.write("\7~\2\2\u0180\u0181\7~\2\2\u0181j\3\2\2\2\u0182\u0183")
        buf.write("\7#\2\2\u0183\u0184\7?\2\2\u0184l\3\2\2\2\u0185\u0186")
        buf.write("\7?\2\2\u0186\u0187\7?\2\2\u0187n\3\2\2\2\u0188\u0189")
        buf.write("\7>\2\2\u0189p\3\2\2\2\u018a\u018b\7@\2\2\u018br\3\2\2")
        buf.write("\2\u018c\u018d\7@\2\2\u018d\u018e\7?\2\2\u018et\3\2\2")
        buf.write("\2\u018f\u0190\7>\2\2\u0190\u0191\7?\2\2\u0191v\3\2\2")
        buf.write("\2\u0192\u0193\7<\2\2\u0193\u0194\7<\2\2\u0194x\3\2\2")
        buf.write("\2\u0195\u0199\t\t\2\2\u0196\u0198\t\n\2\2\u0197\u0196")
        buf.write("\3\2\2\2\u0198\u019b\3\2\2\2\u0199\u0197\3\2\2\2\u0199")
        buf.write("\u019a\3\2\2\2\u019az\3\2\2\2\u019b\u0199\3\2\2\2\u019c")
        buf.write("\u019d\7\61\2\2\u019d\u019e\7,\2\2\u019e\u01a0\3\2\2\2")
        buf.write("\u019f\u01a1\13\2\2\2\u01a0\u019f\3\2\2\2\u01a1\u01a2")
        buf.write("\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a3")
        buf.write("\u01a4\3\2\2\2\u01a4\u01a5\7,\2\2\u01a5\u01a6\7\61\2\2")
        buf.write("\u01a6\u01a7\3\2\2\2\u01a7\u01a8\b>\5\2\u01a8|\3\2\2\2")
        buf.write("\u01a9\u01aa\7\61\2\2\u01aa\u01ab\7\61\2\2\u01ab\u01af")
        buf.write("\3\2\2\2\u01ac\u01ae\n\13\2\2\u01ad\u01ac\3\2\2\2\u01ae")
        buf.write("\u01b1\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2")
        buf.write("\u01b0\u01b2\3\2\2\2\u01b1\u01af\3\2\2\2\u01b2\u01b3\b")
        buf.write("?\5\2\u01b3~\3\2\2\2\u01b4\u01b6\t\f\2\2\u01b5\u01b4\3")
        buf.write("\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8")
        buf.write("\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01ba\b@\5\2\u01ba")
        buf.write("\u0080\3\2\2\2\u01bb\u01c0\7$\2\2\u01bc\u01bf\5\31\r\2")
        buf.write("\u01bd\u01bf\5\25\13\2\u01be\u01bc\3\2\2\2\u01be\u01bd")
        buf.write("\3\2\2\2\u01bf\u01c2\3\2\2\2\u01c0\u01be\3\2\2\2\u01c0")
        buf.write("\u01c1\3\2\2\2\u01c1\u01c4\3\2\2\2\u01c2\u01c0\3\2\2\2")
        buf.write("\u01c3\u01c5\t\r\2\2\u01c4\u01c3\3\2\2\2\u01c5\u01c6\3")
        buf.write("\2\2\2\u01c6\u01c7\bA\6\2\u01c7\u0082\3\2\2\2\u01c8\u01cd")
        buf.write("\7$\2\2\u01c9\u01cc\5\31\r\2\u01ca\u01cc\5\25\13\2\u01cb")
        buf.write("\u01c9\3\2\2\2\u01cb\u01ca\3\2\2\2\u01cc\u01cf\3\2\2\2")
        buf.write("\u01cd\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01d0\3")
        buf.write("\2\2\2\u01cf\u01cd\3\2\2\2\u01d0\u01d1\5\27\f\2\u01d1")
        buf.write("\u01d2\bB\7\2\u01d2\u0084\3\2\2\2\u01d3\u01d4\13\2\2\2")
        buf.write("\u01d4\u01d5\bC\b\2\u01d5\u0086\3\2\2\2\33\2\u008b\u0092")
        buf.write("\u0096\u009a\u00a0\u00a5\u00ab\u00af\u00b5\u00ba\u00c2")
        buf.write("\u00c7\u00cc\u00ce\u00d8\u0199\u01a2\u01af\u01b7\u01be")
        buf.write("\u01c0\u01c4\u01cb\u01cd\t\3\2\2\3\3\3\3\n\4\b\2\2\3A")
        buf.write("\5\3B\6\3C\7")
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

    ruleNames = [ "INT_LIT", "FLOAT_LIT", "POINT_FLOAT", "EXPONENT_FLOAT", 
                  "EXPONENT", "INT_PART", "FRACTION_PART", "BOOLEAN_LIT", 
                  "STRING_LIT", "ESC", "ESC_ERR", "STR_CHAR", "AUTO", "BOOLEAN", 
                  "INTEGER", "FLOAT", "STRING", "ARRAY", "BREAK", "DO", 
                  "ELSE", "IF", "FUNCTION", "FOR", "FALSE", "RETURN", "TRUE", 
                  "VOID", "CONTINUE", "OUT", "WHILE", "OF", "INHERIT", "LP", 
                  "RP", "LCB", "RCB", "LSB", "RSB", "COMMA", "DOT", "SEMI", 
                  "COLON", "ASSIGN", "ADD", "MINUS", "MUL", "DIV", "MOD", 
                  "NOT", "AND", "OR", "NOT_EQ", "EQUAL", "LESS_THAN", "GREATER_THAN", 
                  "GT_EQ", "LT_EQ", "SCOPE_OP", "ID", "BLOCK_COMMENT", "SINGLE_LINE_COMMENT", 
                  "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[63] = self.UNCLOSE_STRING_action 
            actions[64] = self.ILLEGAL_ESCAPE_action 
            actions[65] = self.ERROR_CHAR_action 
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
                
     


