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


def closest_30_in_county(name):
    name = name.lower()
    loc_idx = loc.index(name)
    county = insee[loc_idx][:2]
    here_lat, here_long = lat[loc_idx], long[loc_idx]
    locs_dist_in_county = []
    for idx in range(len(loc)):
        if insee[idx][:2] == county and idx != loc_idx:
            dist_here = abs(lat[idx] - here_lat) + abs(long[idx] - here_long)
            locs_dist_in_county.append((loc[idx], rad_to_km(dist_here)))

    return sorted(locs_dist_in_county, key=compo2)[:30]


name = "Versailles"
close_ones = closest_30_in_county(name)
print("####close to", name, "in same county:", close_ones)
