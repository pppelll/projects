def p1(n, r):
    if n == 0:
        return r
    r = p1(n - 1, r * n)
    return r

print(p1(5, 1))


def p2(n, r):
    r = r * (r - 1)
