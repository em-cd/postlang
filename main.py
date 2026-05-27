from antlr4 import *
from RPNLexer import RPNLexer
from RPNParser import RPNParser

input_stream = InputStream("3 4 2 * +")

lexer = RPNLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = RPNParser(tokens)

tree = parser.prog()

print(tree.toStringTree(recog=parser))