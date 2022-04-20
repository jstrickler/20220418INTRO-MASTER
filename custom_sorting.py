
fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f0 = sorted(fruits)
print("f0: {}\n".format(f0))

#  str.lower()
f1 = sorted(fruits, key=str.lower)
print("f1: {}\n".format(f1))

def ignore_case(fruit):
    compare_version = fruit.lower()
    print(f"comparing {fruit} as {compare_version}")
    return compare_version

f2 = sorted(fruits, key=ignore_case)
print("f2: {}\n".format(f2))

f3 = sorted(fruits, key=len)
print("f3: {}\n".format(f3))

def custom_sort(f):
    return len(f), f.lower()

f4 = sorted(fruits, key=custom_sort)   #custom_sort is a callback
print("f4: {}\n".format(f4))

f5 = sorted(fruits, key=custom_sort, reverse=True)
print("f5: {}\n".format(f5))

def wacky_sort(x):
    return x[2].lower()

f6 = sorted(fruits, key=wacky_sort)
print("f6: {}\n".format(f6))

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1964-08-15'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1964-08-15'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1954-09-27'),
]

for person in sorted(people):
    print(person)
print('-' * 60)

def by_dob(p):
    print(f"sorting {p} as {p[3]}")
    return p[3], p[1], p[0]

for person in sorted(people, key=by_dob):
    print(person)
print('-' * 60)

# lambda param, ...: return-value
for person in sorted(people, key=lambda p: (p[3], p[1], p[0])):
    print(person)
print('-' * 60)

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}
print(airports.items(), '\n')

for code, name in sorted(airports.items()):
    print(code, name)
print('-' * 60)

def by_value(element):
    return element[1], element[0]  # sort by value, then key

for code, name in sorted(airports.items(), key=by_value):
    print(code, name)
print('-' * 60)

fruits.sort(key=ignore_case)
print("fruits: {}\n".format(fruits))

fruits.sort()
print("fruits: {}\n".format(fruits))

fruits.sort(reverse=True)
print("fruits: {}\n".format(fruits))




