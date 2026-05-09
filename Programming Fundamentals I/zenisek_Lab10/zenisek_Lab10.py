# Imported employee.py
from employee import Employee

# Defined the main function:
def main():

# Employees list:
    employees = []

# Loop to create 3 employees
    for i in range(3):

        print(f"\nEnter information for employee {i + 1}")

        name = input("Enter employee name: ")
        id_number = input("Enter employee ID: ")
        department = input("Enter department: ")
        job_title = input("Enter position: ")

# Created the object
        emp = Employee(name, id_number, department, job_title)

        # Add object to list
        employees.append(emp)

# Display employee information:
    print("\nEmployee Information")
    print("---------------------")

# The loop that gets more employees:
    for i in range(3):
        print(f"\nEmployee {i + 1}:")
        print(employees[i])

# Calls the main function:
if __name__ == "__main__":
    main()