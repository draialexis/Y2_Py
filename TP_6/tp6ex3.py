insee = []
loc = []
long = []
lat = []

f = open("villes.csv", encoding="utf8")

next(f)
for line in f:
    data = line.split(';')
    insee.append(data[0])
    loc.append(data[1].lower())
    long.append(float(data[4]))
    lat.append(float(data[5]))

f.close()

print("########EX1########\n")


def km_to_rad(km):
    return km * 0.00015961


def rad_to_km(rad):
    return rad * (1 / 0.00015961)


def compo2(couple):
    return couple[1]


def closest_in_county(name):
    name = name.lower()
    loc_idx = loc.index(name)
    county = insee[loc_idx][:2]
    here_lat, here_long = lat[loc_idx], long[loc_idx]
    locs_dist_in_county = []
    for idx in range(len(loc)):
        if insee[idx][:2] == county and idx != loc_idx:
            dist_here = abs(lat[idx] - here_lat) + abs(long[idx] - here_long)
            locs_dist_in_county.append((loc[idx], rad_to_km(dist_here)))

    return sorted(locs_dist_in_county, key=compo2)


name = "Lille"
close_ones = closest_in_county(name)
print("close to", name, "in same county (name, dist):", close_ones[:30])

print("\n########EX2########\n")

print("furthest from", name, "in same county:", close_ones[-1][0])

print("\n########EX3########\n")

dist = close_ones[-1][1]
print("dist:", dist, "km")

print("\n########EX4########\n")

radius = dist / 2


def in_radius(name, radius):
    name = name.lower()
    loc_idx = loc.index(name)
    here_lat, here_long = lat[loc_idx], long[loc_idx]
    county = insee[loc_idx][:2]
    counter = 0
    radius = km_to_rad(radius)
    locs_in_county = [loc[loc_idx]]

    for idx in range(len(loc)):
        if insee[idx][:2] == county and idx != loc_idx:
            locs_in_county.append(loc[idx])
            dist_lat_here = abs(lat[idx] - here_lat)
            dist_long_here = abs(long[idx] - here_long)
            dist_here = dist_lat_here + dist_long_here
            if dist_here < radius:
                # print(loc[idx], "is", rad_to_km(dist_here), "km from", name)
                counter += 1

    return counter, (counter * 100 / len(locs_in_county))


number, ratio = in_radius(name, radius)
print(number, "communes", radius, "km from", name, ";", ratio, "%")
