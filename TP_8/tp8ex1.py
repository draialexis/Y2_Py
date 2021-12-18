import numpy as np
import matplotlib.pyplot as plt

plt.hist(np.sin(np.arange(0, 10000, 1)), bins=np.linspace(-1, 1, 100), edgecolor='black')
plt.show()

"""
hist des 10000 1er val de la suite, comparer les barres
"""

print("the terms given by sin(x) don't appear to be uniformly spaced within the [-1, 1] interval. Rounding?")
