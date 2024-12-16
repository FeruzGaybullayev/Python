"""
Write a Python program to check if a given string is palindrome or not.
What is a Palindrome String? A string is called a palindrome if the reverse of the string is the same as the original one. Example: “madam”, “racecar”, “12321”.
"""

string = input("Enter a string : ")
string_2 = string[::-1]

if string == string_2 :
    print("Palindrome")
else:
    print("Not Palindrome")

