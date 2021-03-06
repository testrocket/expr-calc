import tokens

"""parse expression using Reverse Polish Notation algorithm"""
def parse_rpn(expr):

    tokens_list = tokens.tokenize(expr)

    result, tmp = [], []
    i, n = 0, len(tokens_list)
    while i < n:
        token = tokens_list[i]
        if token.ttype in [tokens.Token.INT, tokens.Token.DOUBLE]:
            result.append(token)
        elif token.ttype == tokens.Token.ID:
            if (i + 1) < n and tokens_list[i + 1].ttype == tokens.Token.PAREN_LEFT:
                tmp.append(token)
            else:
                result.append(token) 
        elif token.ttype == tokens.Token.PAREN_LEFT:
            tmp.append(token)
        elif token.ttype in tokens.Token.OPERATORS:
            op_priority = operator_priority(token)
            while tmp and operator_priority(tmp[len(tmp) - 1]) >= op_priority:
                result.append(tmp.pop())
            tmp.append(token)
        elif token.ttype == tokens.Token.PAREN_RIGHT:
            while tmp and tmp[len(tmp) - 1].ttype != tokens.Token.PAREN_LEFT:
                result.append(tmp.pop())
            tmp.pop()

            if tmp and tmp[len(tmp) - 1].ttype == tokens.Token.ID:
                result.append(tmp.pop())

        i += 1

    while tmp:
        result.append(tmp.pop())
    return result

def operator_priority(token):
    tt = token.ttype
    if tt == tokens.Token.OP_EQ:
        return 0
    elif tt == tokens.Token.OP_ADD or tt == tokens.Token.OP_SUB:
        return 1
    elif tt == tokens.Token.OP_MUL or tt == tokens.Token.OP_DIV:
        return 2
    elif tt == tokens.Token.OP_POW:
        return 3
    return -1
