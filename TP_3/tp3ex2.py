import tp3ex1 as prv


# 1)

def code_str(string):
    words = string.split()
    res = []
    for word in words:
        res.append(prv.code_mot(word))
    return res


def decode_str(nums):
    str_arr = []
    for num_arr in nums:
        str_arr.append(prv.decode_mot(num_arr))
    res = " ".join(str_arr)
    return res


def encypher(num, d):
    # print(num ,'->', num+d)
    num += d
    if num >= 26:
        # print('___',num ,'->', num%26)
        num = num % 26
    return num


def cesar(string, d):
    nums = code_str(string)
    nums_delta = []
    for num_arr in nums:
        nums_delta_i = []
        for num in num_arr:
            nums_delta_i.append(encypher(num, d))
        nums_delta.append(nums_delta_i)

    res = decode_str(nums_delta)
    return res


my_str = 'THAT WAS ROUGH'
cypher = cesar(my_str, 3)
print(cypher)
