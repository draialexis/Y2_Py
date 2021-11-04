import sympy as sm

# 1)

sm.var('x y z')
p = 3 * (x ** 3) - (7 * (x ** 2) / 2) - (x / 2) + 1
s = sm.solve(p, x)
for i in range(len(s)):
    print('s[', i, '] =', s[i])

sm.pprint(p.subs(x, -0.5))
sm.pprint(p.subs(x, sm.Rational(2, 3)))
sm.pprint(p.subs(x, 1))

# 2)

row1 = 2 * y + 5 * z - 3
row2 = -3 * x + 2 * y - z + 1
row3 = -x + 2 * y + 2 * z - 5
m = [row1, row2, row3]
v = [x, y, z]
s_ = sm.solve(m, v)

print('x =', s_[x], '\ny =', s_[y], '\nz =', s_[z])  # it's a dictionary, not a list!
print(row1.subs(s_))
print(row2.subs(s_))
print(row3.subs(s_))  # subs accepts a dictionary as a parameter!
