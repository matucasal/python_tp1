# Generated from Logica.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\6\2\22\n\2\r\2\16\2\23\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\5\3\34\n\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\5\b\66\n\b\3\b\2\2\t\2\4\6\b\n\f\16\2\4\3\2\3\5\3\2")
        buf.write("\6\b\2\66\2\21\3\2\2\2\4\33\3\2\2\2\6\35\3\2\2\2\b\"\3")
        buf.write("\2\2\2\n\'\3\2\2\2\f)\3\2\2\2\16\65\3\2\2\2\20\22\5\4")
        buf.write("\3\2\21\20\3\2\2\2\22\23\3\2\2\2\23\21\3\2\2\2\23\24\3")
        buf.write("\2\2\2\24\3\3\2\2\2\25\26\5\6\4\2\26\27\b\3\1\2\27\34")
        buf.write("\3\2\2\2\30\31\5\b\5\2\31\32\b\3\1\2\32\34\3\2\2\2\33")
        buf.write("\25\3\2\2\2\33\30\3\2\2\2\34\5\3\2\2\2\35\36\5\16\b\2")
        buf.write("\36\37\5\n\6\2\37 \5\16\b\2 !\b\4\1\2!\7\3\2\2\2\"#\5")
        buf.write("\16\b\2#$\5\f\7\2$%\5\16\b\2%&\b\5\1\2&\t\3\2\2\2\'(\t")
        buf.write("\2\2\2(\13\3\2\2\2)*\t\3\2\2*\r\3\2\2\2+,\7\t\2\2,\66")
        buf.write("\b\b\1\2-.\7\n\2\2.\66\b\b\1\2/\60\7\13\2\2\60\66\b\b")
        buf.write("\1\2\61\62\7\f\2\2\62\66\b\b\1\2\63\64\7\r\2\2\64\66\b")
        buf.write("\b\1\2\65+\3\2\2\2\65-\3\2\2\2\65/\3\2\2\2\65\61\3\2\2")
        buf.write("\2\65\63\3\2\2\2\66\17\3\2\2\2\5\23\33\65")
        return buf.getvalue()


class LogicaParser ( Parser ):

    grammarFileName = "Logica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'and'", "'y'", "'&'", "'or'", "'o'", 
                     "'|'", "'true'", "'t'", "'v'", "'false'", "'f'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WS" ]

    RULE_logica = 0
    RULE_predicado = 1
    RULE_conjuncion = 2
    RULE_disyuncion = 3
    RULE_op_and = 4
    RULE_op_or = 5
    RULE_value = 6

    ruleNames =  [ "logica", "predicado", "conjuncion", "disyuncion", "op_and", 
                   "op_or", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LogicaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predicado(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogicaParser.PredicadoContext)
            else:
                return self.getTypedRuleContext(LogicaParser.PredicadoContext,i)


        def getRuleIndex(self):
            return LogicaParser.RULE_logica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogica" ):
                listener.enterLogica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogica" ):
                listener.exitLogica(self)




    def logica(self):

        localctx = LogicaParser.LogicaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_logica)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.predicado()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LogicaParser.T__6) | (1 << LogicaParser.T__7) | (1 << LogicaParser.T__8) | (1 << LogicaParser.T__9) | (1 << LogicaParser.T__10))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredicadoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.a = None # ConjuncionContext
            self.b = None # DisyuncionContext

        def conjuncion(self):
            return self.getTypedRuleContext(LogicaParser.ConjuncionContext,0)


        def disyuncion(self):
            return self.getTypedRuleContext(LogicaParser.DisyuncionContext,0)


        def getRuleIndex(self):
            return LogicaParser.RULE_predicado

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicado" ):
                listener.enterPredicado(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicado" ):
                listener.exitPredicado(self)




    def predicado(self):

        localctx = LogicaParser.PredicadoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_predicado)
        try:
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                localctx.a = self.conjuncion()
                print(localctx.a.res)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                localctx.b = self.disyuncion()
                print(localctx.b.res)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConjuncionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.a = None # ValueContext
            self.b = None # ValueContext

        def op_and(self):
            return self.getTypedRuleContext(LogicaParser.Op_andContext,0)


        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogicaParser.ValueContext)
            else:
                return self.getTypedRuleContext(LogicaParser.ValueContext,i)


        def getRuleIndex(self):
            return LogicaParser.RULE_conjuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjuncion" ):
                listener.enterConjuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjuncion" ):
                listener.exitConjuncion(self)




    def conjuncion(self):

        localctx = LogicaParser.ConjuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_conjuncion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            localctx.a = self.value()
            self.state = 28
            self.op_and()
            self.state = 29
            localctx.b = self.value()
            localctx.res=localctx.a.res and localctx.b.res
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DisyuncionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.a = None # ValueContext
            self.b = None # ValueContext

        def op_or(self):
            return self.getTypedRuleContext(LogicaParser.Op_orContext,0)


        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogicaParser.ValueContext)
            else:
                return self.getTypedRuleContext(LogicaParser.ValueContext,i)


        def getRuleIndex(self):
            return LogicaParser.RULE_disyuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisyuncion" ):
                listener.enterDisyuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisyuncion" ):
                listener.exitDisyuncion(self)




    def disyuncion(self):

        localctx = LogicaParser.DisyuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_disyuncion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            localctx.a = self.value()
            self.state = 33
            self.op_or()
            self.state = 34
            localctx.b = self.value()
            localctx.res=localctx.a.res or localctx.b.res
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_andContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LogicaParser.RULE_op_and

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_and" ):
                listener.enterOp_and(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_and" ):
                listener.exitOp_and(self)




    def op_and(self):

        localctx = LogicaParser.Op_andContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_op_and)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LogicaParser.T__0) | (1 << LogicaParser.T__1) | (1 << LogicaParser.T__2))) != 0)):
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


    class Op_orContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LogicaParser.RULE_op_or

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_or" ):
                listener.enterOp_or(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_or" ):
                listener.exitOp_or(self)




    def op_or(self):

        localctx = LogicaParser.Op_orContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_op_or)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LogicaParser.T__3) | (1 << LogicaParser.T__4) | (1 << LogicaParser.T__5))) != 0)):
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


    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None


        def getRuleIndex(self):
            return LogicaParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = LogicaParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_value)
        try:
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LogicaParser.T__6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(LogicaParser.T__6)
                localctx.res=True
                pass
            elif token in [LogicaParser.T__7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.match(LogicaParser.T__7)
                localctx.res=True
                pass
            elif token in [LogicaParser.T__8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.match(LogicaParser.T__8)
                localctx.res=True
                pass
            elif token in [LogicaParser.T__9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 47
                self.match(LogicaParser.T__9)
                localctx.res=False
                pass
            elif token in [LogicaParser.T__10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 49
                self.match(LogicaParser.T__10)
                localctx.res=False
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





