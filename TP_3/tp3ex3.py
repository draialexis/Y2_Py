from TP_2 import tp2ex5 as p
import tp3ex1 as prv

A = [0,
     1,
     2,
     3,
     4,
     5,
     6,
     7,
     8,
     9,
     10,
     11,
     12,
     13,
     14,
     15,
     16,
     17,
     18,
     19,
     20,
     21,
     22,
     23,
     24,
     25]


# "Supposons que 'a' est premier avec 26" -> pgcd(a, 26) = 1

# 1)

# for i in A:
#     res = p.pgcd(i, 26)
#     if res == 1:
#         print(i, 'is coprime with 26')


# 2)
# au lieu d'appliquer un decalage d a chaque lettre
# codee f(n) = n+d % 26 (n € [0; 25]),
# on applique une fonction affine
# f(n) = an+b % 26
# (pour une valeur admissible de a).

def affine(string, a, b):
    nums = prv.encode(string)
    if not p.pgcd(a, 26) == 1:
        print(p.pgcd(a, 26))
        print("'a' € [0, 25] must be coprime with 26")
        for i in A:
            res = p.pgcd(i, 26)
            if res == 1:
                print(i, 'is coprime with 26')

    nums_delta = []
    for num in nums:
        if isinstance(num, int):
            nums_delta.append((a * num + b) % 26)
        elif num == ' ':
            nums_delta.append(num)

    res = prv.decode(nums_delta)
    return res


# my_string = 'KILL ME NOW'
# print(affine(my_string, 25, 7))


# 3)

cst = 26


def inverse(a):
    for i in range(1, cst):
        a_m = a % cst
        i_m = i % cst
        a_i_m = a_m * i_m % cst
        if a_i_m == 1:
            return i
    return 0


for x in range(1, cst):
    inv = inverse(x)
    if inv == 0:
        print('cannot find an "inverse modulo 26" for', x)
    else:
        print(x, '*', inv, '%', cst, '=', 1)
