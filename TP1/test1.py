from antlr4 import CommonTokenStream, ParseTreeWalker, InputStream

from LogicaLexer import LogicaLexer
from LogicaParser import LogicaParser
from LogicaListener import LogicaListener

js = '''
x= v and v 
v or x
f or f
v or v
f y v
'''

print('Comenzando...')
input = InputStream(js)
lexer = LogicaLexer(input)
stream = CommonTokenStream(lexer)
parser = LogicaParser(stream)

tree = parser.logica()


print('Fin.')