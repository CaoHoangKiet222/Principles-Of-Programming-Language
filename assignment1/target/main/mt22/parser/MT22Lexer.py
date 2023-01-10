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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u01dc\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\7\2\u008c\n\2\f\2\16\2\u008f\13\2\3\2")
        buf.write("\3\2\6\2\u0093\n\2\r\2\16\2\u0094\7\2\u0097\n\2\f\2\16")
        buf.write("\2\u009a\13\2\3\2\5\2\u009d\n\2\3\2\3\2\3\3\3\3\5\3\u00a3")
        buf.write("\n\3\3\3\3\3\3\4\5\4\u00a8\n\4\3\4\3\4\3\4\3\4\5\4\u00ae")
        buf.write("\n\4\3\5\3\5\5\5\u00b2\n\5\3\5\3\5\3\6\3\6\5\6\u00b8\n")
        buf.write("\6\3\6\6\6\u00bb\n\6\r\6\16\6\u00bc\3\7\3\7\3\b\3\b\7")
        buf.write("\b\u00c3\n\b\f\b\16\b\u00c6\13\b\3\t\3\t\5\t\u00ca\n\t")
        buf.write("\3\n\3\n\3\n\7\n\u00cf\n\n\f\n\16\n\u00d2\13\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\5\13\u00db\n\13\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3")
        buf.write("+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\38\38\38\39\39\3:\3:\3;\3;\3;\3<\3<\3<\3=\3")
        buf.write("=\3=\3>\3>\7>\u019e\n>\f>\16>\u01a1\13>\3?\3?\3?\3?\6")
        buf.write("?\u01a7\n?\r?\16?\u01a8\3?\3?\3?\3?\3?\3@\3@\3@\3@\7@")
        buf.write("\u01b4\n@\f@\16@\u01b7\13@\3@\3@\3A\6A\u01bc\nA\rA\16")
        buf.write("A\u01bd\3A\3A\3B\3B\3B\7B\u01c5\nB\fB\16B\u01c8\13B\3")
        buf.write("B\5B\u01cb\nB\3B\3B\3C\3C\3C\7C\u01d2\nC\fC\16C\u01d5")
        buf.write("\13C\3C\3C\3C\3D\3D\3D\3\u01a8\2E\3\3\5\4\7\2\t\2\13\2")
        buf.write("\r\2\17\2\21\5\23\6\25\2\27\2\31\2\33\7\35\b\37\t!\n#")
        buf.write("\13%\f\'\r)\16+\17-\20/\21\61\22\63\23\65\24\67\259\26")
        buf.write(";\27=\30?\31A\32C\33E\34G\35I\36K\37M O!Q\"S#U$W%Y&[\'")
        buf.write("](_)a*c+e,g-i.k/m\60o\61q\62s\63u\64w\65y\66{\67}8\177")
        buf.write("9\u0081:\u0083;\u0085<\u0087=\3\2\16\3\2\63;\3\2\62;\4")
        buf.write("\2GGgg\4\2--//\n\2$$))^^ddhhppttvv\t\2))^^ddhhppttvv\5")
        buf.write("\2\f\f$$^^\5\2C\\aac|\6\2\62;C\\aac|\4\2\f\f\17\17\5\2")
        buf.write("\13\f\17\17\"\"\3\3\f\f\2\u01ea\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3")
        buf.write("\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0085\3\2\2\2\2\u0087\3\2\2\2\3\u009c\3\2\2\2\5\u00a2")
        buf.write("\3\2\2\2\7\u00ad\3\2\2\2\t\u00b1\3\2\2\2\13\u00b5\3\2")
        buf.write("\2\2\r\u00be\3\2\2\2\17\u00c0\3\2\2\2\21\u00c9\3\2\2\2")
        buf.write("\23\u00cb\3\2\2\2\25\u00da\3\2\2\2\27\u00dc\3\2\2\2\31")
        buf.write("\u00df\3\2\2\2\33\u00e1\3\2\2\2\35\u00e6\3\2\2\2\37\u00ee")
        buf.write("\3\2\2\2!\u00f6\3\2\2\2#\u00fa\3\2\2\2%\u0100\3\2\2\2")
        buf.write("\'\u0107\3\2\2\2)\u010d\3\2\2\2+\u0113\3\2\2\2-\u0116")
        buf.write("\3\2\2\2/\u011b\3\2\2\2\61\u011e\3\2\2\2\63\u0127\3\2")
        buf.write("\2\2\65\u012b\3\2\2\2\67\u0131\3\2\2\29\u0138\3\2\2\2")
        buf.write(";\u013d\3\2\2\2=\u0142\3\2\2\2?\u014b\3\2\2\2A\u014f\3")
        buf.write("\2\2\2C\u0155\3\2\2\2E\u0158\3\2\2\2G\u0160\3\2\2\2I\u0162")
        buf.write("\3\2\2\2K\u0164\3\2\2\2M\u0166\3\2\2\2O\u0168\3\2\2\2")
        buf.write("Q\u016a\3\2\2\2S\u016c\3\2\2\2U\u016e\3\2\2\2W\u0170\3")
        buf.write("\2\2\2Y\u0172\3\2\2\2[\u0174\3\2\2\2]\u0176\3\2\2\2_\u0178")
        buf.write("\3\2\2\2a\u017a\3\2\2\2c\u017c\3\2\2\2e\u017e\3\2\2\2")
        buf.write("g\u0180\3\2\2\2i\u0182\3\2\2\2k\u0185\3\2\2\2m\u0188\3")
        buf.write("\2\2\2o\u018b\3\2\2\2q\u018e\3\2\2\2s\u0190\3\2\2\2u\u0192")
        buf.write("\3\2\2\2w\u0195\3\2\2\2y\u0198\3\2\2\2{\u019b\3\2\2\2")
        buf.write("}\u01a2\3\2\2\2\177\u01af\3\2\2\2\u0081\u01bb\3\2\2\2")
        buf.write("\u0083\u01c1\3\2\2\2\u0085\u01ce\3\2\2\2\u0087\u01d9\3")
        buf.write("\2\2\2\u0089\u008d\t\2\2\2\u008a\u008c\t\3\2\2\u008b\u008a")
        buf.write("\3\2\2\2\u008c\u008f\3\2\2\2\u008d\u008b\3\2\2\2\u008d")
        buf.write("\u008e\3\2\2\2\u008e\u0098\3\2\2\2\u008f\u008d\3\2\2\2")
        buf.write("\u0090\u0092\7a\2\2\u0091\u0093\t\3\2\2\u0092\u0091\3")
        buf.write("\2\2\2\u0093\u0094\3\2\2\2\u0094\u0092\3\2\2\2\u0094\u0095")
        buf.write("\3\2\2\2\u0095\u0097\3\2\2\2\u0096\u0090\3\2\2\2\u0097")
        buf.write("\u009a\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2")
        buf.write("\u0099\u009d\3\2\2\2\u009a\u0098\3\2\2\2\u009b\u009d\7")
        buf.write("\62\2\2\u009c\u0089\3\2\2\2\u009c\u009b\3\2\2\2\u009d")
        buf.write("\u009e\3\2\2\2\u009e\u009f\b\2\2\2\u009f\4\3\2\2\2\u00a0")
        buf.write("\u00a3\5\7\4\2\u00a1\u00a3\5\t\5\2\u00a2\u00a0\3\2\2\2")
        buf.write("\u00a2\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5\b")
        buf.write("\3\3\2\u00a5\6\3\2\2\2\u00a6\u00a8\5\r\7\2\u00a7\u00a6")
        buf.write("\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9")
        buf.write("\u00ae\5\17\b\2\u00aa\u00ab\5\r\7\2\u00ab\u00ac\7\60\2")
        buf.write("\2\u00ac\u00ae\3\2\2\2\u00ad\u00a7\3\2\2\2\u00ad\u00aa")
        buf.write("\3\2\2\2\u00ae\b\3\2\2\2\u00af\u00b2\5\7\4\2\u00b0\u00b2")
        buf.write("\5\r\7\2\u00b1\u00af\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2")
        buf.write("\u00b3\3\2\2\2\u00b3\u00b4\5\13\6\2\u00b4\n\3\2\2\2\u00b5")
        buf.write("\u00b7\t\4\2\2\u00b6\u00b8\t\5\2\2\u00b7\u00b6\3\2\2\2")
        buf.write("\u00b7\u00b8\3\2\2\2\u00b8\u00ba\3\2\2\2\u00b9\u00bb\t")
        buf.write("\3\2\2\u00ba\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00ba")
        buf.write("\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\f\3\2\2\2\u00be\u00bf")
        buf.write("\5\3\2\2\u00bf\16\3\2\2\2\u00c0\u00c4\7\60\2\2\u00c1\u00c3")
        buf.write("\t\3\2\2\u00c2\u00c1\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4")
        buf.write("\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\20\3\2\2\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c7\u00ca\59\35\2\u00c8\u00ca\5\65\33")
        buf.write("\2\u00c9\u00c7\3\2\2\2\u00c9\u00c8\3\2\2\2\u00ca\22\3")
        buf.write("\2\2\2\u00cb\u00d0\7$\2\2\u00cc\u00cf\5\25\13\2\u00cd")
        buf.write("\u00cf\5\31\r\2\u00ce\u00cc\3\2\2\2\u00ce\u00cd\3\2\2")
        buf.write("\2\u00cf\u00d2\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00d1")
        buf.write("\3\2\2\2\u00d1\u00d3\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d3")
        buf.write("\u00d4\7$\2\2\u00d4\u00d5\b\n\4\2\u00d5\24\3\2\2\2\u00d6")
        buf.write("\u00d7\7^\2\2\u00d7\u00db\t\6\2\2\u00d8\u00d9\7)\2\2\u00d9")
        buf.write("\u00db\7$\2\2\u00da\u00d6\3\2\2\2\u00da\u00d8\3\2\2\2")
        buf.write("\u00db\26\3\2\2\2\u00dc\u00dd\7^\2\2\u00dd\u00de\n\7\2")
        buf.write("\2\u00de\30\3\2\2\2\u00df\u00e0\n\b\2\2\u00e0\32\3\2\2")
        buf.write("\2\u00e1\u00e2\7c\2\2\u00e2\u00e3\7w\2\2\u00e3\u00e4\7")
        buf.write("v\2\2\u00e4\u00e5\7q\2\2\u00e5\34\3\2\2\2\u00e6\u00e7")
        buf.write("\7d\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea")
        buf.write("\7n\2\2\u00ea\u00eb\7g\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed")
        buf.write("\7p\2\2\u00ed\36\3\2\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0")
        buf.write("\7p\2\2\u00f0\u00f1\7v\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3")
        buf.write("\7i\2\2\u00f3\u00f4\7g\2\2\u00f4\u00f5\7t\2\2\u00f5 \3")
        buf.write("\2\2\2\u00f6\u00f7\7k\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9")
        buf.write("\7v\2\2\u00f9\"\3\2\2\2\u00fa\u00fb\7h\2\2\u00fb\u00fc")
        buf.write("\7n\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe\7c\2\2\u00fe\u00ff")
        buf.write("\7v\2\2\u00ff$\3\2\2\2\u0100\u0101\7u\2\2\u0101\u0102")
        buf.write("\7v\2\2\u0102\u0103\7t\2\2\u0103\u0104\7k\2\2\u0104\u0105")
        buf.write("\7p\2\2\u0105\u0106\7i\2\2\u0106&\3\2\2\2\u0107\u0108")
        buf.write("\7c\2\2\u0108\u0109\7t\2\2\u0109\u010a\7t\2\2\u010a\u010b")
        buf.write("\7c\2\2\u010b\u010c\7{\2\2\u010c(\3\2\2\2\u010d\u010e")
        buf.write("\7d\2\2\u010e\u010f\7t\2\2\u010f\u0110\7g\2\2\u0110\u0111")
        buf.write("\7c\2\2\u0111\u0112\7m\2\2\u0112*\3\2\2\2\u0113\u0114")
        buf.write("\7f\2\2\u0114\u0115\7q\2\2\u0115,\3\2\2\2\u0116\u0117")
        buf.write("\7g\2\2\u0117\u0118\7n\2\2\u0118\u0119\7u\2\2\u0119\u011a")
        buf.write("\7g\2\2\u011a.\3\2\2\2\u011b\u011c\7k\2\2\u011c\u011d")
        buf.write("\7h\2\2\u011d\60\3\2\2\2\u011e\u011f\7h\2\2\u011f\u0120")
        buf.write("\7w\2\2\u0120\u0121\7p\2\2\u0121\u0122\7e\2\2\u0122\u0123")
        buf.write("\7v\2\2\u0123\u0124\7k\2\2\u0124\u0125\7q\2\2\u0125\u0126")
        buf.write("\7p\2\2\u0126\62\3\2\2\2\u0127\u0128\7h\2\2\u0128\u0129")
        buf.write("\7q\2\2\u0129\u012a\7t\2\2\u012a\64\3\2\2\2\u012b\u012c")
        buf.write("\7h\2\2\u012c\u012d\7c\2\2\u012d\u012e\7n\2\2\u012e\u012f")
        buf.write("\7u\2\2\u012f\u0130\7g\2\2\u0130\66\3\2\2\2\u0131\u0132")
        buf.write("\7t\2\2\u0132\u0133\7g\2\2\u0133\u0134\7v\2\2\u0134\u0135")
        buf.write("\7w\2\2\u0135\u0136\7t\2\2\u0136\u0137\7p\2\2\u01378\3")
        buf.write("\2\2\2\u0138\u0139\7v\2\2\u0139\u013a\7t\2\2\u013a\u013b")
        buf.write("\7w\2\2\u013b\u013c\7g\2\2\u013c:\3\2\2\2\u013d\u013e")
        buf.write("\7x\2\2\u013e\u013f\7q\2\2\u013f\u0140\7k\2\2\u0140\u0141")
        buf.write("\7f\2\2\u0141<\3\2\2\2\u0142\u0143\7e\2\2\u0143\u0144")
        buf.write("\7q\2\2\u0144\u0145\7p\2\2\u0145\u0146\7v\2\2\u0146\u0147")
        buf.write("\7k\2\2\u0147\u0148\7p\2\2\u0148\u0149\7w\2\2\u0149\u014a")
        buf.write("\7g\2\2\u014a>\3\2\2\2\u014b\u014c\7q\2\2\u014c\u014d")
        buf.write("\7w\2\2\u014d\u014e\7v\2\2\u014e@\3\2\2\2\u014f\u0150")
        buf.write("\7y\2\2\u0150\u0151\7j\2\2\u0151\u0152\7k\2\2\u0152\u0153")
        buf.write("\7n\2\2\u0153\u0154\7g\2\2\u0154B\3\2\2\2\u0155\u0156")
        buf.write("\7q\2\2\u0156\u0157\7h\2\2\u0157D\3\2\2\2\u0158\u0159")
        buf.write("\7k\2\2\u0159\u015a\7p\2\2\u015a\u015b\7j\2\2\u015b\u015c")
        buf.write("\7g\2\2\u015c\u015d\7t\2\2\u015d\u015e\7k\2\2\u015e\u015f")
        buf.write("\7v\2\2\u015fF\3\2\2\2\u0160\u0161\7*\2\2\u0161H\3\2\2")
        buf.write("\2\u0162\u0163\7+\2\2\u0163J\3\2\2\2\u0164\u0165\7}\2")
        buf.write("\2\u0165L\3\2\2\2\u0166\u0167\7\177\2\2\u0167N\3\2\2\2")
        buf.write("\u0168\u0169\7]\2\2\u0169P\3\2\2\2\u016a\u016b\7_\2\2")
        buf.write("\u016bR\3\2\2\2\u016c\u016d\7.\2\2\u016dT\3\2\2\2\u016e")
        buf.write("\u016f\7\60\2\2\u016fV\3\2\2\2\u0170\u0171\7=\2\2\u0171")
        buf.write("X\3\2\2\2\u0172\u0173\7<\2\2\u0173Z\3\2\2\2\u0174\u0175")
        buf.write("\7?\2\2\u0175\\\3\2\2\2\u0176\u0177\7-\2\2\u0177^\3\2")
        buf.write("\2\2\u0178\u0179\7/\2\2\u0179`\3\2\2\2\u017a\u017b\7,")
        buf.write("\2\2\u017bb\3\2\2\2\u017c\u017d\7\61\2\2\u017dd\3\2\2")
        buf.write("\2\u017e\u017f\7\'\2\2\u017ff\3\2\2\2\u0180\u0181\7#\2")
        buf.write("\2\u0181h\3\2\2\2\u0182\u0183\7(\2\2\u0183\u0184\7(\2")
        buf.write("\2\u0184j\3\2\2\2\u0185\u0186\7~\2\2\u0186\u0187\7~\2")
        buf.write("\2\u0187l\3\2\2\2\u0188\u0189\7#\2\2\u0189\u018a\7?\2")
        buf.write("\2\u018an\3\2\2\2\u018b\u018c\7?\2\2\u018c\u018d\7?\2")
        buf.write("\2\u018dp\3\2\2\2\u018e\u018f\7>\2\2\u018fr\3\2\2\2\u0190")
        buf.write("\u0191\7@\2\2\u0191t\3\2\2\2\u0192\u0193\7@\2\2\u0193")
        buf.write("\u0194\7?\2\2\u0194v\3\2\2\2\u0195\u0196\7>\2\2\u0196")
        buf.write("\u0197\7?\2\2\u0197x\3\2\2\2\u0198\u0199\7<\2\2\u0199")
        buf.write("\u019a\7<\2\2\u019az\3\2\2\2\u019b\u019f\t\t\2\2\u019c")
        buf.write("\u019e\t\n\2\2\u019d\u019c\3\2\2\2\u019e\u01a1\3\2\2\2")
        buf.write("\u019f\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0|\3\2\2")
        buf.write("\2\u01a1\u019f\3\2\2\2\u01a2\u01a3\7\61\2\2\u01a3\u01a4")
        buf.write("\7,\2\2\u01a4\u01a6\3\2\2\2\u01a5\u01a7\13\2\2\2\u01a6")
        buf.write("\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a9\3\2\2\2")
        buf.write("\u01a8\u01a6\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ab\7")
        buf.write(",\2\2\u01ab\u01ac\7\61\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01ae")
        buf.write("\b?\5\2\u01ae~\3\2\2\2\u01af\u01b0\7\61\2\2\u01b0\u01b1")
        buf.write("\7\61\2\2\u01b1\u01b5\3\2\2\2\u01b2\u01b4\n\13\2\2\u01b3")
        buf.write("\u01b2\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5\u01b3\3\2\2\2")
        buf.write("\u01b5\u01b6\3\2\2\2\u01b6\u01b8\3\2\2\2\u01b7\u01b5\3")
        buf.write("\2\2\2\u01b8\u01b9\b@\5\2\u01b9\u0080\3\2\2\2\u01ba\u01bc")
        buf.write("\t\f\2\2\u01bb\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd")
        buf.write("\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01bf\3\2\2\2")
        buf.write("\u01bf\u01c0\bA\5\2\u01c0\u0082\3\2\2\2\u01c1\u01c6\7")
        buf.write("$\2\2\u01c2\u01c5\5\31\r\2\u01c3\u01c5\5\25\13\2\u01c4")
        buf.write("\u01c2\3\2\2\2\u01c4\u01c3\3\2\2\2\u01c5\u01c8\3\2\2\2")
        buf.write("\u01c6\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01ca\3")
        buf.write("\2\2\2\u01c8\u01c6\3\2\2\2\u01c9\u01cb\t\r\2\2\u01ca\u01c9")
        buf.write("\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01cd\bB\6\2\u01cd")
        buf.write("\u0084\3\2\2\2\u01ce\u01d3\7$\2\2\u01cf\u01d2\5\31\r\2")
        buf.write("\u01d0\u01d2\5\25\13\2\u01d1\u01cf\3\2\2\2\u01d1\u01d0")
        buf.write("\3\2\2\2\u01d2\u01d5\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3")
        buf.write("\u01d4\3\2\2\2\u01d4\u01d6\3\2\2\2\u01d5\u01d3\3\2\2\2")
        buf.write("\u01d6\u01d7\5\27\f\2\u01d7\u01d8\bC\7\2\u01d8\u0086\3")
        buf.write("\2\2\2\u01d9\u01da\13\2\2\2\u01da\u01db\bD\b\2\u01db\u0088")
        buf.write("\3\2\2\2\33\2\u008d\u0094\u0098\u009c\u00a2\u00a7\u00ad")
        buf.write("\u00b1\u00b7\u00bc\u00c4\u00c9\u00ce\u00d0\u00da\u019f")
        buf.write("\u01a8\u01b5\u01bd\u01c4\u01c6\u01ca\u01d1\u01d3\t\3\2")
        buf.write("\2\3\3\3\3\n\4\b\2\2\3B\5\3C\6\3D\7")
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
    INT = 8
    FLOAT = 9
    STRING = 10
    ARRAY = 11
    BREAK = 12
    DO = 13
    ELSE = 14
    IF = 15
    FUNCTION = 16
    FOR = 17
    FALSE = 18
    RETURN = 19
    TRUE = 20
    VOID = 21
    CONTINUE = 22
    OUT = 23
    WHILE = 24
    OF = 25
    INHERIT = 26
    LP = 27
    RP = 28
    LCB = 29
    RCB = 30
    LSB = 31
    RSB = 32
    COMMA = 33
    DOT = 34
    SEMI = 35
    COLON = 36
    ASSIGN = 37
    ADD = 38
    MINUS = 39
    MUL = 40
    DIV = 41
    MOD = 42
    NOT = 43
    AND = 44
    OR = 45
    NOT_EQ = 46
    EQUAL = 47
    LESS_THAN = 48
    GREATER_THAN = 49
    GT_EQ = 50
    LT_EQ = 51
    SCOPE_OP = 52
    ID = 53
    BLOCK_COMMENT = 54
    SINGLE_LINE_COMMENT = 55
    WS = 56
    UNCLOSE_STRING = 57
    ILLEGAL_ESCAPE = 58
    ERROR_CHAR = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'boolean'", "'integer'", "'int'", "'float'", "'string'", 
            "'array'", "'break'", "'do'", "'else'", "'if'", "'function'", 
            "'for'", "'false'", "'return'", "'true'", "'void'", "'continue'", 
            "'out'", "'while'", "'of'", "'inherit'", "'('", "')'", "'{'", 
            "'}'", "'['", "']'", "','", "'.'", "';'", "':'", "'='", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'!='", "'=='", 
            "'<'", "'>'", "'>='", "'<='", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "INT_LIT", "FLOAT_LIT", "BOOLEAN_LIT", "STRING_LIT", "AUTO", 
            "BOOLEAN", "INTEGER", "INT", "FLOAT", "STRING", "ARRAY", "BREAK", 
            "DO", "ELSE", "IF", "FUNCTION", "FOR", "FALSE", "RETURN", "TRUE", 
            "VOID", "CONTINUE", "OUT", "WHILE", "OF", "INHERIT", "LP", "RP", 
            "LCB", "RCB", "LSB", "RSB", "COMMA", "DOT", "SEMI", "COLON", 
            "ASSIGN", "ADD", "MINUS", "MUL", "DIV", "MOD", "NOT", "AND", 
            "OR", "NOT_EQ", "EQUAL", "LESS_THAN", "GREATER_THAN", "GT_EQ", 
            "LT_EQ", "SCOPE_OP", "ID", "BLOCK_COMMENT", "SINGLE_LINE_COMMENT", 
            "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "INT_LIT", "FLOAT_LIT", "POINT_FLOAT", "EXPONENT_FLOAT", 
                  "EXPONENT", "INT_PART", "FRACTION_PART", "BOOLEAN_LIT", 
                  "STRING_LIT", "ESC", "ESC_ERR", "STR_CHAR", "AUTO", "BOOLEAN", 
                  "INTEGER", "INT", "FLOAT", "STRING", "ARRAY", "BREAK", 
                  "DO", "ELSE", "IF", "FUNCTION", "FOR", "FALSE", "RETURN", 
                  "TRUE", "VOID", "CONTINUE", "OUT", "WHILE", "OF", "INHERIT", 
                  "LP", "RP", "LCB", "RCB", "LSB", "RSB", "COMMA", "DOT", 
                  "SEMI", "COLON", "ASSIGN", "ADD", "MINUS", "MUL", "DIV", 
                  "MOD", "NOT", "AND", "OR", "NOT_EQ", "EQUAL", "LESS_THAN", 
                  "GREATER_THAN", "GT_EQ", "LT_EQ", "SCOPE_OP", "ID", "BLOCK_COMMENT", 
                  "SINGLE_LINE_COMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

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
            actions[64] = self.UNCLOSE_STRING_action 
            actions[65] = self.ILLEGAL_ESCAPE_action 
            actions[66] = self.ERROR_CHAR_action 
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
                
     


