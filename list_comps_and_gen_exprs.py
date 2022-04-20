import re

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []  # empty list
for f in fruits:  # iterate over list
    f0.append(f.upper())  # add upper-case fruit to list
print("f0: {}\n".format(f0))


f1 = [f.upper() for f in fruits]
print("f1: {}\n".format(f1))

f2 = [len(f) for f in fruits]
print("max(f2): {}".format(max(f2)))
print("f2: {}\n".format(f2))

f3 = [f.upper() for f in fruits if f.startswith('p')]
print("f3: {}\n".format(f3))

f4 = [f for f in fruits if f.startswith('p')]
print("f4: {}\n".format(f4))

f5 = [f for f in fruits if re.search('^p[ae]', f)]
print("f5: {}".format(f5))
print("len(f5): {}\n".format(len(f5)))

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

dobs = [p[-1] for p in people]
print("dobs: {}\n".format(dobs))

f0 = [f.upper() for f in fruits]

fruit_gen = (f.upper() for f in fruits)
print("fruit_gen: {}".format(fruit_gen))

for fruit in fruit_gen:
    print(fruit)
print()

