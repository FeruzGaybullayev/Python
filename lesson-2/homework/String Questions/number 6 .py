# Write a Python program to check if one string contains another.

main_string = input("Enter a main string : ")
sub_string = input("Enter a substring : ")
if sub_string in main_string:
    print(f'"{sub_string}" "{main_string}" ichida mavjud.')
else:
    print(f'"{sub_string}" "{main_string}" ichida mavjud emas.')