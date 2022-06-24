def find_all_odds(lst):
    odd_lst = []
    for element in lst:
        if element%2 != 0:
            odd_lst.append(element)
    
    return odd_lst


print(find_all_odds([1,2,3,4,5,6,5,5,3,2]))