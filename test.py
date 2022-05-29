# Welcome to our Python playground!

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

try:
    if len(digits) != 10:
        raise Exception("There should be exactly 10 digits!")
except Exception as e:
    print(e)
finally:
    print("Goodbye!")