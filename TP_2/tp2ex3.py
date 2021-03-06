from math import factorial


# 1)

def inverse(L):
    return L[::-1]


L = [7, 3, 2, 5, 9]
print(L)
L = inverse(L)
print(L)


# 2)

def dec(b):
    res = 0
    for i, digit in enumerate(b[::-1]):
        res += pow(2, i) * digit
    return res


list1 = [1, 1, 0, 1]  # 13
print(list1, '(b10) =', dec(list1))

list2 = [1, 0, 1, 1, 1, 0, 0, 1]  # 185
print(list2, '(b10) =', dec(list2))

# 3)

list3 = [1, 1, 0, 1, 1, 0, 0]
list4 = [1, 0, 1, 0, 1, 0, 1, 0]
print(list3, '+', list4, '=', (dec(list3) + dec(list4)))  # like this?


# 4)

def binaire(n):
    res = []
    while n > 0:
        res.append(n % 2)
        n = n // 2
    return res[::-1]


num1 = 13
print(num1, '(b2) =', binaire(num1))
num2 = 278
print(num2, '(b2) =', binaire(num2))

# 5)

print(list3, '+', list4, '=', binaire((dec(list3) + dec(list4))))  # like this?

# 6)
factbin = binaire(factorial(50))
print(factorial(50), '(b2) =', factbin)
print('length:', len(factbin))
