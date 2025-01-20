def curried_pow(x):

    def h(y):
        return pow(x, y)

    return h


curried_pow(2)(4)
