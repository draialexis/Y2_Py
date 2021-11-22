import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randint

# 1)

l1 = randint(0, 2, 100)

# 2)

s2 = np.sum(l1)

# 3)

sup_53 = 0
inf_eq_40 = 0


def pf():
    L = randint(0, 2, 100)
    res = np.sum(L)
    return res


# print("# of tails out of 100 throws:", pf())

"""
# a) & b)
if p € [0, 1], then the probability for a random int (€ [0, 1]) to belong
to [0, p] is equal to p...

I need to get into stats...

looking like 24-25% for sup_53
and 3% for inf_eq_40


IT'S A BELL CURVE /facepalm

"""

tries = 20000
results = []
for _ in range(tries):
    res = pf()
    results.append(res)
    if res > 53:
        sup_53 += 1
    if res <= 40:
        inf_eq_40 += 1

a = sup_53 / tries  # sample mean for sup_53
b = inf_eq_40 / tries  # sample mean for inf_eq_40
print('sample mean for sup_53:', sup_53, '/', tries, '=', a)
print('sample mean for inf_eq_40:', inf_eq_40, '/', tries, '=', b)

# 4)

my_bins = [(i + 1) for i in range(100)]

plt.hist(results, bins=my_bins)
plt.show()

test = [0]
print(test)
