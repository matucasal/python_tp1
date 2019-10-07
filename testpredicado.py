from antlr4 import CommonTokenStream, ParseTreeWalker, InputStream

from PredicadoLexer import PredicadoLexer
from PredicadoParser import PredicadoParser
from PredicadoListener import PredicadoListener

js = '''
1<4
'''

print('Comenzando...')
input = InputStream(js)
lexer = PredicadoLexer(input)
stream = CommonTokenStream(lexer)
parser = PredicadoParser(stream)

tree = parser.statement()


print('Fin.')