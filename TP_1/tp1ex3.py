import numpy as np

# 1)

sol1_1 = np.sin(pow(np.pi, 2))
print('sol1_1 =', sol1_1)

sol1_2 = np.log(2050)
print('sol1_2 =', sol1_2)

# 2)

sol2_1 = np.log10(90)
print('sol2_1 =', sol2_1)
sol2_2 = np.log10(99)
print('sol2_2 =', sol2_2)
sol2_3 = np.log10(101)
print('sol2_3 =', sol2_3)
sol2_4 = np.log10(120)
print('sol2_4 =', sol2_4)
sol2_5 = np.log10(999)
print('sol2_5 =', sol2_5)
sol2_6 = np.log10(500)
print('sol2_6 =', sol2_6)
sol2_7 = np.log10(1001)
print('sol2_7 =', sol2_7)


# tells us how many times the number can be divided by 10 before becoming < 1

# 3)

def int_part_size(x):
    sol = int(np.log10(x) + 1)
    return sol


sol3_1 = int_part_size(2)
print('sol3_1 =', sol3_1)
sol3_2 = int_part_size(25)
print('sol3_2 =', sol3_2)
sol3_3 = int_part_size(2566)
print('sol3_3 =', sol3_3)
sol3_4 = int_part_size(pow(2, 64) - 1)
print('sol3_4 =', sol3_4)
