from postlang.PostLangVisitor import PostLangVisitor

class PostLangVisitorImpl(PostLangVisitor):
  def visitProg(self, ctx):
      return [self.visit(c) for c in ctx.statement()]
  
  def visitStatement(self, ctx):
      return self.visitChildren(ctx)

  def visitVarDecl(self, ctx):
      var = ctx.VAR().getText()
      expr = self.visit(ctx.expr())
      return expr + ['=' + var]

  def visitPrintStmt(self, ctx):
      expr = self.visit(ctx.expr())
      return expr + ['print']

  def visitAssignStmt(self, ctx):
      var = ctx.VAR().getText()
      expr = self.visit(ctx.expr())
      return expr + ['=' + var]

  def visitExpr(self, ctx):
      # Binary
      if ctx.op:
          left = self.visit(ctx.left)
          op = ctx.op.text
          right = self.visit(ctx.right)
          return left + right + [op]
      
      # Otherwise it is a term
      return self.visit(ctx.term())
  
  def visitTerm(self, ctx):
      # Binary
      if ctx.op:
          left = self.visit(ctx.left)
          op = ctx.op.text
          right = self.visit(ctx.right)
          return left + right + [op]
      
      # Otherwise it is a factor
      return self.visit(ctx.factor())
  
  def visitFactor(self, ctx):
      return [ctx.getText()]