import numpy as np
import matplotlib.pyplot as plt
import random

n = 300

A = np.zeros((n, n), dtype=int)
for i in range(n):
    for j in range(n):
        A[i, j] = random.randint(0, i + 1)

plt.matshow(A, 0, cmap='hot')
plt.show()
