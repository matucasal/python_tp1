# Generated from Predicado.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PredicadoParser import PredicadoParser
else:
    from PredicadoParser import PredicadoParser

# This class defines a complete listener for a parse tree produced by PredicadoParser.
class PredicadoListener(ParseTreeListener):

    # Enter a parse tree produced by PredicadoParser#statement.
    def enterStatement(self, ctx:PredicadoParser.StatementContext):
        pass

    # Exit a parse tree produced by PredicadoParser#statement.
    def exitStatement(self, ctx:PredicadoParser.StatementContext):
        pass


    # Enter a parse tree produced by PredicadoParser#expression.
    def enterExpression(self, ctx:PredicadoParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PredicadoParser#expression.
    def exitExpression(self, ctx:PredicadoParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PredicadoParser#term.
    def enterTerm(self, ctx:PredicadoParser.TermContext):
        pass

    # Exit a parse tree produced by PredicadoParser#term.
    def exitTerm(self, ctx:PredicadoParser.TermContext):
        pass


    # Enter a parse tree produced by PredicadoParser#factor.
    def enterFactor(self, ctx:PredicadoParser.FactorContext):
        pass

    # Exit a parse tree produced by PredicadoParser#factor.
    def exitFactor(self, ctx:PredicadoParser.FactorContext):
        pass


