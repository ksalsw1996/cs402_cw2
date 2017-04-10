bin_op = ['&', '|', '>', '<', '=']
uni_op = ['-']

def result(a):
    b = AFF(a)
    c = NNF(b)
    d = CNF(c)
    return d

def AFF(a):
    op = a.pop(0)
    if op in bin_op:
        if op == '>':
            return ['|', ['-', AFF(a[0])], AFF(a[1])]
        elif op == '<':
            return ['|', AFF(a[0]), ['-', AFF(a[1])]]
        else:
            return [op, AFF(a[0]), AFF(a[1])]
    else:
        if op in uni_op:
            return [op, AFF(a[0])]
        return [op]


def NNF(a):
    op = a.pop(0)
    if op in bin_op:
        return [op, NNF(a[0]), NNF(a[1])]
    if op == '-':
        b = a[0]
        op1 = b.pop(0)
        if op1 == '&':
            return NNF(['|', ['-', b[0]], ['-', b[1]]])
        elif op1 == '|':
            return NNF(['&', ['-', b[0]], ['-', b[1]]])
        elif op1 == '-':
            return NNF(b[0])
        else:
            return ['-', [op1]]
    else:
        return [op]


def CNF(a):
    op = a[0]
    if op == '&':
        return ['&', CNF(a[1]), CNF(a[2])]
    elif op == '|':
        return DISTR(CNF(a[1]), CNF(a[2]))
    else:
        return a


def DISTR(a, b):
    op = a[0]
    op1 = b[0]
    if op == '&':
        return ['&', DISTR(a[1], b), DISTR(a[2], b)]
    elif op1 == '&':
        return ['&', DISTR(a, b[1]), DISTR(a, b[2])]
    else:
        return ['|', a, b]
