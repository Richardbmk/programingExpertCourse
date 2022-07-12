# Welcome to our Python playground!

def outer(x, y):
    def nested():
        return x + y

    return nested

value = outer(1, 2)()
print(value)


def foo(x):
    print(x)

def call_func(func, x):
    func(x)

# print(call_func(foo, 7))

def outer(x):
    def inner(y):
        print(x + y)

    return inner

func = outer(7)
# print(func)
# func(5)
# func(12)
# func2 = outer(1)
# func2(1)

def outer(x):
    def inner(y):
        def inner2(z):
            print(x + y + z)

        return inner2

    return inner

# outer(5)(5)(5)

def outer(x):
    # this is a closure function
    def inner():
        print(x)

    return inner

func = outer(5)
# func()

def collection():

    lst = []

    def inner(value):
        lst.append(value)
        return lst

    return inner

add_value = collection()
# print(add_value(1))
# print(add_value(2))
# print(add_value(3))
# print(add_value(4))
# print(add_value(5))

# Class Sample
class Collection:
    def __init__(self):
        self.lst = []

    def add_value(self, value):
        self.lst.append(value)
        return self.lst


def counter(start):
    count = start

    def increment(value):
        nonlocal count
        count += value
        return count

    return increment

count = counter(2)
# print(count(1))
# print(count(1))
# print(count(1))
# print(count(1))

# Class Sample
class Counter:
    def __init__(self, start):
        self.count = start

    def count(self, value):
        self.count += value
        return self.count


def outer():
    def inner():
        def inner2():
            nonlocal x
            x = 2
            print("Inner2:", x)

        x = 3
        inner2()
        print("Inner:", x)

    x = 4
    inner()
    print("Outer:", x)

outer()


