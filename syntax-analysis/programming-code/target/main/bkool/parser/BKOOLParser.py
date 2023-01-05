# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("?\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\3\3\3\5\3\27\n\3\3\3\3\3\3\3\3")
        buf.write("\3\5\3\35\n\3\5\3\37\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\5\5)\n\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\5\7\64")
        buf.write("\n\7\3\b\3\b\3\b\3\b\3\b\5\b;\n\b\3\t\3\t\3\t\2\2\n\2")
        buf.write("\4\6\b\n\f\16\20\2\2\2<\2\22\3\2\2\2\4\36\3\2\2\2\6 \3")
        buf.write("\2\2\2\b$\3\2\2\2\n-\3\2\2\2\f\63\3\2\2\2\16:\3\2\2\2")
        buf.write("\20<\3\2\2\2\22\23\5\4\3\2\23\3\3\2\2\2\24\27\5\b\5\2")
        buf.write("\25\27\5\6\4\2\26\24\3\2\2\2\26\25\3\2\2\2\27\30\3\2\2")
        buf.write("\2\30\31\5\4\3\2\31\37\3\2\2\2\32\35\5\b\5\2\33\35\5\6")
        buf.write("\4\2\34\32\3\2\2\2\34\33\3\2\2\2\35\37\3\2\2\2\36\26\3")
        buf.write("\2\2\2\36\34\3\2\2\2\37\5\3\2\2\2 !\7\4\2\2!\"\5\f\7\2")
        buf.write("\"#\7\7\2\2#\7\3\2\2\2$%\7\4\2\2%&\5\20\t\2&(\7\b\2\2")
        buf.write("\')\5\16\b\2(\'\3\2\2\2()\3\2\2\2)*\3\2\2\2*+\7\t\2\2")
        buf.write("+,\5\n\6\2,\t\3\2\2\2-.\7\3\2\2.\13\3\2\2\2/\60\7\5\2")
        buf.write("\2\60\61\7\6\2\2\61\64\5\f\7\2\62\64\7\5\2\2\63/\3\2\2")
        buf.write("\2\63\62\3\2\2\2\64\r\3\2\2\2\65\66\5\6\4\2\66\67\5\16")
        buf.write("\b\2\67;\3\2\2\289\7\4\2\29;\5\f\7\2:\65\3\2\2\2:8\3\2")
        buf.write("\2\2;\17\3\2\2\2<=\7\5\2\2=\21\3\2\2\2\b\26\34\36(\63")
        buf.write(":")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'body'", "<INVALID>", "<INVALID>", "','", 
                     "';'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "TYPE", "ID", "COMMA", "SEMICOLON", 
                      "LB", "RB", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_program_int = 1
    RULE_vardecl = 2
    RULE_funcdecl = 3
    RULE_body = 4
    RULE_identifiers = 5
    RULE_func_args = 6
    RULE_func_name = 7

    ruleNames =  [ "program", "program_int", "vardecl", "funcdecl", "body", 
                   "identifiers", "func_args", "func_name" ]

    EOF = Token.EOF
    T__0=1
    TYPE=2
    ID=3
    COMMA=4
    SEMICOLON=5
    LB=6
    RB=7
    WS=8
    ERROR_CHAR=9

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

        def program_int(self):
            return self.getTypedRuleContext(BKOOLParser.Program_intContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.program_int()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Program_intContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def program_int(self):
            return self.getTypedRuleContext(BKOOLParser.Program_intContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(BKOOLParser.FuncdeclContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program_int

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram_int" ):
                return visitor.visitProgram_int(self)
            else:
                return visitor.visitChildren(self)




    def program_int(self):

        localctx = BKOOLParser.Program_intContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program_int)
        try:
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 18
                    self.funcdecl()
                    pass

                elif la_ == 2:
                    self.state = 19
                    self.vardecl()
                    pass


                self.state = 22
                self.program_int()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 24
                    self.funcdecl()
                    pass

                elif la_ == 2:
                    self.state = 25
                    self.vardecl()
                    pass


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(BKOOLParser.TYPE, 0)

        def identifiers(self):
            return self.getTypedRuleContext(BKOOLParser.IdentifiersContext,0)


        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = BKOOLParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(BKOOLParser.TYPE)
            self.state = 31
            self.identifiers()
            self.state = 32
            self.match(BKOOLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(BKOOLParser.TYPE, 0)

        def func_name(self):
            return self.getTypedRuleContext(BKOOLParser.Func_nameContext,0)


        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def body(self):
            return self.getTypedRuleContext(BKOOLParser.BodyContext,0)


        def func_args(self):
            return self.getTypedRuleContext(BKOOLParser.Func_argsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = BKOOLParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(BKOOLParser.TYPE)
            self.state = 35
            self.func_name()
            self.state = 36
            self.match(BKOOLParser.LB)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.TYPE:
                self.state = 37
                self.func_args()


            self.state = 40
            self.match(BKOOLParser.RB)
            self.state = 41
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKOOLParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = BKOOLParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(BKOOLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifiersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def identifiers(self):
            return self.getTypedRuleContext(BKOOLParser.IdentifiersContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_identifiers

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifiers" ):
                return visitor.visitIdentifiers(self)
            else:
                return visitor.visitChildren(self)




    def identifiers(self):

        localctx = BKOOLParser.IdentifiersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_identifiers)
        try:
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.match(BKOOLParser.ID)
                self.state = 46
                self.match(BKOOLParser.COMMA)
                self.state = 47
                self.identifiers()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_argsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def func_args(self):
            return self.getTypedRuleContext(BKOOLParser.Func_argsContext,0)


        def TYPE(self):
            return self.getToken(BKOOLParser.TYPE, 0)

        def identifiers(self):
            return self.getTypedRuleContext(BKOOLParser.IdentifiersContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_func_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_args" ):
                return visitor.visitFunc_args(self)
            else:
                return visitor.visitChildren(self)




    def func_args(self):

        localctx = BKOOLParser.Func_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_func_args)
        try:
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.vardecl()
                self.state = 52
                self.func_args()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.match(BKOOLParser.TYPE)
                self.state = 55
                self.identifiers()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_func_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_name" ):
                return visitor.visitFunc_name(self)
            else:
                return visitor.visitChildren(self)




    def func_name(self):

        localctx = BKOOLParser.Func_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_func_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





