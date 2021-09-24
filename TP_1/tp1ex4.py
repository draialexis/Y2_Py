#1)

def carre_plus(n):
    b = n*n + 2
    return b
    print("Ceci ne s'affichera pas!")

print(carre_plus(5))

sol1 = carre_plus(345) + carre_plus(567)
print('sol1 =', sol1)

#2)

def racines(a, b, c):
    d = pow(b, 2) - 4 * a * c
    if d > 0:
        return 2
    elif d == 0:
        return 1
    else:
        return 0

print('{x^2 + x - 2 = 0} présente', racines(1, 1, -2), 'solution(s)')
print('{4x^2 - 12x + 9 = 0} présente', racines(4, -12, 9), 'solution(s)')
print('{2x^2 + x + 1 = 0} présente', racines(2, 1, 1), 'solution(s)')