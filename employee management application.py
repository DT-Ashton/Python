class Employee:
    def __init__(self, code, name, phone_number, address):
        self.code = code
        self.name = name
        self.phone_number = phone_number
        self.address = address


class Fulltime(Employee):
    def __init__(self, code, name, phone_number, address, absent):
        Employee.__init__(self, code, name, phone_number, address)  # Có thể dùng upper() thay cho Employee
        self.absent = absent
        self.salary = 1500
        self.total = 0


class Parttime(Employee):
    def __init__(self, code, name, phone_number, address, present):
        Employee.__init__(self, code, name, phone_number, address)
        self.present = present
        self.total = 0


employee_list = list()

def add_fulltime():
    code = input('Enter code:')
    name = input('Enter name:')
    phone_number = input('Enter phone number:')
    address = input('Enter address')
    absent = int(input('Enter absent: '))
    employee = Fulltime(code, name, phone_number, address, absent)
    employee_list.append(employee)
    checksalary(employee)

def add_parttime():
    code = input('Enter code:')
    name = input('Enter name:')
    phone_number = input('Enter phone number:')
    address = input('Enter address')
    present = int(input('Enter present: '))
    employee = Fulltime(code, name, phone_number, address, present)
    employee_list.append(employee)
    checksalary(employee)

def checksalary(employee):
    if isinstance(employee, Fulltime):
        dayoffwork = employee.absent * 40
        employee.total = employee.salary - dayoffwork
    else:
        employee.total = 25 * employee.present

def display_info(employee):
    print(employee.code, employee.name, employee.total)
    print('--------------------------------------')

def search_employee():
    result = -1
    search = input('Enter code: ')
    for x in employee_list:
        if search.upper() == x.code.upper():
            display_info(x)
            result = 1
    if result == -1:
        print('Not found')

def remove_employee():
    result = 0
    search = input('Enter code: ')
    for x in employee_list:
        if search.upper() == x.code.upper():
            employee_list.remove(x)
            result = 1
    return result

def sort_list():
    employee_list.sort(key=lambda v: v.total)
    for e in employee_list:
        display_info(e)

def menu():
    print('-----Menu-----')
    print('1: Add a new fulltime employee')
    print('2. Add a new parttime employee')
    print('3. Search an employee')
    print('4. Remove an employee')
    print('5. Print a list of employees in ascending order of total salary')
    print('6. Exit')

def main():
    while True:
        menu()
        choose = 0
        try:
            choose = int(input('Choose a function from menu'))
        except:
            print('Invalid input. Try again.')
        if choose == 1:
            add_fulltime()
        elif choose == 2:
            add_parttime()
        elif choose == 3:
            search_employee()
        elif choose == 4:
            remove_employee()
        elif choose == 5:
            sort_list()
        else:
            break

if __name__ == '__main__':
    main()
