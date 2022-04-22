#!/usr/bin/env python
import requests

response = requests.get("https://www.python.org")  # <1>

for header, value in sorted(response.headers.items()): # <2>
    print("{:20.20s} {}".format(header, value))
print()

print(response.text[:500])   # <3>
print('...')
print(response.text[-500:])   # <4>
