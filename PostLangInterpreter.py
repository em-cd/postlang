from postlang.Stack import Stack

class PostLangInterpreter:
  def __init__(self):
    self.env: dict[str, int] = {} # To store environement variables
    self.stack = Stack()

  def run(self, rpn_statements):
    for stmt in rpn_statements:
      for token in stmt:
        match token:
          case '+':
            b, a = self.stack.pop(), self.stack.pop()
            self.stack.push(a + b)
          case '-':
            b, a = self.stack.pop(), self.stack.pop()
            self.stack.push(a - b)
          case '*':
            b, a = self.stack.pop(), self.stack.pop()
            self.stack.push(a * b)
          case '/':
            b, a = self.stack.pop(), self.stack.pop()
            self.stack.push(a // b)
          case 'print':
            print(self.stack.pop())
          case _ if token.startswith('='):
            # Take the string from the second character to strip the '='
            self.env[token[1:]] = self.stack.pop()
          case _:
            # It's a variable we have previously stored
            if token in self.env:
              self.stack.push(self.env[token])
            # It's a literal
            elif token.isdigit():
              self.stack.push(int(token))
            else:
              raise RuntimeError(f"Undefined variable or unknown token: '{token}'")

        # print(f"self.stack: {self.stack}")
        # print(f"Env:  {self.env}")
