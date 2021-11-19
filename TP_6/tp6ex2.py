import matplotlib.pyplot as plt

loc = []
long = []
lat = []
pop = []
f = open("villes.csv", encoding="utf8")

next(f)
for line in f:
    data = line.split(';')
    loc.append(data[1].lower())
    long.append(float(data[4]))
    lat.append(float(data[5]))
    pop.append(int(data[6]))

f.close()

print("########EX1########\n")

max_lat = max(lat)
max_lat_ind = lat.index(max_lat)
max_lat_loc = loc[max_lat_ind]

print("northernmost town:", max_lat_loc, "at", max_lat)

print("\n########EX2########\n")

mid_ind = len(loc) // 2
med_lat = sorted(lat)[mid_ind]
med_long = sorted(long)[mid_ind]
print("median latitude:", med_lat)
print("median longitude:", med_long)

print("\n########EX3########\n")

dist_to_center = []

for i in range(len(loc)):
    dist_lat = abs(lat[i] - med_lat)
    dist_long = abs(long[i] - med_long)
    dist_to_center.append(dist_lat + dist_long)

min_dist = min(dist_to_center)
min_dist_ind = dist_to_center.index(min_dist)

print("closest town to center:", loc[min_dist_ind], "at", min_dist, "from center")
print("( latitude:", lat[min_dist_ind], "-- longitude:", long[min_dist_ind], ")")

print("\n########EX4########\n")

pop_1k_4999 = dict()
pop_5k_9999 = dict()
pop_10k_14999 = dict()
pop_15k_20k = dict()

for i, val in enumerate(pop):
    if 1000 <= val < 5000:
        pop_1k_4999[loc[i]] = pop[i]
    if 5000 <= val < 10000:
        pop_5k_9999[loc[i]] = pop[i]
    if 10000 <= val < 15000:
        pop_10k_14999[loc[i]] = pop[i]
    if 15000 <= val <= 20000:
        pop_15k_20k[loc[i]] = pop[i]

dicts = {
    "1k-4999": pop_1k_4999,
    "5k-9999": pop_5k_9999,
    "10k-14999": pop_10k_14999,
    "15k-20k": pop_15k_20k,
}

width = 0.5
curr = 0.25
title = 'Number of communes with pop between 1k and 20k'

for key in dicts:
    plt.bar(curr, len(dicts[key]), width, label=key)
    curr += width

plt.xticks([], [])
plt.legend()
plt.title(title)
# plt.show()

print("\n########EX5########\n")

colors = []
pop_100k_plus = []

for i, val in enumerate(pop):
    if val > 100000:
        colors.append("red")
        pop_100k_plus.append(loc[i])
    else:
        colors.append("blue")

print("communes with pop 100k+:")
for val in pop_100k_plus:
    print(val)

x = range(len(pop))
y = []
for val in pop:
    y.append(val / 100)
plt.scatter(x, y, c=colors)
plt.xlabel('index of commune')
plt.ylabel('population in hundreds')
# plt.show()

print("\n########EX6########\n")


def km_to_rad(km):
    return km * 0.00015961


def rad_to_km(rad):
    return rad * (1 / 0.00015961)


def agglomeration(name):
    name = name.lower()
    loc_idx = loc.index(name)
    here_lat, here_long = lat[loc_idx], long[loc_idx]
    counter = 0
    radius = km_to_rad(20)

    for idx in range(len(loc)):
        if idx != loc_idx:
            dist_lat_here = abs(lat[idx] - here_lat)
            dist_long_here = abs(long[idx] - here_long)
            dist_here = dist_lat_here + dist_long_here
            if dist_here < radius:
                print(loc[idx], "is", rad_to_km(dist_here), "km from", name)
                counter += 1

    return counter


name = "Clermont-Ferrand"
print("####close to", name, ":", agglomeration(name))
