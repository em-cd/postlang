# PostLang - Infix to RPN Compiler

PostLang is a small compiled language that takes infix arithmetic expressions and compiles them to Reverse Polish Notation (RPN), which is then evaluated by a stack-based interpreter.

## Project Structure

```
.
├── PostLang.g4               # ANTLR grammar
├── main.py                   # Entry point
├── PostLangVisitorImpl.py    # Compiler: Parse tree to RPN token list
├── Interpreter.py            # Interpreter: executes RPN on a stack
├── Stack.py                  # Simple stack data structure
├── program.pl                # Example source file
└── postlang/                 # ANTLR-generated parser/lexer files
    ├── PostLangLexer.py
    ├── PostLangParser.py
    ├── PostLangVisitor.py
    └── ...

```

## Language features
- Integer arithmetic: `+`, `-`, `*`, `/` (integer division)
- Operator precedence and associativity handled by the grammar
- Support for parentheses, e.g. `(x + 2)`
- Variable declaration with `let`
- Variable assignment
- `print` statement

### Syntax
 
```
let x = 5;            // declare and initialise a variable
x = x + 1;            // reassign a variable
print x;              // print a value or expression
print x * 2 + 1;
```

## How It Works
 
The pipeline has three stages:
 
1. **Parsing** — ANTLR lexes and parses the source file into a parse tree.
2. **Compilation** — A visitor walks the parse tree and produces a flat list of RPN tokens for each statement. For example, `x * y + 1` becomes `x y * 1 +`. Variable assignments are stored as `=varname` tokens to distinguish them from variable reads.
3. **Interpretation** — The interpreter executes each RPN token list from left to right, using a stack. Operands are pushed; operators pop their arguments, compute, and push the result; `=varname` tokens pop the top of the stack and store it in the environment; `print` pops and prints.

 
## Usage
 
### Requirements
 
- Python 3.10+

### Install dependencies

```bash
pip install -r requirements.txt
```

### Generate the parser (if not already done)
 
```bash
antlr4 -Dlanguage=Python3 -visitor PostLang.g4 -o postlang
```
 
### Run a program
 
```bash
python main.py program.pl
```
 
Add `--debug` to print the parse tree and compiled RPN before execution:
 
```bash
python main.py program.pl --debug
```
 
 
## Example
 
**Input:**
 
```
let x = 2;
let y = 5;
let z = x * y;

x = x + 1;
y = x / 3;
 
print x;
print y;
print z;
```
 
**Compiled RPN (visible with `--debug`):**
 
```
2 =x 5 =y x y * =z x 1 + =x x 3 / =y x print y print z print
```
 
**Output:**
 
```
3
1
10
```

**Trace for `z = x * y` with `x=2, y=5`:**

RPN is: `x y * =z`
 
| Token | Stack      |
|-------|------------|
| `x`   | `2`        |
| `y`   | `2 5`      |
| `*`   | `10`       |
| `=z`  | *(empty)*  → `z = 10` |