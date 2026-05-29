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
  : expr operator expr
  | VAR
  | INT
  ;

operator
  : PLUS
  | MINUS
  | MULT
  | DIV
  ;

VAR: [a-zA-Z]+;
INT: [0-9]+ ;
PLUS: '+' ;
MINUS: '-';
MULT: '*';
DIV: '/';

WS : [ \t\r\n]+ -> skip;