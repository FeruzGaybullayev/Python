# Write a program that checks if a string starts with one word and ends with another.
# Example:

# Input: "Python is fun!" # type: ignore
# Starts with: "Python" # type: ignore
# Ends with: "fun!" # type: ignore
    
# Program to check if a string starts with one word and ends with another.

a = input("Enter a string: ")
b = a.split
c = b[1]
d = b[-1]

if c == d :
    print("Starts with one word and ends with another: Equal")
else:
    print("Starts with one word and ends with another: Not equal")