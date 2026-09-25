# Exercise 1: Split a sentence into words

sentence = "Python is useful for scientific data analysis."

words = sentence.split(maxsplit=3)

print(words)


# Exercise 2: Find a character within a specific range

word = "Meerschweinchen"

position = word.find("e", 1, 5)

print(f"The character was found at index: {position}")