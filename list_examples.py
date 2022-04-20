list1 = list()  # empty list
list2 = ['red', 'orange', 'pink', 'magenta']
list3 = [5, 8, 1, 19]
list4 = [3, "wombat", 8.9, None, 0]

cities = ['Toronto', 'Durham', 'Dallas', 'Los Angeles',
          'New York', 'Phoenix']

print(cities[0], cities[4])
cities.insert(0, 'Hong Kong')
print("cities: {}".format(cities))
cities.insert(6, "Dubai")
print("cities: {}".format(cities))
cities.append('Ottawa')
cities.append('Worcestershire')
print("cities: {}".format(cities))
print("len(cities): {}".format(len(cities)))
# cities[len(cities) - 1]
print("cities[-1]: {}".format(cities[-1]))
more_cities = ['Arlington', 'Ballston', 'Fairfax']
cities.extend(more_cities)
print("cities: {}".format(cities))

#  LIST.insert(pos, obj)
#  LIST.append(obj)
#  LIST.extend(iterable)

cities.insert(99, "Tampa")
print("cities: {}".format(cities))

cities.insert(-3, 'Portland')
print("cities: {}".format(cities))

food = ['spam', 'spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'spam', 'eggs', 'spam']

print(food.count('spam'), food.count('eggs'),
      food.count('ham'))

del cities[2]   # NOT del(cities[2]  NOT cities.delete(2)
print("cities: {}".format(cities))

city = cities.pop()
print("city: {}".format(city))
print("cities: {}".format(cities))

city = cities.pop(5)
print("city: {}".format(city))
print("cities: {}".format(cities))

cities.remove('Worcestershire')
print("cities: {}".format(cities))

# del LIST[pos]
# LIST.remove(value)
# element = LIST.pop()
# element = LIST.pop(pos)

cities.sort()
print("cities: {}".format(cities))

print(cities[5], cities[1], cities[0], cities[-3])

print(cities[:3])  # slice of a sequence
print(cities[0:3])  #  elements 0-2
#  [start:stop]  [:stop]  [start:]  [:]
print(cities[3:6])
print(cities[6:])
print(cities[-5:])
pos = cities.index('New York')
print("pos: {}".format(pos))
print(cities[pos:])

actor = "Chris Hemsworth"

print(actor[:5])
print(actor[-5:])
print(actor[3:5])
print(actor[0], actor[5], actor[-1])

print("cities: {}".format(cities))
cities[1] = "Falls Church"
print("cities: {}".format(cities))
print()

# for VAR in ITERABLE:
#    ???
for city in cities:
    # city = cities[0]
    # city = cities[1]
    # ...
    print(city.upper())
print()

for city in cities[:5]:
    print(city)
print()















