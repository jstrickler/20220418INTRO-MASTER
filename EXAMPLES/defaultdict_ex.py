#!/usr/bin/env python
from collections import defaultdict

def get_zero():
    return "wombat"

dd = defaultdict(get_zero)  # callback function

dd['spam'] = 10  # <2>
dd['eggs'] = 22

print(dd['spam'])  # <3>
print(dd['eggs'])
print(dd['foo'])  # <4>
print(dd['bar'])

print('-' * 60)

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

fruit_info = defaultdict(list)

for fruit in fruits:
    first_letter = fruit[0]
    if first_letter not in fruit_info:
        fruit_info[first_letter] = list()
    fruit_info[first_letter].append(fruit)

for letter, fruits in sorted(fruit_info.items()):
    print(letter, fruits)

