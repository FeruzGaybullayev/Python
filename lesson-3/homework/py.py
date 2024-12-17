list_of_elements = input("Enter a list (elements separated by space): ").split()
n = input("Elementni kiriting: ")

# Element qanchalik ko'p marta uchrayotganini hisoblash
count = list_of_elements.count(n)

print(f"{n} ro'yxatda {count} marta uchraydi.")