import matplotlib.pyplot as plt
from numpy.random import rand

print('########1########')


def bern(a, b, p):
    if rand() <= p:
        return b
    else:
        return a


print('should return 1:', bern(-1, 1, 1.0))
print('should return -1:', bern(-1, 1, 0.0))
print('should return -1 or 1 at equal probs:', bern(-1, 1, 0.5))

print('########2########')

L = []

for i in range(100):
    L.append(bern(-1, 1, 0.3))

plt.hist(L, bins=2, edgecolor='black')
plt.show()
