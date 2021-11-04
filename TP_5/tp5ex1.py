import sympy as sm
from sympy import cos, sin, sqrt, pi

sm.var('x y z')
# print(x + y + 2*x + z + 1)

# 1)

p1 = (x - 1) * (x - 2) * (x + 3)
print(p1, "=")
sm.pprint(sm.expand(p1))

p2 = x ** 3 - 39 * x - 70

print('\n', p2, "=")
sm.pprint(sm.factor(p2))

p3 = 1 / (x + 1) + 1 / y + 1 / z
print('\n', p3, '=')
sm.pprint(sm.ratsimp(p3))
# print(sm.together(p3))

p4 = (2 * (x ** 2) + 4 * x + 3) / p2
print('\n', p4, '=')
sm.pprint(sm.apart(p4))

p5 = cos(x + y) + cos(x - y) + sin(x + y) + sin(x - y)
print('\n', p5, '=\n', sm.simplify(p5))

print('\n', sm.factor(x ** 2 + 2 * x + 1))

p61 = 2 * (x ** 2) - 3 * x + 1
print('\n', p61, '; x=5 =>\n', p61.subs(x, 5))

p62 = p61.subs(x, y + 1) - p61.subs(x, y - 1)
print('\n(', p61.subs(x, y + 1), ') - (', p61.subs(x, y - 1), ') =')
sm.pprint(sm.simplify(p62))

print(sqrt(10).evalf())
x = pi
print((x ** 2 + x + 1).evalf())
print(pi.evalf(500))