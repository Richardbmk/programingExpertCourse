lst = [[2, 3, 4], [-2, -4, 0], [1, 2], [1, 1, 1, 5, 6], [0, 9, 8, 7]]

"""My solution1"""
# Write your code here.
for idx,elem in enumerate(lst):
    print(sum(elem))


"""My solution2"""
# Write your code here.
for i in lst: 
    addition = 0
    for j in i:
        addition += j
        
    print(addition)

"""TIM SOLUTION"""
lst = [[2, 3, 4], [-2, -4, 0], [1, 2], [1, 1, 1, 5, 6], [0, 9, 8, 7]]

for inner_list in lst:
    sum_of_inner_list = 0

    for item in inner_list:
        sum_of_inner_list += item

    print(sum_of_inner_list)


## Some sample code

# Sample code 1
lst = [[1,2],[3,4],[5,6],[7,8]]

for i in range(len(lst)):
    interior_lst = lst[i]

    for j in range(len(interior_lst)):
        print(interior_lst[j])

# Sample code 2
numbers = []

for i in range(3):
    num = input("Enter a number: ")
    numbers.append(int(num))

print(numbers)

# Sample code 3
words = ("hello", "name", "this", "is", "word")
target = "nae"

for word in words:
    if word == target:
        print(f"I find the word!: {target}")
        break
else:
    print("I didn't find the word")
