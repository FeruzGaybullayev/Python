# Write a program that asks the user for a string and a character, then removes all occurrences of that character from the string.

user_string = input("Enter a string: ")

char_to_remove = input("Enter the character to remove: ")

result = user_string.replace(char_to_remove, "")

print("String after removal:", result)
