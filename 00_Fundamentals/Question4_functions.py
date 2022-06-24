def compare_lists(lst1=[], lst2=[]):
    common_elements = set(lst1) & set(lst2)
    return len(list(common_elements))


"""TIM SOLUTION"""

def compare_lists(lst1=[], lst2=[]):
    lst1_set = set(lst1)
    lst2_set = set(lst2)
    set_intersection = lst1_set.intersection(lst2_set)

    return len(set_intersection)