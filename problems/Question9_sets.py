characters = set()

while True:
    char = input("Enter a character: ")

    if char in characters or len(char) > 1:
        unique_chars = len(characters)
        print(f"Number of unique characters entered: {unique_chars}")
        break

    characters.add(char)