# Sample Code 00
# Welcome to our Python playground!


# I bet you couldn't store all of those in a list! There are an
# infinite number of even numbers but generators solve this problem
# easily!
def all_even_numbers():
    i = 0
    while True:
        if i % 2 == 0:
            yield i
        i += 1


# count = 0
# for even_number in all_even_numbers():
#     print("Even number:", even_number)
#     count += 1

#     # Let's just print 10 even numbers, but this could run forever
#     # if we wanted to let it!
#     if count >= 10:
#         break

# Sample Code 01
def gen():
    yield 1
    yield 2
    yield 3

# print(type(gen()))
# print(gen())

itr = gen()
# print(next(itr))
# print(next(itr))
# print(next(itr))

# for i in itr:
#     print(i)

# Sample code 02
def fib(n):
    pass

fib_numbers = [1, 1]

for i in range(2, 10):
    last = fib_numbers[i - 1]
    second_last = fib_numbers[i - 2]
    num = last + second_last
    fib_numbers.append(num)

# print(fib_numbers)

# Sample Code 03
def fib(n):
    last = 1
    second_last = 1
    current = 3

    while current <= n:
        num = last + second_last
        yield num

        second_last = last
        last = num
        current += 1

# for val in fib(10):
#     print(val)

# Sample code 04
def a(lst, power):
    for element in lst:
        if element % 2 == 0:
            yield element ** power

gen = a([1,2,3,4,5,6,7,8], 2)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
