def trim_list(lst, element_to_trim):
    if element_to_trim == 0:
        return lst
    else:
        return lst[:-element_to_trim]


""" TIM SOLUTIONS """

def trim_list(lst, element_to_trim):
    trimmed_list = []

    for idx in range(len(lst) - element_to_trim):
        element = lst[idx]
        trimmed_list.append(element)
    
    return trim_list