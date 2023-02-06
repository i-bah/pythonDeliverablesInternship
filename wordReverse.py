# Prompt the user to enter a phrase or sentence
user_data = input("Enter a phrase or sentence: ")

# Initialize the starting point of each word
word_start = 0

# Store each word in a list
words = []

# Loop through each character in the user data
for i, char in enumerate(user_data):
    # If a space is encountered, store the word
    if char == ' ':
        words.append(user_data[word_start:i])
        word_start = i + 1

# Add the last word to the list
words.append(user_data[word_start:])

# Initialize a list to store the reversed words
rev_words = []

# Loop through each word in the list
for word in words:
    # Initialize a variable to store the reversed word
    rev_word = ''

    # Loop through each letter in the word in reverse order
    for letter in range(len(word) - 1, -1, -1):
        rev_word += word[letter]

    # Add the reversed word to the list of reversed words
    rev_words.append(rev_word)

# Concatenate the reversed words into a single string
concatenated = rev_words[0]
for rev_word in rev_words[1:]:
    concatenated += ' ' + rev_word

# Print the concatenated string
print(concatenated)
