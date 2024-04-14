def numberofstudent():
    number = int(input('Enter the number of students in the class (10 < number of students <= 100): '))
    if number <= 10 or number > 100:
        print('Invalid input. Try again')
        return numberofstudent()
    else:
        return number

student_list = []
def addstudent():
    number = int(input('Enter the number of students:'))
    for i in range(number):
        if len(student_list) == 100:
            print('There are 100 students in the list')
            break
        name = input('Enter student first name: ')
        student_list.append(name)

def removestudent():
    newlist = []
    for n in student_list:
        if n not in newlist:
            newlist.append(n)
    student_list.clear()
    for n in newlist:
        student_list.append(n)
    print('Done')

def printname():
    for n in student_list:
        if 'an' in n:
            print(n)

def printlist():
    student_list.sort(reverse=True)
    print(student_list)

def menu():
    print('_____ Menu _____')
    print('1. Enter the number of students in the class')
    print('2. Add a student list')
    print('3. Remove students with the same first name')
    print('4. Print out students whose first name contains the string "an"')
    print('5. Print the list in ascending order')
    print('6. Quit')

def main():
    while True:
        menu()
        try:
            choice = int(input('Choose a number from menu: '))
            if choice == 1:
                numberofstudent()
            elif choice == 2:
                addstudent()
            elif choice == 3:
                removestudent()
            elif choice == 4:
                printname()
            elif choice == 5:
                printlist()
            else:
                break
        except:
            print('Invalid input. Try again.')

if __name__ == '__main__':
    main()
