def string_lengths(strings):
    string_length = []
    for element in strings:
        element_length = len(element)
        string_length.append(element_length)

    return string_length

strings = ["hello", "this", "is", "a", "beard", "orange", "blue"]
string_lengths_list = string_lengths(strings)

print(string_lengths_list)