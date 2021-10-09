import numpy as np

sol = 0

n = 1
isFound = False

while not isFound:
    if n * (n + 1) / 2 > 1000000:
        sol = n
        print('solution is:', sol)
        print('(', n, '(', n, '+', 1, ')', '/', 2, '=', (n * (n + 1)) / 2)
        print('(', n - 1, '(', n - 1, '+', 1, ')', '/', 2, '=', (n * (n - 1)) / 2)
        isFound = True
    n += 1
