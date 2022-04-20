
a = "wom"
b = "bat"
c = a + b
print("c: {}".format(c))

a = [1, 2, 3]
b = ['a', 'b', 'c']
c = a + b
print("c: {}".format(c))

print('-' * 60)
x = 'WOMBATS ' * 3
print("x: {}".format(x))

flags = [False] * 10
print("flags: {}".format(flags))

values = [0] * 25
print("values: {}".format(values))

cities = ['Toronto', 'Durham', 'Dallas', 'Los Angeles',
          'New York', 'Phoenix']

for city  in 'Durham', 'Dallas', 'Des Moines', 'Poughkeepsie':
    print(city, city in cities)

if 'Vancouver' not in cities:
    print("Why do you hate BC?")
print()

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

print("cities: {}".format(cities))
print("nums: {}".format(nums))

print(len(cities), min(cities), max(cities), sorted(cities))
print(len(nums), min(nums), max(nums), sorted(nums), sum(nums))
print()
print("cities: {}\n".format(cities))

rev_cities = reversed(cities)
print("rev_cities: {}".format(rev_cities))
print(rev_cities)

for city in rev_cities:
    print(city)
print()

colors = ['purple', 'pink', 'green']
animals = ['snail', 'wombat', 'pine marten']

combo = zip(colors, animals)
print("combo: {}".format(combo))

for item in combo:
    print(item)
print()

combo = zip(colors, animals)
for color, animal in combo:
    print(color, animal)
print()

for city in cities:
    print(city)
print()

for i, city in enumerate(cities):
    print(i, city)
print()

for num in range(1, 11):
    print(num)
print()

#  range(start, stop)  range(stop)  range(start, stop, step)

for _ in range(10):
    print("Python is gr00vy")
print()







