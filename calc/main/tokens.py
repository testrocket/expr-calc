class Token(object):

    UNKNOWN = 0
    ID = 1
    INT = 2
    DOUBLE = 3
    PAREN_LEFT = 4
    PAREN_RIGHT = 5
    OP_ADD = 6
    OP_SUB = 7
    OP_MUL = 8
    OP_DIV = 9
    OP_POW = 10
    OP_EQ = 11
    PUNC_SEMICOLON = 20

    OPERATORS = [OP_ADD, OP_SUB, OP_MUL, OP_DIV, OP_POW, OP_EQ]

    def __init__(self, value, ttype):
        self.value = value
        self.ttype =  ttype

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


def tokenize(expr):
    tokens_list = []

    i = 0
    n = len(expr)
    while i < n:
        c = expr[i]

        k = i + 1
        if c.isspace():
            i = skip_while(k, expr, lambda ch: ch.isspace())
            continue

        if c.isalpha():
            k = skip_while(k, expr, lambda ch: ch.isalpha() or ch.isdigit())
            ttype = Token.ID
        elif c.isdigit():
            k = skip_while(k, expr, lambda ch: ch.isdigit())
            if k < n and expr[k] == '.':
                k = skip_while(k + 1, expr, lambda ch: ch.isdigit())
                ttype = Token.DOUBLE
            else:
                ttype = Token.INT
        elif c == '+':
            ttype = Token.OP_ADD
        elif c == '-':
            ttype = Token.OP_SUB
        elif c == '*':
            ttype = Token.OP_MUL
        elif c == '/':
            ttype = Token.OP_DIV
        elif c == '=':
            ttype = Token.OP_EQ
        elif c == '^':
            ttype = Token.OP_POW
        elif c == '(':
            ttype = Token.PAREN_LEFT
        elif c == ')':
            ttype = Token.PAREN_RIGHT
        elif c == ';':
            ttype = Token.PUNC_SEMICOLON
        else:
            ttype = Token.UNKNOWN

        tokens_list.append(Token(expr[i:k], ttype))
        i = k

    return tokens_list


def skip_while(start, expr, condition):
    while start < len(expr) and condition(expr[start]):
        start += 1
    return start
