# Generated from Logica.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LogicaParser import LogicaParser
else:
    from LogicaParser import LogicaParser

# This class defines a complete listener for a parse tree produced by LogicaParser.
class LogicaListener(ParseTreeListener):

    # Enter a parse tree produced by LogicaParser#logica.
    def enterLogica(self, ctx:LogicaParser.LogicaContext):
        pass

    # Exit a parse tree produced by LogicaParser#logica.
    def exitLogica(self, ctx:LogicaParser.LogicaContext):
        pass


    # Enter a parse tree produced by LogicaParser#predicado.
    def enterPredicado(self, ctx:LogicaParser.PredicadoContext):
        pass

    # Exit a parse tree produced by LogicaParser#predicado.
    def exitPredicado(self, ctx:LogicaParser.PredicadoContext):
        pass


    # Enter a parse tree produced by LogicaParser#conjuncion.
    def enterConjuncion(self, ctx:LogicaParser.ConjuncionContext):
        pass

    # Exit a parse tree produced by LogicaParser#conjuncion.
    def exitConjuncion(self, ctx:LogicaParser.ConjuncionContext):
        pass


    # Enter a parse tree produced by LogicaParser#disyuncion.
    def enterDisyuncion(self, ctx:LogicaParser.DisyuncionContext):
        pass

    # Exit a parse tree produced by LogicaParser#disyuncion.
    def exitDisyuncion(self, ctx:LogicaParser.DisyuncionContext):
        pass


    # Enter a parse tree produced by LogicaParser#op_and.
    def enterOp_and(self, ctx:LogicaParser.Op_andContext):
        pass

    # Exit a parse tree produced by LogicaParser#op_and.
    def exitOp_and(self, ctx:LogicaParser.Op_andContext):
        pass


    # Enter a parse tree produced by LogicaParser#op_or.
    def enterOp_or(self, ctx:LogicaParser.Op_orContext):
        pass

    # Exit a parse tree produced by LogicaParser#op_or.
    def exitOp_or(self, ctx:LogicaParser.Op_orContext):
        pass


    # Enter a parse tree produced by LogicaParser#value.
    def enterValue(self, ctx:LogicaParser.ValueContext):
        pass

    # Exit a parse tree produced by LogicaParser#value.
    def exitValue(self, ctx:LogicaParser.ValueContext):
        pass


