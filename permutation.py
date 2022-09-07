#writing a function to return permutations of a given set of letters

test_list = ['a', 'b', 'c', 'd', 'e']


def p1(n, r):
    if n == 0:
        return r
    r = p1(n - 1, r * n)
    return r

def perm(inventory, candidate):
    for i in range(len(inventory)):
        c = inventory.delete(i)
        perm(inventory, candid)


def permutate(list):
    p = ''
    pl = []
    ch = 0
    for n1 in range(5):
        for n2 in range(5):
            for n3 in range(5):
                for n4 in range(5):
                    for n5 in range(5):
                        p += (list[n1] + list[n2] + list[n3] + list[n4] + list[n5])
                        for i in range (5):
                            if p.count(list[i]) > list.count(list[i]):
                                ch += 1
                        if ch == 0:
                            pl.append(p)
                            print(p)
                        ch = 0
                        p = ''

    return pl
permutate(test_list)


def permutateRecursion(list):
    p = ''
    pl = []
    ch = 0
    ft = len(list)
    dl = factorial(len(list))


    if len(pl) >=
    for n in range(len(list):
        p += list[n]
        permutateRecursion




##feels like theres a way better way to do this. i just dont know how to bring it out
##for now this is a rough-n-ready permutator to be good enough until i know how to better use iterators.
