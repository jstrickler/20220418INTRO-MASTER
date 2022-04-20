#!/usr/bin/env python

"""Basic sorting example"""

fruits = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon", "Kiwi",
         "ORANGE", "lime", "Watermelon", "guava", "papaya", "FIG", "pear", "banana",
         "Tamarind", "persimmon", "elderberry", "peach", "BLUEberry", "lychee",
         "grape"]

sorted_fruit = sorted(fruits)  # <1>

print(sorted_fruit)

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

sorted_nums = sorted(nums, reverse=True)
print("sorted_nums: {}".format(sorted_nums))
