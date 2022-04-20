from math import pi


ANIMAL = 'wombat'

class Dog:
    def bark(self):
        print("Woof woof")

_JUNK = "rubbish"

def hello():
    print("Hello, Python world")

def circle_area(diameter):
    if isinstance(diameter, (int, float)):
        radius = diameter / 2
        area = pi * (radius ** 2)
        return area
    else:
        raise TypeError("Argument must be numeric")

def rectangle_area(length, width):
    return length * width

if __name__ == '__main__':    # if this file run as script...
    print("HI, MOM!!")

    r = rectangle_area(15, 18)
    print("r: {}".format(r))
