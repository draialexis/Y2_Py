import numpy as np
import matplotlib.pyplot as plt
from numpy.random import rand

print('########1########')


def bern(a, b, p):
    r = rand()
    if r <= p:
        return b
    else:
        return a


steps = [(bern(-1, 1, 0.5)) for _ in range(10)]
walk = np.cumsum(steps)
print(steps)
print(walk)
# plt.scatter()
