from random import randint

import matplotlib.pyplot as plt
import numpy as np

n = 300

A = np.zeros((n, n), dtype=int)
for i in range(n):
    for j in range(n):
        A[i, j] = randint(0, i + 1)

plt.matshow(A, 0, cmap='hot')
plt.show()
