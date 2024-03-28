import json
import os

employee_records = {}

data_file = 'info.json'


def load_data():
    global employee_records
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            employee_records = json.load(file)


def save_data():
    with open(data_file, 'w') as file:
        json.dump(employee_records, file, indent=4)


def add_employee():
    print('Enter employee details:')
    emp_id = input('Employee ID: ')
    name = input('Name: ')
    department = input('Department: ')
    position = input('Position: ')
    salary = input('Salary: ')

    employee_records[emp_id] = {
        'name': name,
        'department': department,
        'position': position,
        'salary': salary
    }
    print('Employee added successfully!')
    save_data()


def update_employee():
    emp_id = input('Enter Employee ID to update: ')
    if emp_id in employee_records:
        print('Enter new details:')
        name = input('Name: ')
        department = input('Department: ')
        position = input('Position: ')
        salary = input('Salary: ')

        employee_records[emp_id] = {
            'name': name,
            'department': department,
            'position': position,
            'salary': salary
        }
        print('Employee details updated successfully!')
        save_data()
    else:
        print('Employee not found!')


def delete_employee():
    emp_id = input('Enter Employee ID to delete: ')
    if emp_id in employee_records:
        del employee_records[emp_id]
        print('Employee deleted successfully!')
        save_data()
    else:
        print('Employee not found!')


def search_employee():
    search_key = input('Enter search key (name/department/position): ').lower()
    search_value = input('Enter search value: ').lower()

    found = False
    for emp_id, emp_details in employee_records.items():
        if search_value in emp_details[search_key].lower():
            print(f"\nEmployee ID: {emp_id}")
            print(f"Name: {emp_details['name']}")
            print(f"Department: {emp_details['department']}")
            print(f"Position: {emp_details['position']}")
            print(f"Salary: {emp_details['salary']}")
            found = True

    if not found:
        print('No matching employee found.')


def list_employees():
    sorted_records = sorted(employee_records.items(), key=lambda x: x[1]['name'].split()[-1])
    for emp_id, emp_details in sorted_records:
        print(f"Employee ID: {emp_id}")
        print(f"Name: {emp_details['name']}")
        print(f"Department: {emp_details['department']}")
        print(f"Position: {emp_details['position']}")
        print(f"Salary: {emp_details['salary']}")
        print()


def main():
    load_data()
    try:
        while True:
            print('\nEmployee Management System Menu:')
            print('1. Add Employee')
            print('2. Update Employee')
            print('3. Delete Employee')
            print('4. Search Employee')
            print('5. List Employees')
            print('6. Save Data')
            print('7. Exit')

            choice = input('Enter your choice: ')

            if choice == '1':
                add_employee()
            elif choice == '2':
                update_employee()
            elif choice == '3':
                delete_employee()
            elif choice == '4':
                search_employee()
            elif choice == '5':
                list_employees()
            elif choice == '6':
                save_data()
            elif choice == '7':
                break
            else:
                print('Invalid choice, please enter a number between 1 and 7.')
    except KeyboardInterrupt:
        save_data()
        print('\nData saved.')
    except Exception as e:
        print('An error occurred:', e)
        save_data()
        print('Data saved.')


if __name__ == '__main__':
    main()
