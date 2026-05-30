import argparse
from antlr4 import *
from postlang.PostLangLexer import PostLangLexer
from postlang.PostLangParser import PostLangParser
from PostLangVisitorImpl import PostLangVisitorImpl
from Interpreter import Interpreter

def main():
  parser_args = argparse.ArgumentParser()
  parser_args.add_argument("file", help="Source file to run")
  parser_args.add_argument("--debug", action="store_true", help="Print parse tree and RPN")
  args = parser_args.parse_args()

  with open(args.file, "r", encoding="utf-8") as f:
    data = f.read()

  # Get the input
  input_stream = InputStream(data)

  # Lex and parse
  lexer = PostLangLexer(input_stream)
  tokens = CommonTokenStream(lexer)
  parser = PostLangParser(tokens)
  tree = parser.prog()

  if args.debug:
    print("Parse tree:\n", tree.toStringTree(recog=parser), "\n")

  # Compile to RPN
  visitor = PostLangVisitorImpl()
  result = visitor.visit(tree)

  if args.debug:
    flat = [token for stmt in result for token in stmt]
    print("RPN:\n", " ".join(flat), "\n")

  # Run
  interpreter = Interpreter()
  interpreter.run(result)

if __name__ == "__main__":
  main()