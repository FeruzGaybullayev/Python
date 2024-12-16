# Write a program that asks the user for a sentence and prints the number of words in it.

# Ask the user for a sentence

sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Count the number of words
word_count = len(words)

# Print the number of words
print("The number of words in the sentence is:", word_count)