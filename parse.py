bin_op = ['&', '|', '>', '<', '=']
uni_op = ['-']
def bin_divide(a):
    token = a.pop(0)
    first = [token]
    if token in bin_op:
        val = 2
    elif token in uni_op:
        val = 1
    else:
        return (first, a)
    for i in range(len(a)):
        token = a.pop(0)
        first.append(token)
        if token in bin_op:
            val += 1
        elif token not in uni_op:
            val -= 1
        if val == 0:
            return (first, a)


def parse(a):
    token = a.pop(0)
    if token in bin_op:
        fir, sec = bin_divide(a)
        return [token, parse(fir), parse(sec)]
    elif token in uni_op:
        return [token, parse(a)]
    else:
        return [token]
