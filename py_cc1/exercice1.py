# Alexis DRAI - 22001161
# 08/11/2021

import matplotlib.pyplot as plt
import numpy as np

## 1)

#le cercle unité
t = np.linspace(0, 2 * np.pi)
x = np.cos(t)
y = np.sin(t)
plt.plot(x, y)
# le polygone inscrit
x_p_i = [-0.5, 0.5, 1, 0.5, -0.5, -1, -0.5]
y_p_i = [-np.sqrt(3)/2, -np.sqrt(3)/2, 0, np.sqrt(3)/2, np.sqrt(3)/2, 0, -np.sqrt(3)/2]
plt.plot(x_p_i, y_p_i)
# le polygone extérieur
x_p_e = [-1/np.sqrt(3), 1/np.sqrt(3), 2/np.sqrt(3), 1/np.sqrt(3), -1/np.sqrt(3), -2/np.sqrt(3), -1/np.sqrt(3)]
y_p_e = [-1, -1, 0, 1, 1, 0, -1]
plt.plot(x_p_e, y_p_e)
#repère orthonormé
plt.axis('equal')
plt.title('ex1_1')
plt.figure()

## 2)

#le cercle unité
t = np.linspace(0, 2 * np.pi)
x = np.cos(t)
y = np.sin(t)
plt.plot(x, y)

n = 5
k_max = 6 * pow(2, n)
x_p_i = []
y_p_i = []
x_p_e = []
y_p_e = []
# le polygone inscrit avec n = 4
for i in range(1, k_max + 2): #+1 pour range, +1 pour fermer la boucle
    x_p_i_k = np.cos((2 * i * np.pi)/(k_max))
    y_p_i_k = np.sin((2 * i * np.pi)/(k_max))
    x_p_i.append(x_p_i_k)
    y_p_i.append(y_p_i_k)
    # le polygone extérieur avec n = 4
    coef_p_e = 1/np.cos(np.pi/k_max)
    x_p_e.append(coef_p_e * x_p_i_k)
    y_p_e.append(coef_p_e * y_p_i_k)
plt.plot(x_p_i, y_p_i)
plt.plot(x_p_e, y_p_e)

#repère orthonormé
plt.axis('equal')
plt.title('ex1_2')
plt.show()
print("ex1_2 : Les 2 polygones et le cercle sont presque impossibles à distinguer visuellement")

"""
Les 2 polygones et le cercle sont presque impossibles à distinguer visuellement
"""

## 3)

def s(n):
    if n == 0:
        return 0.5
    return np.sqrt(0.5 * (1 - np.sqrt(1 - pow(s(n-1), 2))))

def t(n):
    if n == 0:
        return 1/np.sqrt(3)
    return (np.sqrt(1 + pow(t(n-1), 2)) - 1) / t(n-1)

print('ex1_3')
for i in range(16):
    inf = 6 * pow(2, i) * s(i)
    sup = 6 * pow(2, i) * t(i)
    print('n =', i, ': pi est compris entre', inf , 'et', sup)


## 4)


print('ex1_4')
for i in range(16):
    inf = 6 * pow(2, i) * s(i)
    sup = 6 * pow(2, i) * t(i)
    if inf < np.pi and sup > np.pi:
        print('n =', i, ': valide')
    else:
        print('n =', i, ': non valide')

"""
notre approximation reste valide jusqu'à n = 12
"""

## 5)

"""
notre programme ne fournit pas d'approximation aussi précise qu'Al-Kashi

probablement à cause des approximations qui ont lieu avec les flottants
(on pourrait utiliser sympy pour utiliser des fractions réelles)
"""








































