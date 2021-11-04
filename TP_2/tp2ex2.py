import math as m

# 1)

# v_n = int_0-1((x^(n-1)/(a+x))dx)
# 0 ≤ x ≤ 1   (<== "int_0-1")
# a ≤ a+x ≤ a+1
# 1/(a+1) ≤ 1/(a+x) ≤ 1/a
# x^(n-1)/(a+1) ≤ x^(n-1)/(a+x) ≤ x^(n-1)/a
# int_0-1((x^(n-1)/(a+1))dx) ≤ int_0-1((x^(n-1)/(a+x))dx) ≤ int_0-1((x^(n-1)/a)dx)
# 1/(n*(a+1)) ≤ v_n ≤ 1/(n*a)
# sandwich ==> v_n = 0 when n->inf+

# v_n = int_0-1((x^(n-1)/(a+x))dx)
# v_1 = int_0-1((1/(a+x))dx) = int_0-1((ln(a+x))dx) = ln(a+1) - ln(a)
# v_1 = ln((a+1)/a)

# v_n + a*v_n-1 = int_0-1((x^(n-1)/(a+x))dx) + int_0-1((a*x^(n-2)/(a+x))dx)
# = int_0-1((x^(n-2)*(x+a)/(a+x))dx)
# = int_0-1(x^(n-2)dx) = 1/(n-1) = v_n + a*v_n-1
# ==> v_n = 1/(n-1) - a*v_n-1

# 2)

a = 3

v = m.log((1 + a) / a)
print('v1 =', v)
prev = v
n = 2  # (!) n >= 2

while not n > 40:
    v = (1 / (n - 1)) - (a * prev)
    prev = v
    print('at n =', n, ', v =', v)

    n += 1

    # this gets wild... v -> 0 when n -> + inf, but rounding error seems to
    # make v spike back up at around n = 30
    # v40 = 253.080... somehow

print('yaouch')

# 3)

v = ((1 / 180) + (1 / 240)) / 2
print('v60 =', v)
prev = v
n = 60

while not n < 40:
    v = - (prev - (1 / (n - 1)) / a)
    prev = v
    print('at n =', n, ', v =', v)

    n -= 1

print('that\'s better')
