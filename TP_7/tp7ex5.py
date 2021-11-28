import numpy as np
import matplotlib.pyplot as plt
from numpy.random import rand

print('########1########')

s = 5000


def bern(a, b, p):
    if rand() <= p:
        return b
    else:
        return a


steps = [(bern(-1, 1, 0.5)) for _ in range(s)]
walk = np.cumsum(steps)
x = np.linspace(0, s, s)
plt.plot(x, walk)
plt.ylabel("left to right")
plt.xlabel("0 to r")
plt.title('drunk walk, from (0, 0) to (r, 0)')
plt.figure()

print('########2########')

r = 500
s = 500

for i in range(r):
    steps = [(bern(-1, 1, 0.5)) for _ in range(s)]
    walk = np.cumsum(steps)
    x = np.linspace(0, s, s)
    plt.plot(x, walk)

plt.ylabel("left to right")
plt.xlabel("0 to r")
plt.title('500 drunk walks, from (0, 0) to (r, 0)')
plt.show()
