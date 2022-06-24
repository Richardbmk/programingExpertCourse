numbers = [1, 3, 6, 10, 15, 21]
i = 0

while i < len(numbers):
    number_squared = numbers[i]**2
    i += 1
    print(number_squared)

## Code Samples

# Sample 1

num = input("Enter an integer: ")

while not num.isdigit():
    num = input("Enter an integer: ")

# Sample 2

while True:
    num = input("Enter an integer: ")
    if num.isdigit():
        break

# Sample 3

lst = [2, 3, 3, -2, -2, -1]

result = 0
i = 0

while result < 9 and i < len(lst):
    num = lst[i]
    result += num
    i += 1

    print(num)

# Sample 4

lst = [2, 3, 3, -2, -2, -1]
i = 0

while i < len(lst):
    if lst[i] == -2:
        print("found it")
        break
    i += 1
else:
    print("didn't find it")

