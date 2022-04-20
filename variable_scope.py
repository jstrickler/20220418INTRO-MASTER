
x = 100  # global name (variable) ("file global")


def spam():
    y = "pastafazool"  # local name
    print("in spam() x is ", x)
    return y


x = spam()
print("in main: x is", x)

if x:
    pass

def foo():
    pass

for x in range(10):
    pass
