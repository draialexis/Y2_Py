def div35(n):
    if n < 3:
        return 0

    i = 3
    sol = 0
    while i < n:
        if (i % 3 == 0) or (i % 5 == 0):
            sol += i
        i += 1
    return sol

print('div35(10) =', div35(10))
print('div35(45) =', div35(45))
print('div35(1000) =', div35(1000))
print('div35(2000) + div35(3000) =', div35(2000) + div35(3000))

#div35(2000) + div35(3000) = 3_030_168