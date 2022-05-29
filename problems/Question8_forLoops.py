"""My solution"""

lst = [-2, 0, 4, 5, 1, 2]

# Write your code here.
for i in range(len(lst)):
    if i != len(lst) - 1:
        sum_next2me = lst[i] + lst[i + 1]
        print(sum_next2me)
    

"""TIM Solution"""
for idx in range(len(lst) - 1):
    current_item = lst[idx]
    next_item = lst[idx + 1]

    sum_of_items = current_item + next_item
    print(sum_of_items)