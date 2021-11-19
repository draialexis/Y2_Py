import matplotlib.pyplot as plt

dt = []
co = []
cma = []
cmi = []
cc = []

with open("cac40.csv", encoding="utf8") as f:
    for line in f:
        line = line.replace(",", ".")
        data = line.split(";")
        dt.append(data[1])
        co.append(float(data[2]))
        cma.append(float(data[3]))
        cmi.append(float(data[4]))
        cc.append(float(data[5]))

print("########EX1########\n")

print("number of entries:", len(co))

print("\n########EX2########\n")

min_co = min(co)
min_co_ind = co.index(min_co)
min_co_dt = dt[min_co_ind]

print("min_co:", min_co)
print("date of min_co:", min_co_dt)

print("\n########EX3########\n")

acc = []

for i in range(len(co)):
    acc.append(cc[i] - co[i])

plt.plot(range(len(acc)), acc)
# plt.show()

"""
we can't tell what's what, using a curve
"""

neg_acc = 0
pos_acc = 0
avg_gain = 0
avg_loss = 0

for val in acc:
    if val > 0:
        pos_acc += 1
        avg_gain += val
    if val < 0:
        neg_acc += 1
        avg_loss += val

avg_gain /= pos_acc
avg_loss /= neg_acc

width = 0.5
start = 0.25
title = 'Nature des accroissements du CAC40 entre le ' + dt[0] + ' et le ' + dt[-1]
plt.bar(start, pos_acc, width, color='g', label='pos')
plt.bar(start + width, neg_acc, width, color='orange', label='neg')
plt.xticks([], [])
plt.legend()
plt.title(title)
# plt.show()

print("1133 jours avec un accroissement positif, 1109 -- negatif")

print("\n########EX4########\n")

print('total gain or loss with naive strategy:', sum(acc))
print('average loss:', abs(avg_loss), '-- average gain:', avg_gain)

"""
although there were more gain days than there were loss days, 
the average loss was greater than the average gain
"""
