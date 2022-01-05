import matplotlib.pyplot as plt
import numpy as np


def serp_carp(d):
    a = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])  # lvl1

    for k in range(1, d + 1):  # start from 1, stop at 6
        a = np.vstack((a, a, a))
        a = np.hstack((a, a, a))
        n, dmp = a.shape
        n = int(n / 3)
        for i in range(n, n * 2):
            for j in range(n, n * 2):
                # print("a[", i, "," , j, "]")
                a[i, j] = 0

    plt.matshow(a, cmap="Greys")
    plt.show()


serp_carp(6)
