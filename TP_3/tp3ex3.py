from TP_2 import tp2ex5 as p

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

for i in A:
    res = p.pgcd(i, 26)
    if res == 1:
        print(i, 'is coprime with 26')

# 2)

