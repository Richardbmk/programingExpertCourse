w = 2  # <- Change this
x = 2  # <- Change this
y = -3  # <- Change this
z = -1  # <- Change this

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




first_slice = lst[::z]  # 1) [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
second_slice = first_slice[:y]  # 2) [10, 9, 8, 7, 6, 5, 4]
third_slice = second_slice[x:] # 3) [8, 7, 6, 5, 4]
last_slice = third_slice[::w] # 4) [8, 6, 4]

# print(last_slice)
print(last_slice)
# [8, 6, 4]