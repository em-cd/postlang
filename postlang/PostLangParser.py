# Generated from PostLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,75,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,1,0,1,1,1,1,1,1,3,
        1,28,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,
        1,4,1,5,1,5,1,5,1,5,1,5,1,5,5,5,51,8,5,10,5,12,5,54,9,5,1,6,1,6,
        1,6,1,6,1,6,1,6,5,6,62,8,6,10,6,12,6,65,9,6,1,7,1,7,1,7,1,7,1,7,
        1,7,3,7,73,8,7,1,7,0,2,10,12,8,0,2,4,6,8,10,12,14,0,2,1,0,5,6,1,
        0,7,8,73,0,19,1,0,0,0,2,27,1,0,0,0,4,29,1,0,0,0,6,35,1,0,0,0,8,39,
        1,0,0,0,10,44,1,0,0,0,12,55,1,0,0,0,14,72,1,0,0,0,16,18,3,2,1,0,
        17,16,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,22,1,
        0,0,0,21,19,1,0,0,0,22,23,5,0,0,1,23,1,1,0,0,0,24,28,3,4,2,0,25,
        28,3,6,3,0,26,28,3,8,4,0,27,24,1,0,0,0,27,25,1,0,0,0,27,26,1,0,0,
        0,28,3,1,0,0,0,29,30,5,1,0,0,30,31,5,11,0,0,31,32,5,2,0,0,32,33,
        3,10,5,0,33,34,5,3,0,0,34,5,1,0,0,0,35,36,5,4,0,0,36,37,3,10,5,0,
        37,38,5,3,0,0,38,7,1,0,0,0,39,40,5,11,0,0,40,41,5,2,0,0,41,42,3,
        10,5,0,42,43,5,3,0,0,43,9,1,0,0,0,44,45,6,5,-1,0,45,46,3,12,6,0,
        46,52,1,0,0,0,47,48,10,2,0,0,48,49,7,0,0,0,49,51,3,12,6,0,50,47,
        1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,11,1,0,0,0,
        54,52,1,0,0,0,55,56,6,6,-1,0,56,57,3,14,7,0,57,63,1,0,0,0,58,59,
        10,2,0,0,59,60,7,1,0,0,60,62,3,14,7,0,61,58,1,0,0,0,62,65,1,0,0,
        0,63,61,1,0,0,0,63,64,1,0,0,0,64,13,1,0,0,0,65,63,1,0,0,0,66,73,
        5,11,0,0,67,73,5,12,0,0,68,69,5,9,0,0,69,70,3,10,5,0,70,71,5,10,
        0,0,71,73,1,0,0,0,72,66,1,0,0,0,72,67,1,0,0,0,72,68,1,0,0,0,73,15,
        1,0,0,0,5,19,27,52,63,72
    ]

class PostLangParser ( Parser ):

    grammarFileName = "PostLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'let'", "'='", "';'", "'print'", "'+'", 
                     "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "VAR", "INT", 
                      "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_varDecl = 2
    RULE_printStmt = 3
    RULE_assignStmt = 4
    RULE_expr = 5
    RULE_term = 6
    RULE_factor = 7

    ruleNames =  [ "prog", "statement", "varDecl", "printStmt", "assignStmt", 
                   "expr", "term", "factor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    VAR=11
    INT=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PostLangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PostLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(PostLangParser.StatementContext,i)


        def getRuleIndex(self):
            return PostLangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = PostLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2066) != 0):
                self.state = 16
                self.statement()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
            self.match(PostLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(PostLangParser.VarDeclContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(PostLangParser.PrintStmtContext,0)


        def assignStmt(self):
            return self.getTypedRuleContext(PostLangParser.AssignStmtContext,0)


        def getRuleIndex(self):
            return PostLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = PostLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.varDecl()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.printStmt()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.assignStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(PostLangParser.VAR, 0)

        def expr(self):
            return self.getTypedRuleContext(PostLangParser.ExprContext,0)


        def getRuleIndex(self):
            return PostLangParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = PostLangParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(PostLangParser.T__0)
            self.state = 30
            self.match(PostLangParser.VAR)
            self.state = 31
            self.match(PostLangParser.T__1)
            self.state = 32
            self.expr(0)
            self.state = 33
            self.match(PostLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PostLangParser.ExprContext,0)


        def getRuleIndex(self):
            return PostLangParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = PostLangParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(PostLangParser.T__3)
            self.state = 36
            self.expr(0)
            self.state = 37
            self.match(PostLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(PostLangParser.VAR, 0)

        def expr(self):
            return self.getTypedRuleContext(PostLangParser.ExprContext,0)


        def getRuleIndex(self):
            return PostLangParser.RULE_assignStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignStmt(self):

        localctx = PostLangParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(PostLangParser.VAR)
            self.state = 40
            self.match(PostLangParser.T__1)
            self.state = 41
            self.expr(0)
            self.state = 42
            self.match(PostLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # TermContext

        def term(self):
            return self.getTypedRuleContext(PostLangParser.TermContext,0)


        def expr(self):
            return self.getTypedRuleContext(PostLangParser.ExprContext,0)


        def getRuleIndex(self):
            return PostLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PostLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PostLangParser.ExprContext(self, _parentctx, _parentState)
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 47
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 48
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==5 or _la==6):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 49
                    localctx.right = self.term(0) 
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # TermContext
            self.op = None # Token
            self.right = None # FactorContext

        def factor(self):
            return self.getTypedRuleContext(PostLangParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(PostLangParser.TermContext,0)


        def getRuleIndex(self):
            return PostLangParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PostLangParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_term, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 63
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PostLangParser.TermContext(self, _parentctx, _parentState)
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 58
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 59
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==7 or _la==8):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 60
                    localctx.right = self.factor() 
                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(PostLangParser.VAR, 0)

        def INT(self):
            return self.getToken(PostLangParser.INT, 0)

        def expr(self):
            return self.getTypedRuleContext(PostLangParser.ExprContext,0)


        def getRuleIndex(self):
            return PostLangParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = PostLangParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_factor)
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(PostLangParser.VAR)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(PostLangParser.INT)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.match(PostLangParser.T__8)
                self.state = 69
                self.expr(0)
                self.state = 70
                self.match(PostLangParser.T__9)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expr_sempred
        self._predicates[6] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




