# Generated from postlang/PostLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PostLangParser import PostLangParser
else:
    from PostLangParser import PostLangParser

# This class defines a complete generic visitor for a parse tree produced by PostLangParser.

class PostLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PostLangParser#prog.
    def visitProg(self, ctx:PostLangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostLangParser#statement.
    def visitStatement(self, ctx:PostLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostLangParser#varDecl.
    def visitVarDecl(self, ctx:PostLangParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostLangParser#printStmt.
    def visitPrintStmt(self, ctx:PostLangParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostLangParser#assignStmt.
    def visitAssignStmt(self, ctx:PostLangParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostLangParser#expr.
    def visitExpr(self, ctx:PostLangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostLangParser#operator.
    def visitOperator(self, ctx:PostLangParser.OperatorContext):
        return self.visitChildren(ctx)



del PostLangParser