import numpy as np
import matplotlib.pyplot as plt
from numpy.random import rand

print('########1########')


def un_pas():
    x = rand()
    if x < 0.25:
        return np.array([1, 0])
    elif x < 0.5:
        return np.array([0, 1])
    elif x < 0.75:
        return np.array([-1, 0])
    else:
        return np.array([0, -1])


print('########2########')


def marche_2d(n):
    xs = [0]
    ys = [0]
    pos = np.array([0, 0])
    plt.scatter(xs, ys, s=50, color='r')
    for i in range(1, n):
        pos = pos + un_pas()
        xs.append(pos[0])
        ys.append(pos[1])
    plt.plot(xs, ys, color='b')
    plt.scatter(xs[-1], ys[-1], s=50, color='g')
    plt.axis('equal')
    plt.legend("nda")
    plt.show()


marche_2d(100)
