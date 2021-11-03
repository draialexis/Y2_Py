import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(-2, 2, 400)
# y = x**2

# plt.plot(x, y)
# plt.plot(x,4 - x**2)
# plt.axis("equal")
# plt.show()

x = np.linspace(-10, 10, 500)
y = np.sin(x) / x

plt.plot(x, y)
plt.figure()

x = np.linspace(0, 20, 500)
y = np.sin(x ** 2)

plt.plot(x, y)
plt.show()
