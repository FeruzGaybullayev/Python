# Xodimlar haqidagi ma'lumotlarni boshqarish uchun dastur tuzish:

def main():
    while True:
        print("\nMenu:")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        choice = input("Select an option (1-6): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

def add_employee():
    with open("employees.txt", "a") as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        record = f"{emp_id}, {name}, {position}, {salary}\n"
        file.write(record)
        print("Employee record added.")

def view_employees():
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
            if records:
                print("\nAll Employee Records:")
                for record in records:
                    print(record.strip())
            else:
                print("No employee records found.")
    except FileNotFoundError:
        print("No employee records found.")

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
            for record in records:
                if record.startswith(emp_id):
                    print("Employee Record:", record.strip())
                    found = True
                    break
            if not found:
                print("Employee not found.")
    except FileNotFoundError:
        print("No employee records found.")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    found = False

    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()

        with open("employees.txt", "w") as file:
            for record in records:
                if record.startswith(emp_id):
                    print("Current Record:", record.strip())
                    name = input("Enter new Name (leave blank to keep current): ")
                    position = input("Enter new Position (leave blank to keep current): ")
                    salary = input("Enter new Salary (leave blank to keep current): ")
                    
                    if not name: name = record.split(", ")[1]
                    if not position: position = record.split(", ")[2]
                    if not salary: salary = record.split(", ")[3].strip()
                    
                    record = f"{emp_id}, {name}, {position}, {salary}\n"
                    found = True
                file.write(record)
            if found:
                print("Employee record updated.")
            else:
                print("Employee not found.")
    except FileNotFoundError:
        print("No employee records found.")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    found = False
    
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()

        with open("employees.txt", "w") as file:
            for record in records:
                if not record.startswith(emp_id):
                    file.write(record)
                else:
                    found = True
            if found:
                print("Employee record deleted.")
            else:
                print("Employee not found.")
    except FileNotFoundError:
        print("No employee records found.")

# Dastur boshqaruvini boshlash
if __name__ == "__main__":
    main()
