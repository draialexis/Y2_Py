import sympy as sm

n = 0
x = sm.Float(0.23)

while not n > 60:
    x = (4 * x * (1 - x)).evalf(500)
    if n % 10 == 0:
        print('at', n, ', x =', x)
    n += 1

print('and now...')

n = 0
x = sm.Float(0.23)

while not n > 60:
    x = ((4 * x) - (4 * x ** 2)).evalf(500)
    if n % 10 == 0:
        print('at', n, ', x =', x)
    n += 1

# the results are much much closer, although still not strictly the same
