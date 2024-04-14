def menu():
    print('--- Menu ---')
    print('1: Add employee')
    print('2: Find employee')
    print('3: Update employee')
    print('4: Delete employee')
    print('5: Print list of employee in descending order')
    print('6: Save to file')
    print('7: Exist')

employee_list = dict()

def num_of_employee():
    number = int(input('Enter the number of employee: '))
    return number

def add_employee():
    n = num_of_employee()
    for i in range(0, n):
        code = input("Enter employee's code: ")
        name = input("Enter employee's fullname: ")
        salary = float(input("Enter employee's salary: "))
        employee_list[code] = {'fullname': name, 'salary': salary}

def find_employee():
    find = input("Enter employee's code: ")
    employee = dict()
    employee[find] = employee_list[find]
    for v in employee.items():
        print(v[0], v[1]['fullname'], v[1]['salary'])


def update_employee():
    add_employee()
    print('Employee list after update: ')
    print(employee_list)


def delete_employee():
    delete = input("Enter employee's code: ")
    employee_list.pop(delete)
    print('Deleted.')


def print_list():
    emp_list = sorted(employee_list.items(), key=lambda x: x[1]['salary'], reverse=True)
    for i in emp_list:
        print(i[0], i[1]['fullname'], i[1]['salary'])


def save_file():
    file = open('employee_information.txt', 'w')
    for key, value in employee_list.items():
        file.write('%s %s %s\n' % (key, value['fullname'], value['salary']))
    file.close()


def main():
    while True:
        menu()
        choose = 0
        try:
            choose = int(input('Enter a number from menu: '))
            if choose == 1:
                add_employee()
            elif choose == 2:
                find_employee()
            elif choose == 3:
                update_employee()
            elif choose == 4:
                delete_employee()
            elif choose == 5:
                print_list()
            elif choose == 6:
                save_file()
            else:
                break
        except:
            print('Invalid input. Try again')

if __name__ == '__main__':
    main()
1