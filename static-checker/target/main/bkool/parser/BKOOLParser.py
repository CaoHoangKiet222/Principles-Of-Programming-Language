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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("L\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\6\2\22\n\2\r\2\16\2\23\3\2\3\2\3\3\3\3\3\3\7")
        buf.write("\3\33\n\3\f\3\16\3\36\13\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4")
        buf.write("\7\4\'\n\4\f\4\16\4*\13\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\5\5\64\n\5\3\5\3\5\5\58\n\5\3\6\6\6;\n\6\r\6\16\6")
        buf.write("<\3\7\3\7\3\7\3\7\3\7\3\7\7\7E\n\7\f\7\16\7H\13\7\3\7")
        buf.write("\3\7\3\7\2\2\b\2\4\6\b\n\f\2\3\3\2\5\6\2R\2\21\3\2\2\2")
        buf.write("\4\27\3\2\2\2\6\"\3\2\2\2\b.\3\2\2\2\n:\3\2\2\2\f>\3\2")
        buf.write("\2\2\16\22\5\4\3\2\17\22\5\6\4\2\20\22\5\b\5\2\21\16\3")
        buf.write("\2\2\2\21\17\3\2\2\2\21\20\3\2\2\2\22\23\3\2\2\2\23\21")
        buf.write("\3\2\2\2\23\24\3\2\2\2\24\25\3\2\2\2\25\26\7\2\2\3\26")
        buf.write("\3\3\2\2\2\27\34\7\t\2\2\30\31\7\3\2\2\31\33\7\t\2\2\32")
        buf.write("\30\3\2\2\2\33\36\3\2\2\2\34\32\3\2\2\2\34\35\3\2\2\2")
        buf.write("\35\37\3\2\2\2\36\34\3\2\2\2\37 \7\4\2\2 !\t\2\2\2!\5")
        buf.write("\3\2\2\2\"#\7\7\2\2#(\7\t\2\2$%\7\3\2\2%\'\7\t\2\2&$\3")
        buf.write("\2\2\2\'*\3\2\2\2(&\3\2\2\2()\3\2\2\2)+\3\2\2\2*(\3\2")
        buf.write("\2\2+,\7\4\2\2,-\7\n\2\2-\7\3\2\2\2./\7\t\2\2/\60\7\4")
        buf.write("\2\2\60\61\7\b\2\2\61\63\7\r\2\2\62\64\5\n\6\2\63\62\3")
        buf.write("\2\2\2\63\64\3\2\2\2\64\65\3\2\2\2\65\67\7\16\2\2\668")
        buf.write("\5\f\7\2\67\66\3\2\2\2\678\3\2\2\28\t\3\2\2\29;\5\4\3")
        buf.write("\2:9\3\2\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2\2=\13\3\2\2\2")
        buf.write(">F\7\r\2\2?E\5\4\3\2@E\5\6\4\2AE\5\b\5\2BE\7\n\2\2CE\7")
        buf.write("\t\2\2D?\3\2\2\2D@\3\2\2\2DA\3\2\2\2DB\3\2\2\2DC\3\2\2")
        buf.write("\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2GI\3\2\2\2HF\3\2\2\2I")
        buf.write("J\7\16\2\2J\r\3\2\2\2\13\21\23\34(\63\67<DF")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "':'", "'int'", "'float'", "'const'", 
                     "'function'", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "INTTYPE", 
                      "FLOATTYPE", "CONST", "FUNCTION", "ID", "INTLIT", 
                      "LB", "RB", "LP", "RP", "SEMI", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_vardecl = 1
    RULE_constdecl = 2
    RULE_funcdecl = 3
    RULE_param_list = 4
    RULE_body = 5

    ruleNames =  [ "program", "vardecl", "constdecl", "funcdecl", "param_list", 
                   "body" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    INTTYPE=3
    FLOATTYPE=4
    CONST=5
    FUNCTION=6
    ID=7
    INTLIT=8
    LB=9
    RB=10
    LP=11
    RP=12
    SEMI=13
    WS=14
    ERROR_CHAR=15
    UNCLOSE_STRING=16
    ILLEGAL_ESCAPE=17

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

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.VardeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.VardeclContext,i)


        def constdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ConstdeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ConstdeclContext,i)


        def funcdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.FuncdeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.FuncdeclContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 15
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 12
                    self.vardecl()
                    pass

                elif la_ == 2:
                    self.state = 13
                    self.constdecl()
                    pass

                elif la_ == 3:
                    self.state = 14
                    self.funcdecl()
                    pass


                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.CONST or _la==BKOOLParser.ID):
                    break

            self.state = 19
            self.match(BKOOLParser.EOF)
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def INTTYPE(self):
            return self.getToken(BKOOLParser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(BKOOLParser.FLOATTYPE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = BKOOLParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(BKOOLParser.ID)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.T__0:
                self.state = 22
                self.match(BKOOLParser.T__0)
                self.state = 23
                self.match(BKOOLParser.ID)
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self.match(BKOOLParser.T__1)
            self.state = 30
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.INTTYPE or _la==BKOOLParser.FLOATTYPE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(BKOOLParser.CONST, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_constdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstdecl" ):
                return visitor.visitConstdecl(self)
            else:
                return visitor.visitChildren(self)




    def constdecl(self):

        localctx = BKOOLParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_constdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(BKOOLParser.CONST)
            self.state = 33
            self.match(BKOOLParser.ID)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.T__0:
                self.state = 34
                self.match(BKOOLParser.T__0)
                self.state = 35
                self.match(BKOOLParser.ID)
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
            self.match(BKOOLParser.T__1)
            self.state = 42
            self.match(BKOOLParser.INTLIT)
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

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def FUNCTION(self):
            return self.getToken(BKOOLParser.FUNCTION, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def param_list(self):
            return self.getTypedRuleContext(BKOOLParser.Param_listContext,0)


        def body(self):
            return self.getTypedRuleContext(BKOOLParser.BodyContext,0)


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
            self.state = 44
            self.match(BKOOLParser.ID)
            self.state = 45
            self.match(BKOOLParser.T__1)
            self.state = 46
            self.match(BKOOLParser.FUNCTION)
            self.state = 47
            self.match(BKOOLParser.LP)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.ID:
                self.state = 48
                self.param_list()


            self.state = 51
            self.match(BKOOLParser.RP)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.LP:
                self.state = 52
                self.body()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.VardeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.VardeclContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = BKOOLParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 55
                self.vardecl()
                self.state = 58 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.ID):
                    break

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

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.VardeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.VardeclContext,i)


        def constdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ConstdeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ConstdeclContext,i)


        def funcdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.FuncdeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.FuncdeclContext,i)


        def INTLIT(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.INTLIT)
            else:
                return self.getToken(BKOOLParser.INTLIT, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = BKOOLParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(BKOOLParser.LP)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.CONST) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.INTLIT))) != 0):
                self.state = 66
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 61
                    self.vardecl()
                    pass

                elif la_ == 2:
                    self.state = 62
                    self.constdecl()
                    pass

                elif la_ == 3:
                    self.state = 63
                    self.funcdecl()
                    pass

                elif la_ == 4:
                    self.state = 64
                    self.match(BKOOLParser.INTLIT)
                    pass

                elif la_ == 5:
                    self.state = 65
                    self.match(BKOOLParser.ID)
                    pass


                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





