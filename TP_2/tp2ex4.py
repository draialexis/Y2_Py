#1 & 2)

def fibo(n):
    res = 0
    if n < 0:
        print('oh no no no')
        return -1
        quit()
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        res += (fibo(n - 1) + fibo(n - 2))

    return res

def fibo_liste(n):
    res = []

    for i in range(0, n + 1):
        res.append(fibo(i))

    return res


num1 = 20
print('fibo_liste(', num1, ') =', fibo_liste(num1))
#fibo_liste(num1)

#3)

def fibo_weird(n):
    fib = 0
    res = 0
    if n < 0:
        print('oh no no no')
        return -1
        quit()
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib += (fibo(n - 1) + fibo(n - 2))
        if fib % 2 == 0:
            res += fib

    return res

print('fibo_weird(', 100000, ') =', fibo_weird(num1))
