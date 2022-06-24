lst = [45, 24, 22, 1, 45, 2, 12, 13, 16, 10, 0, -7]

"""My Solution"""
# Write your code here. 
for idx,elem in enumerate(lst):
    if (elem % 2 == 0) and (idx % 2 != 0) :
        print(elem)


"""TIM SOLUTION"""

for idx in range(len(lst)):
    item = lst[idx]

    if item % 2 == 0 and idx % 2 != 0:
        print(item)