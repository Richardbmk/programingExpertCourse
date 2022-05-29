"""My SOlution"""

list_of_word = []
count_word_letters = 0

while True:
    word = input("Enter a word: ")

    if word != "q" and word != "quit":
        list_of_word.append(word)
        
    if word == "q" or word == "quit":
        break

for word  in list_of_word:
    count_word_letters += len(word)

# print(count_word_letters)


if len(list_of_word) == 0:
    pass
else:
    average = count_word_letters / len(list_of_word)
    print(f"The average word length is: {average}.")



"""TIM SOLUTION"""

word_length_sum = 0
word_count = 0

while True:
    word = input("Enter a word: ")

    if word == "q" or word == "quit":
        break

    word_length_sum += len(word)
    word_count += 1

if word_count > 0:
    average_word_length = word_length_sum / word_count
    print(f"The average word length is: {average_word_length}.")