""" My Solution 0 """
"""
Python check if the variable is an integer
"""
# https://pythonguides.com/python-check-if-the-variable-is-an-integer/#:~:text=is%20an%20integer-,To%20check%20if%20the%20variable%20is%20an%20integer%20in%20Python,of%20type%20integer%20or%20not.&text=After%20writing%20the%20above%20code,appear%20as%20a%20%E2%80%9C%20True%20%E2%80%9D.


# string = input("Enter a string: ")

# print(string)

x = 0
y = 0
x_list = []
y_list = []
result = []

while x < 5:
    string = input("Enter a string: ")
    x_list.append(string)
    x +=1


while y < 3:
    number = int(input("Enter a number: "))
    result.append(x_list[number])
    y +=1


result = "".join(result)

# print(x_list)
print(result)

"""TIM solution, number 1"""

string1 = input("Enter a string: ")
string2 = input("Enter a string: ")
string3 = input("Enter a string: ")
string4 = input("Enter a string: ")
string5 = input("Enter a string: ")

strings = [string1, string2, string3, string4, string5]

num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
num3 = input("Enter a number: ")

final_string = strings[num1] + strings[num2] + strings[num3]
print(final_string)


"""TIM solution, number 2"""
"""TIM solution, number 3"""