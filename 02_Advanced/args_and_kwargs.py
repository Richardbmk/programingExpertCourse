# Sample code 00
# Welcome to our Python playground!


def pretty_print(*args, **kwargs):
    print("*" * 15)
    print(*args, **kwargs)
    print("*" * 15)


pretty_print(*["H", "e", "l", "l", "o", "world"], end="!\n")

# Sample Code 01
def sum_items(*args):
    print(sum(args))

sum_items(1,2,3,4,5)

def sum_items(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs['a'])

sum_items(1,2,3,4,5, k=2, a=3)

def sum_items(a, b, c):
    return a + b + c

args = [4, 5, 7]
args = "457"
a = sum_items(*args)
print(a)

def sum_items(a, b, c):
    print(a, b, c)
    return a + b + c

kwargs = {"a": 5, "c": 10, "b": 5}
x = sum_items(**kwargs)
print(x)

def sample(*args):
    print(args)

sample(*"hello")