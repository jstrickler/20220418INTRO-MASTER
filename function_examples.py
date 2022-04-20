from math import pi

def hello():
    print("Hello, Python world")

hello()
hello()

def circle_area(diameter):
    if isinstance(diameter, (int, float)):
        radius = diameter / 2
        area = pi * (radius ** 2)
        return area
    else:
        raise TypeError("Argument must be numeric")

def rectangle_area(length, width):
    return length * width


a = circle_area(10)
print(a)
a = circle_area(42.73)
print(a)
print(circle_area(2))
wombat = 7
print(circle_area(wombat))
# print(circle_area("wombat"))

print(rectangle_area(5, 7))

def greet(whom="world"):
    print(f"Hello, {whom}")
    # return None

greet("Mom")
greet("New York")
greet()

#   p1 positional-only
def wacky(p1, /, p2, p3, *p4, p5, p6, **p7):
    print("p1: {}".format(p1))
    print("p2: {}".format(p2))
    print("p3: {}".format(p3))
    print("p4: {}".format(p4))
    print("p5: {}".format(p5))
    print("p6: {}".format(p6))
    print("p7: {}".format(p7))
    print('-' * 60)

wacky(1, 20, 30, 40, 50, p5=10, p6=11, animal="wombat", country="Burkina Faso")


def find_text(file_name, text_to_find, *, ignore_case=False):
    found = []
    if ignore_case:
        text_to_find = text_to_find.lower()
    with open(file_name) as file_in:
        for raw_line in file_in:
            line = raw_line.rstrip()
            if ignore_case:
                search_line = line.lower()
            else:
                search_line = line
            if text_to_find in search_line:
                found.append(line)
    return found

lines = find_text('DATA/alice.txt', 'pig', ignore_case=True)
print(lines)

def void():
    pass


