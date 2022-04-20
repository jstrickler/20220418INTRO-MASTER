#  from pkg.pkg import module
#  load johnapp/math/geometry.py
from johnapp.math import geometry
# find geometry.py and run it

import sys

a = geometry.circle_area(25)
print("a: {}".format(a))

print(geometry.ANIMAL)

geometry.hello()

print(geometry.rectangle_area(25, 15))

d = geometry.Dog()
d.bark()

print(geometry.pi)
print(sys.platform)

# module search order:
# 1. current folder
# 2. folders in PYTHONPATH
# 3. builtin folders (from your Python install)

for path in sys.path:
    print(path)
