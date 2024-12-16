# Write a program that accepts a username and password and checks if both are not empty.


username = input("Enter username: ")
password = input("Enter password: ")

if username and password:
    print("Username and password are valid.")
else:
    print("Error: Username and password cannot be empty.")
