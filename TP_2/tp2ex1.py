# 1)

n = 0
x = 0.23

while not n > 60:
    x = 4 * x * (1 - x)
    if n == 10 or n == 60:
        print('at', n, ', x =', x)
    n += 1

print('and now...')
# 2)

n = 0
x = 0.23

while not n > 60:
    x = (4 * x) - (4 * x ** 2)
    if n == 10 or n == 60:
        print('at', n, ', x =', x)
    n += 1

print('huh?')
# different results for each expression, even though they're formally the same
# computers struggle with precision on floats, limited number of bits
# => approximation and errors

# neither of these 2 seem correct, I might check later
