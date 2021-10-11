# 1 & 2)

def fibo(n):
    res = 0
    if n < 0:
        print('oh no no no')
        return -1
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


# print('fibo_liste(', num1, ') =', fibo_liste(num1))
# fibo_liste(num1)

# 3)

def fibo_weird(n, mod):
    n_2 = 0
    n_1 = 1
    my_sum = 0
    fib = 0
    if n < 0:
        print('oh no no no')
        return -1
    if n == 0 or n == 1:
        return n
    for i in range(2, n + 1):
        fib = n_2 + n_1
        # print('fib =', fib)
        if fib % 2 == 0:
            my_sum += fib
            # print('sum =', sum)
        n_2 = n_1
        n_1 = fib

    return my_sum % mod

# print('fibo_weird(', 100000, ') =', fibo_weird(100000, 10000007))
# prints out "2676110"
