import sympy as sm
from sympy import diff

sm.var('x')

e1 = ((x ** 2) / 2) + (x - 1)

# tangent at 2: y_ = f'(2) * (x-2) + f(2)

e1_ = diff(e1, x)
e2 = e1_.subs(x, 2) * (x - 2) + e1.subs(x, 2)

sm.plot(e1, e2, (x, 0, 4))
