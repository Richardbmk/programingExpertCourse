def sort_second_index(item):
    return item[1]

lst = [[-1, -2], [3, 4], [5, -6], [-1, -2], [0, 0]]

lst.sort(reverse=True, key=sort_second_index)

# print(lst)

people = {"Tim": 21, "Joe": 18, "Sarah": 25, "Jennie": 26, "Bill": 34}

result = sorted(people, key=people.get)
print(result)