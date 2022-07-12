# Sample code 00

lst = [
    ('cake', '30'),
    ('orange', '3'),
    ('pasta', '20'),
]

lst.sort(key=lambda x:x[1])

print(lst)

# Sample code 01
# Welcome to our Python playground!

add_one = lambda x: x + 1

print(add_one(1))
print(add_one(41))

hyphenise = lambda s: s.lower().replace(" ", "-")
print(hyphenise("Hello World"))

# Sample code 02

func = lambda x,y,z=0: print(x+y+z)
func(1,2,4)

# Sample code 03
def sort_func(x):
    return x[0]

lst = [(1,2), (-2,-4), (3,4), (0,0)]
lst.sort(key=sort_func)
print(lst)

lst0 = [(1,2), (-2,-4), (3,4), (0,0), (9,8), (5,5)]
lst0.sort(key=lambda x:x[0])
print(lst0)

mul = lambda x: lambda y: x * y

result = mul(2)
print(result(3))

def mul(x):
    def mul2(y):
        return x * y

    return mul2

result = mul(5)
print(result(2))

result = mul(5)(2)
print(result)
