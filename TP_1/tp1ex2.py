import numpy as np
n = 1
isFound = False
while not isFound:
    if n > np.sqrt(2000000 - n):
        print('solution is:',n)
        print('(', n, '(', n, '+', 1, ')', '/', 2 ,'=', (n*(n+1))/2)
        print('(', n-1, '(', n-1, '+', 1, ')', '/', 2 ,'=', (n*(n-1))/2)
        isFound = True
    n += 1