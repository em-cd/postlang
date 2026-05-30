# Generated from PostLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PostLangParser import PostLangParser
else:
    from PostLangParser import PostLangParser

# This class defines a complete listener for a parse tree produced by PostLangParser.
class PostLangListener(ParseTreeListener):

    # Enter a parse tree produced by PostLangParser#prog.
    def enterProg(self, ctx:PostLangParser.ProgContext):
        pass

    # Exit a parse tree produced by PostLangParser#prog.
    def exitProg(self, ctx:PostLangParser.ProgContext):
        pass


    # Enter a parse tree produced by PostLangParser#statement.
    def enterStatement(self, ctx:PostLangParser.StatementContext):
        pass

    # Exit a parse tree produced by PostLangParser#statement.
    def exitStatement(self, ctx:PostLangParser.StatementContext):
        pass


    # Enter a parse tree produced by PostLangParser#varDecl.
    def enterVarDecl(self, ctx:PostLangParser.VarDeclContext):
        pass

    # Exit a parse tree produced by PostLangParser#varDecl.
    def exitVarDecl(self, ctx:PostLangParser.VarDeclContext):
        pass


    # Enter a parse tree produced by PostLangParser#printStmt.
    def enterPrintStmt(self, ctx:PostLangParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by PostLangParser#printStmt.
    def exitPrintStmt(self, ctx:PostLangParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by PostLangParser#assignStmt.
    def enterAssignStmt(self, ctx:PostLangParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by PostLangParser#assignStmt.
    def exitAssignStmt(self, ctx:PostLangParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by PostLangParser#expr.
    def enterExpr(self, ctx:PostLangParser.ExprContext):
        pass

    # Exit a parse tree produced by PostLangParser#expr.
    def exitExpr(self, ctx:PostLangParser.ExprContext):
        pass


    # Enter a parse tree produced by PostLangParser#term.
    def enterTerm(self, ctx:PostLangParser.TermContext):
        pass

    # Exit a parse tree produced by PostLangParser#term.
    def exitTerm(self, ctx:PostLangParser.TermContext):
        pass


    # Enter a parse tree produced by PostLangParser#factor.
    def enterFactor(self, ctx:PostLangParser.FactorContext):
        pass

    # Exit a parse tree produced by PostLangParser#factor.
    def exitFactor(self, ctx:PostLangParser.FactorContext):
        pass



del PostLangParser