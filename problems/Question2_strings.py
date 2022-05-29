int_number = input("Enter an integer: ")

if int_number.isdigit():
    you_name = input("What is your name? ")
    print(f"Hello, {you_name.upper()}")
else:
    print(int_number.capitalize())
