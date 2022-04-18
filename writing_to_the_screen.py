person = "Bobby"
city = "Berlin"
value = 39.3829489484

print(person, city, value)
#  output   str(person) + ' ' + str(city) + ' ' + value + '\n'

print("OK")
print("A")
print("B")
print("C")

print("A", end="")
print("B", end=' ')
print("C")
print()

print(person, city, value, sep=";")
print(person, city, value, sep="/")
print(person, city, value, sep="##")
print(person, city, value, sep="")


print(person, city, value)
print()

print(person, "lives in", city)

# 3.6 and later
print(f"{person} lives in {city}")

# pre 3.6
print("{} lives in {}".format(person, city))

print(f"2 + 2 = {2 + 2}")

print(f"{value}")
print(f"{value:.3f}")

huge_number = 23238975289332
print(f"{huge_number:,d}")













