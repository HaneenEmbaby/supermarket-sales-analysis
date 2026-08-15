cities = []
with open("egypt.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        city = data[0]
        description = data[1]
        if len(data) > 2:
            population = int(data[2].strip())
        else:
            population = None
        cities.append((city, description, population))

print("cities: ")
for city, description, population in cities:
    print("City:", city)
    print("Description:", description)
    print("Population:", population)
    print()

popul_desc = [c for c in cities if c[2] is not None]
popul_desc.sort(key=lambda x: x[2], reverse=True)  #sort mn heth el population desc

print("city by population:")
for city, description, population in popul_desc:
    print(city, "-", population)

most_popul = popul_desc[0]

print("city with the most population:")
print(most_popul[0], "-", most_popul[2])

least_popul = popul_desc[-1]

print("city with the least population: ")
print(least_popul[0], "-", least_popul[2])