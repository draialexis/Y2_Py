import numpy as np
import matplotlib.pyplot as plt
import random

n = 300

arr = np.zeros((n, n), dtype=int)
for i in range(n):
    for j in range(n):
        arr[i, j] = random.randint(0, i + 1)

plt.matshow(arr, 0, cmap='hot')
plt.show()
