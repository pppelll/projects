def permutate1(l, s='', cand=[]):
    ll = len(l) - 1
    if l != []:
        for n in range(len(l)):
            ns = s
            ul = l[ : ]
            ns += ul[ll - n]
            ul.remove(ul[ll - n])
            cand.append(ns)
            permutate1(ul, ns)
            if ul == []:
                cand.append(ns)
    return cand


letters = ['a', 'b', 'c', 'd', 'e']
#letters = "abcde"
print(permutate1(letters))
