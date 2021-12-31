"""
somme des 2 nombres de 6 chiffres qui sont des anagrammes l'un de l'autre et dont les produits par 8 sont des anagrammes des originaux
"""


def digits(n):
    res = []
    while n > 0:
        res.append(n % 10)
        n = n // 10
    return res


def is_ana(L1, L2):
    S1 = sorted(L1)
    S2 = sorted(L2)
    if S1 == S2:
        return 1
    else:
        return 0


# returns the sum of the first two such anagrams, but finds more
def anas(bracket, factor):
    min = int(pow(10, bracket - 1))
    max = int(((min * 10) - 1) / factor)
    print("min=", min, "max=", max)
    res = []
    for i in range(min, max + 1):
        if is_ana(digits(i), digits(i * factor)):
            res.append(i);
    print(res)
    if len(res) >= 2 and is_ana(digits(res[0]), digits(res[1])):
        return res[0] + res[1]
    else:
        return -1


print("sum of special anagrams in bracket?", anas(6, 8))
"""
anas(6, 8) → 230364
"""
