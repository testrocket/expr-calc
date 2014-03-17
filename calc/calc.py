import math
from main import parser, tokens

def calculate(expr):
    parse_result = parser.parse_rpn(expr)

    stack = []
    symbol_table = {
        "sin": lambda stack: stack.append(math.sin(float(stack.pop()))),
        "cos": lambda stack: stack.append(math.cos(float(stack.pop()))),
        "rad": lambda stack: stack.append(math.radians(stack.pop())),
        "deg": lambda stack: stack.append(math.degrees(stack.pop())),
        "int": lambda stack: stack.append(int(stack.pop())),
        "float": lambda stack: stack.append(float(stack.pop())),
    }

    for token in parse_result:
        tt = token.ttype
        if tt == tokens.Token.INT:
            stack.append(int(token.value))
        elif tt == tokens.Token.DOUBLE:
            stack.append(float(token.value))
        elif tt == tokens.Token.OP_ADD:
            stack.append(stack.pop() + stack.pop())
        elif tt == tokens.Token.OP_SUB:
            stack.append(stack.pop() - stack.pop())
        elif tt == tokens.Token.OP_MUL:
            stack.append(stack.pop() * stack.pop())
        elif tt == tokens.Token.OP_DIV:
            b, a = stack.pop(), stack.pop()
            stack.append(a / b)
        elif tt == tokens.Token.OP_POW:
            b, a = stack.pop(), stack.pop()
            stack.append(a ** b)
        elif tt == tokens.Token.ID:
            func = symbol_table[token.value]
            func(stack)
    return stack.pop()
