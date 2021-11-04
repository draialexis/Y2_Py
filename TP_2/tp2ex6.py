# 1)

def pgcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


print('pgcd(123456, 234567) =', pgcd(123456, 234567))


# 2)

def phi(n):
    if n == 0:
        print('no no no no no')
        return -1
    count = 0
    for i in range(1, n + 1):
        if pgcd(i, n) == 1:
            # print(i, '/', n)
            count += 1
    return count


print('phi(10) =', phi(10))
print('phi(30) =', phi(30))


# 3)

def farey(n):
    if n == 0:
        print('no no no no no')
        return -1
    count = 1
    # print('0 / 1')
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if pgcd(i, j) == 1 and i < j:
                # print(i, '/', j)
                count += 1
    # print('1 / 1')
    count += 1
    return count


print('farey(4) =', farey(4))

for i in range(10, 31):
    print('farey(', i, ') =', farey(i))
