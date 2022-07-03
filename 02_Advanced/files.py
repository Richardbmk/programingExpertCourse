# Welcome to our Python playground!

with open("02_Advanced/awesome_people.txt", "w") as file:
    file.write("Tim\n")
    file.write("Antoine\n")
    file.write("Clement")

file = open("02_Advanced/awesome_people.txt", "r")
awesome_people = file.read().split("\n")
file.close()

# print(awesome_people)

# Sample code 01

with open("02_Advanced/sample.txt", "r") as file:
    # num_words = file.read().strip()
    num_words01 = file.read().replace(".", "")
    num_words02 = num_words01.replace(",", "")
    num_words03 = num_words02.replace("-", " ")
    num_words04 = num_words03.split()
    print(len(num_words04))


# Sample code 02

with open("02_Advanced/sample.txt", "r+") as file:
    score = file.read()
    new_score = int(score) + 1
    file.seek(0)
    file.write(str(new_score))


# Sample code 03
with open("02_Advanced/sample.txt", "r+") as file:
    count = 0
    for line in file:
        print(line, end="")
        count += 1
        if count >= 3:
            break

with open("02_Advanced/sample.txt", "r+") as file:
    for i, line in enumerate(file):
        print(line, end="")
        if i == 2:
            break


# Sample code 04
# Write your code here.
with open("programmingExpert.txt", "w") as file:
    for i in range(1, 51):
        file.write(str(i**2) + "\n")


