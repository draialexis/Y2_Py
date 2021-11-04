import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2 * np.pi)
x = np.cos(t)
y = np.sin(t)
plt.axis('equal')
plt.plot(x, y)
plt.plot([-np.sqrt(3)/2, np.sqrt(3)/2, 0, -np.sqrt(3)/2], [-0.5, -0.5, 1, -0.5])
plt.grid()
plt.show()
