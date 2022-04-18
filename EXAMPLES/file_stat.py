#!/usr/bin/env python
import os

info = os.stat('../DATA/parrot.txt')  # <1>
print(info)  # <2>

print('size is', info[6])  # <3>
print('size is', info.st_size)  # <4>
