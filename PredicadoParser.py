# Generated from Predicado.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("\67\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\5\3/\n\3\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\2\2\6\2\4\6\b\2\2\28\2\n\3\2\2\2\4.\3\2\2\2\6\60\3")
        buf.write("\2\2\2\b\63\3\2\2\2\n\13\5\4\3\2\13\f\b\2\1\2\f\3\3\2")
        buf.write("\2\2\r\16\5\6\4\2\16\17\b\3\1\2\17/\3\2\2\2\20\21\5\6")
        buf.write("\4\2\21\22\7\3\2\2\22\23\5\6\4\2\23\24\b\3\1\2\24/\3\2")
        buf.write("\2\2\25\26\5\6\4\2\26\27\7\4\2\2\27\30\5\6\4\2\30\31\b")
        buf.write("\3\1\2\31/\3\2\2\2\32\33\5\6\4\2\33\34\7\5\2\2\34\35\5")
        buf.write("\6\4\2\35\36\b\3\1\2\36/\3\2\2\2\37 \5\6\4\2 !\7\6\2\2")
        buf.write("!\"\5\6\4\2\"#\b\3\1\2#/\3\2\2\2$%\5\6\4\2%&\7\7\2\2&")
        buf.write("\'\5\6\4\2\'(\b\3\1\2(/\3\2\2\2)*\5\6\4\2*+\7\b\2\2+,")
        buf.write("\5\6\4\2,-\b\3\1\2-/\3\2\2\2.\r\3\2\2\2.\20\3\2\2\2.\25")
        buf.write("\3\2\2\2.\32\3\2\2\2.\37\3\2\2\2.$\3\2\2\2.)\3\2\2\2/")
        buf.write("\5\3\2\2\2\60\61\5\b\5\2\61\62\b\4\1\2\62\7\3\2\2\2\63")
        buf.write("\64\7\t\2\2\64\65\b\5\1\2\65\t\3\2\2\2\3.")
        return buf.getvalue()


class PredicadoParser ( Parser ):

    grammarFileName = "Predicado.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'=='", "'!='", "'>='", "'<='", "'<'", 
                     "'>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUMBER", "DIGIT", 
                      "WS" ]

    RULE_statement = 0
    RULE_expression = 1
    RULE_term = 2
    RULE_factor = 3

    ruleNames =  [ "statement", "expression", "term", "factor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NUMBER=7
    DIGIT=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.e = None # ExpressionContext

        def expression(self):
            return self.getTypedRuleContext(PredicadoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PredicadoParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = PredicadoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            localctx.e = self.expression()
            print('Result: ' + str(localctx.e.value))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.t = None # TermContext
            self.t1 = None # TermContext
            self.t2 = None # TermContext

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PredicadoParser.TermContext)
            else:
                return self.getTypedRuleContext(PredicadoParser.TermContext,i)


        def getRuleIndex(self):
            return PredicadoParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = PredicadoParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                localctx.t = self.term()
                localctx.value = localctx.t.value
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                localctx.t1 = self.term()
                self.state = 15
                self.match(PredicadoParser.T__0)
                self.state = 16
                localctx.t2 = self.term()
                localctx.value = localctx.t1.value == localctx.t2.value 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 19
                localctx.t1 = self.term()
                self.state = 20
                self.match(PredicadoParser.T__1)
                self.state = 21
                localctx.t2 = self.term()
                localctx.value = localctx.t1.value != localctx.t2.value 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 24
                localctx.t1 = self.term()
                self.state = 25
                self.match(PredicadoParser.T__2)
                self.state = 26
                localctx.t2 = self.term()
                localctx.value = localctx.t1.value >= localctx.t2.value 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 29
                localctx.t1 = self.term()
                self.state = 30
                self.match(PredicadoParser.T__3)
                self.state = 31
                localctx.t2 = self.term()
                localctx.value = localctx.t1.value <= localctx.t2.value 
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 34
                localctx.t1 = self.term()
                self.state = 35
                self.match(PredicadoParser.T__4)
                self.state = 36
                localctx.t2 = self.term()
                localctx.value = localctx.t1.value < localctx.t2.value 
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 39
                localctx.t1 = self.term()
                self.state = 40
                self.match(PredicadoParser.T__5)
                self.state = 41
                localctx.t2 = self.term()
                localctx.value = localctx.t1.value > localctx.t2.value 
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self.f = None # FactorContext

        def factor(self):
            return self.getTypedRuleContext(PredicadoParser.FactorContext,0)


        def getRuleIndex(self):
            return PredicadoParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = PredicadoParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            localctx.f = self.factor()
            localctx.value = localctx.f.value
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self._NUMBER = None # Token

        def NUMBER(self):
            return self.getToken(PredicadoParser.NUMBER, 0)

        def getRuleIndex(self):
            return PredicadoParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = PredicadoParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_factor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            localctx._NUMBER = self.match(PredicadoParser.NUMBER)
            localctx.value = int((None if localctx._NUMBER is None else localctx._NUMBER.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





