
def perc(n, m = None):
    p = n if m is None else n / m
    p = p * 1000
    p = int(p)
    p = p / 10
    return p
    