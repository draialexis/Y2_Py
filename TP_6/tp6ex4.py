import matplotlib.pyplot as plt
import numpy as np

nb_occ = [
    ["A", 0],
    ["B", 0],
    ["C", 0],
    ["D", 0],
    ["E", 0],
    ["F", 0],
    ["G", 0],
    ["H", 0],
    ["I", 0],
    ["J", 0],
    ["K", 0],
    ["L", 0],
    ["M", 0],
    ["N", 0],
    ["O", 0],
    ["P", 0],
    ["Q", 0],
    ["R", 0],
    ["S", 0],
    ["T", 0],
    ["U", 0],
    ["V", 0],
    ["W", 0],
    ["X", 0],
    ["Y", 0],
    ["Z", 0],
]

print("########EX1########\n")

f = open("sherlock.txt", encoding="utf8")
for line in f:
    line = line.upper().rstrip()
    for ch in line:
        for couple in nb_occ:
            if ch == couple[0]:
                couple[1] += 1
f.close()

print("letters by occurrence:", nb_occ)

print("\n########EX2########\n")


common_10 = sorted(nb_occ, key=lambda x: x[1], reverse=True)[:10]
print("10 most common letters:", common_10)

print("\n########EX3########\n")

total_letters = 0
for entry in nb_occ:
    total_letters += entry[1]

letters = []
ratios = []
width = 0.5
index = np.arange(10)

for entry in common_10:
    letters.append(entry[0])
    ratios.append(entry[1] * 100 / total_letters)

# plt.bar(index, ratios, width, label=letters)
plt.bar(index, ratios, width, color=np.random.rand(len(index), 3), label=letters)

title = 'Occurences of characters, in percents'

plt.xticks(index, letters)
plt.title(title)
plt.ylabel("% of the text")
plt.show()
