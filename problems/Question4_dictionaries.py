"""My Solutions"""

string = input("Enter a string: ")
characters = {}

for letter in string:
    characters[letter] = characters.get(letter, 0) + 1

for key,value in characters.items():
    print(f"{key}: {value}")