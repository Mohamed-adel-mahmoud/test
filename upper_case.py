def up_case(word):
    return word.upper()


list_of_word = ["apple", "orange", "watermelon", "banana"]
print(list(map(up_case, list_of_word)))
