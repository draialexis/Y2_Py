def code_une(lt):
    switcher = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
        'I': 8,
        'J': 9,
        'K': 10,
        'L': 11,
        'M': 12,
        'N': 13,
        'O': 14,
        'P': 15,
        'Q': 16,
        'R': 17,
        'S': 18,
        'T': 19,
        'U': 20,
        'V': 21,
        'W': 22,
        'X': 23,
        'Y': 24,
        'Z': 25,
    }
    return switcher.get(lt, '#')

def decode_une(c):
    switcher = {
        0: 'A',
        1: 'B',
        2: 'C',
        3: 'D',
        4: 'E',
        5: 'F',
        6: 'G',
        7: 'H',
        8: 'I',
        9: 'J',
        10: 'K',
        11: 'L',
        12: 'M',
        13: 'N',
        14: 'O',
        15: 'P',
        16: 'Q',
        17: 'R',
        18: 'S',
        19: 'T',
        20: 'U',
        21: 'V',
        22: 'W',
        23: 'X',
        24: 'Y',
        25: 'Z',
    }
    return switcher.get(c, '#')

def code_mot(mot):
    chars = list(mot)
    res = list(map(code_une, chars))
    return res

def decode_mot(nums):
    chars = list(map(decode_une, nums))
    res = "".join(chars)
    return res

# 1)

def code_str(str):
    words = str.split()
    res = []
    for word in words:
        res.append(code_mot(word))
    return res

def decode_str(nums):
    str_arr = []
    for num_arr in nums:
        str_arr.append(decode_mot(num_arr))
    res = " ".join(str_arr)
    return res

def encypher(num, d):
    #print(num ,'->', num+d)
    num += d
    if num >= 26:
        #print('___',num ,'->', num%26)
        num = num % 26
    return num


def cesar(str, d):
    nums = code_str(str)
    nums_delta = []
    for num_arr in nums:
        nums_delta_i = []
        for num in num_arr:
            nums_delta_i.append(encypher(num, d))
        nums_delta.append(nums_delta_i)

    res = decode_str(nums_delta)
    return res

str = 'THAT WAS ROUGH'
cypher = cesar(str, 3)
print(cypher)

