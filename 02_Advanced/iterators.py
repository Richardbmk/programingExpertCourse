# Sample Code 00
# Welcome to our Python playground!


# This DividerIterator class is an iterator that will start
# at a number `start` and divide that number by `factor`
# over and over again until it is smaller than or equal
# to `end`.
class DividerIterator:
    def __init__(self, start, factor, end):
        self.start = start
        self.factor = factor
        self.end = end

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < self.end:
            raise StopIteration
        current = self.current
        self.current = current / self.factor
        return current


# Let's keep dividing 100 by 7 over and over again
# until 0.01.
# count = 0
# for n in DividerIterator(100, 7, 0.01):
#     print(f"Divided {count} times: {n}")
#     count += 1


# Sample Code 01
x = [1,2,3]

x_iter = iter(x)
# print(x_iter)
# print(next(x_iter))
# print(next(x_iter))
# print(next(x_iter))

# Sample Code 02
x = [1,2,3]

# x_iter = iter(x)
x_iter = x.__iter__()

# while True:
#     try:
#         # print(next(x_iter))
#         print(x_iter.__next__())
#     except StopIteration:
#         break

# Sample Code 03
class Numbers:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def __iter__(self):
        return NumberIterator(self.num1, self.num2, self.num3)

class NumberIterator:
    def __init__(self, one, two, three):
        self.one = one
        self.two = two
        self.three = three
        self.current = 0

    def __next__(self):
        self.current += 1
        if self.current == 1:
            return self.one
        elif self.current == 2:
            return self.two
        elif self.current == 3:
            return self.three
        else:
            raise StopIteration

nums = Numbers(1,2,3)

# itr = iter(nums)
# print(itr)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

# for num in nums:
#     print(num)

# Sample Code 04
class Numbers:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.current = 0

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        self.current += 1

        if self.current == 1:
            return self.num1
        elif self.current == 2:
            return self.num2
        elif self.current == 3:
            return self.num3
        else:
            raise StopIteration

nums = Numbers(1,2,3)

for val in nums:
    print(val)