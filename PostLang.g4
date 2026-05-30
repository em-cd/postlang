grammar PostLang;

prog
  : statement* EOF
  ;

statement
  : varDecl
  | printStmt
  | assignStmt
  ;

varDecl
  : 'let' VAR '=' expr ';'
  ;

printStmt
  : 'print' expr ';'
  ;

assignStmt
  : VAR '=' expr ';'
  ;

expr
  : left=expr op=('+'|'-') right=term
  | term
  ;

term
  : left=term op=('*'|'/') right=factor
  | factor
  ;

factor
  : VAR
  | INT
  ;

VAR: [a-zA-Z]+;
INT: [0-9]+ ;

WS : [ \t\r\n]+ -> skip;