def pair(x, y):

    def get(i):
        if i == 0:
            return x
        if i == 1:
            return y

    return get


def select(p, i):
    return p(i)
