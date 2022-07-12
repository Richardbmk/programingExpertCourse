# Sample code 00
# Welcome to our Python playground!

lst = [i for i in range(10)]

plus_two = map(lambda x: x + 2, lst)

evens = filter(lambda x: x % 2 == 0, lst)
odds = filter(lambda x: x % 2 == 1, lst)

print("Original List:", lst)
print("Plus 2:", list(plus_two))
print("Evens:", list(evens))
print("Odds:", list(odds))


# Sample code 02

import math

lst = [[1,2,3], [4,5,6], [1,2,3], [3,4]]

new_lst = filter(lambda y: y % 2 == 0,map(lambda x: sum(x), lst))
print(list(new_lst))

# Sample code 03
lst = [[2,3,4], [4,5,6], [1,1,1], [0,0], [-5,-7]]
x = filter(lambda a: abs(sum(a)) > 10, lst)
print(list(x))


# Sample code 04
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = map(lambda b: b**2, filter(lambda a: a%2 == 0, lst))
for i in y:
    print(i)
# print(list(x))
# print(list(y))