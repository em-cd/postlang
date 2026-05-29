from antlr4 import *
from postlang.PostLangLexer import PostLangLexer
from postlang.PostLangParser import PostLangParser

with open("program.pl", "r", encoding="utf-8") as f:
  data = f.read()

input_stream = InputStream(data)

lexer = PostLangLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = PostLangParser(tokens)

tree = parser.prog()

print(tree.toStringTree(recog=parser))