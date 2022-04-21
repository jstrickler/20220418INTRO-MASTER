import sys

print("sys.argv: {}\n".format(sys.argv))

print("sys.platform: {}\n".format(sys.platform))

# win32 -> Windows (any version)
# linux -> Linux
# darwin -> MacOS
import re
from johnapp.math import geometry

print("sys.modules['re']: {}\n".format(sys.modules['re']))

print("sys.modules['sys']: {}\n".format(sys.modules['sys']))

print("sys.modules['johnapp.math.geometry']: {}\n".format(sys.modules['johnapp.math.geometry']))


print("sys.version: {}\n".format(sys.version))

print("sys.version_info: {}\n".format(sys.version_info))

print("sys.version_info.major: {}\n".format(sys.version_info.major))

print("sys.executable: {}\n".format(sys.executable))

print("sys.prefix: {}\n".format(sys.prefix))

print("sys.maxsize: {:,d}\n".format(sys.maxsize))

for attr_name in sorted(dir(sys)):
    print(attr_name)
print()

print("sys.getrecursionlimit(): {}\n".format(sys.getrecursionlimit()))

x = list(range(10000))
print(len(x))

print("sys.getsizeof(x): {}\n".format(sys.getsizeof(x)))

# sys.stdin  sys.stdout  sys.stderr

sys.stdout.write("hello\n")

print("Invalid entry", file=sys.stderr)

