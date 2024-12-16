# Write a program to check if a string contains any digits.

user_input = input("Enter a text: ")
digits = "0123456789"

found_digit = False
for digit in digits:
    if digit in user_input:
        found_digit = True
        break

if found_digit:
    print("Digits have in the text")
else:
    print("Digits don't have in the text")