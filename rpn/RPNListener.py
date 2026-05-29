# Generated from RPN.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RPNParser import RPNParser
else:
    from RPNParser import RPNParser

# This class defines a complete listener for a parse tree produced by RPNParser.
class RPNListener(ParseTreeListener):

    # Enter a parse tree produced by RPNParser#prog.
    def enterProg(self, ctx:RPNParser.ProgContext):
        pass

    # Exit a parse tree produced by RPNParser#prog.
    def exitProg(self, ctx:RPNParser.ProgContext):
        pass


    # Enter a parse tree produced by RPNParser#expr.
    def enterExpr(self, ctx:RPNParser.ExprContext):
        pass

    # Exit a parse tree produced by RPNParser#expr.
    def exitExpr(self, ctx:RPNParser.ExprContext):
        pass


    # Enter a parse tree produced by RPNParser#operator.
    def enterOperator(self, ctx:RPNParser.OperatorContext):
        pass

    # Exit a parse tree produced by RPNParser#operator.
    def exitOperator(self, ctx:RPNParser.OperatorContext):
        pass



del RPNParser