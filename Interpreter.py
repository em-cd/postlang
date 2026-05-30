from Stack import Stack

# An Interpreter for PostLang. Call run() with a list of RPN statements generated
# by the compiler (PostLangVisitorImpl)
class Interpreter:
  def __init__(self):
    self.env: dict[str, int] = {} # To store environment variables
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
            # Is it a variable we have previously stored?
            if token in self.env:
              self.stack.push(self.env[token])
            else:
              # Try if it is an integer literal
              try:
                self.stack.push(int(token))
              except ValueError:
                raise RuntimeError(f"Undefined variable or unknown token: '{token}'")