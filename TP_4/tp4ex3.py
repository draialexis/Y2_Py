import numpy as np
import matplotlib.pyplot as plt

# 1)

t = np.arange(0.3, 2, 0.2)
x = np.linspace(0, 1, 100)
for i in range(len(t)):
    y = pow(x, t[i])
    plt.plot(x, y)
plt.axis('equal')
plt.grid()
plt.show()
