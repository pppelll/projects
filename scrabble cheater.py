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
dict = open(r'/Users/pel/Documents/python projects/dict.en', 'r')
stripped_dict = []
poss_plays = []
words = dict.readlines()
for word in words:
    stripped_dict.append(word.strip('\n'))
print(stripped_dict)

#INSERT YOUR LETTERS HERE!
letters = ['d', 'e', 'm', 'o', 'n', 'a']

candidates = permutate1(letters)

for word in candidates:
    if word in stripped_dict:
        poss_plays.append(word)
print(poss_plays)
