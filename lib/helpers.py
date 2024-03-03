from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    print('\n')
    departments = Department.get_all()
    for department in departments:
        print(department)
    print('\n')


def find_department_by_name():
    print('\n')
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print (f'Department "{name}" not found.')
    print('\n')


def find_department_by_id():
    print('\n')
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department "{id_}" not found.')
    print('\n')


def create_department():
    print('\n')
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)
    print('\n')
    


def update_department():
    print('\n')
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location
            
            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department "{id_}" not found')
    print('\n')


def delete_department():
    print('\n')
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')
    print('\n')



# You'll implement the employee functions in the lab

def list_employees():
    pass


def find_employee_by_name():
    pass


def find_employee_by_id():
    pass


def create_employee():
    pass


def update_employee():
    pass


def delete_employee():
    pass


def list_department_employees():
    pass