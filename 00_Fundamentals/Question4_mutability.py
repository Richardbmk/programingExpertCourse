
def replace(lst, target, swap_value):
    for idx in range(len(lst)):
        element = lst[idx]

        if element == target:
            lst[idx] = swap_value
    
    return lst



lst = ["Richard", "is", "great", "is", "is", "yes", "no", "blue", "no" ]

print(replace(lst, "is", "the"))