"""My Solution"""

number = int(input("Enter a number: "))
count = 1

while number != 5:
    number = int(input("Enter a number: "))
    count += 1
    if number == 5:
        print(f"You entered {count} numbers.")

"""TIM SOLUTION"""
number_of_entries = 0

while True:
    number = int(input("Enter a number: "))
    number_of_entries += 1

    if number == 5:
        break

print(f"You entered {number_of_entries} numbers")
