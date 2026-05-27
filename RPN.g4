grammar RPN;

prog: expr EOF;

expr
  : expr expr operator
  | INT
  ;

operator
  : PLUS
  | MINUS
  | MULT
  | DIV
  ;

INT: [0-9]+ ;
PLUS: '+' ;
MINUS: '-';
MULT: '*';
DIV: '/';

WS : [ \t\r\n]+ -> skip;