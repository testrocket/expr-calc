import tokens

"""parse expression using Reverse Polish Notation algorithm"""
def parse_rpn(expr):

    tokens_list = tokens.tokenize(expr)

    result, tmp = [], []
    for token in tokens_list:
        if token.ttype in [tokens.Token.INT, tokens.Token.DOUBLE]:
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

    while tmp:
        result.append(tmp.pop())
    return result

def operator_priority(token):
    tt = token.ttype
    if tt == tokens.Token.OP_ADD or tt == tokens.Token.OP_SUB:
        return 1
    elif tt == tokens.Token.OP_MUL or tt == tokens.Token.OP_DIV:
        return 2
    elif tt == tokens.Token.OP_POW:
        return 3
    return -1

