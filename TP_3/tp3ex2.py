import tp3ex1 as prv


# 1)
# 2)

def cesar(string, d, is_decypher):
    if is_decypher:
        d = -1 * d
    nums = prv.encode(string)
    nums_delta = []
    for num in nums:
        if isinstance(num, int):
            nums_delta.append((num + d) % 26)
        elif num == ' ':
            nums_delta.append(num)

    res = prv.decode(nums_delta)
    return res

# 3)

# my_str = 'CE MESSAGE EST CONFIDENTIEL'
# delta = -11
# print(my_str, '| delta =', delta)

# encyphered = cesar(my_str, delta, 0)
# print(encyphered)
# decyphered = cesar(encyphered, delta, 1)
# print(decyphered)

# 4)

# test = 'KYV RIK FW GIFXIRDDZEX ZJ KYV RIK FW FIXREZQZEX TFDGCVOZKP'
# for i in range(1, 26):
#     candidate = cesar(test, i, 1)
#     result = candidate.find('THE')
#     if result >= 0:
#         print('i =', i, '|', candidate)

# i = 17 | THE ART OF PROGRAMMING IS THE ART OF ORGANIZING COMPLEXITY
# (E. W. Dijkstra)
