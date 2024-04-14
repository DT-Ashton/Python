num_list = []
def enterlist():
    print('Input a list of integer number')
    while len(num_list) <= 100:
        number = int(input('Enter an integer numbers: '))
        if number == 0:
            break
        num_list.append(number)

def searchvalue():
    search = int(input('Enter the value you search for: '))
    if search in num_list:
        print(search, 'is found')
    else:
        print('The value is not found')

def printlargest():
    largest = num_list[0]
    for n in num_list:
        if n > largest:
            largest = n
    print('The largest value in the list:', largest)

def remove():
    value = int(input('Enter the value you want to remove: '))
    if value in num_list:
        num_list.remove(value)
        print('Removed')
    else:
        print('The value is not in the list')

def printlist():
    num_list.sort()
    print(num_list)

def menu():
    print('_____ Menu _____')
    print('1. Enter the list of integer number')
    print('2. Search for a value in a list')
    print('3. Print out the element with the largest value in the list')
    print('4. Remove the element whose value is equal to the value entered by the user')
    print('5. Print out the list in ascending order')
    print('6. Quit')

def main():
    while True:
        menu()
        try:
            choice = int(input('Choose a number from menu: '))
            if choice == 1:
                enterlist()
            elif choice == 2:
                searchvalue()
            elif choice == 3:
                printlargest()
            elif choice == 4:
                remove()
            elif choice == 5:
                printlist()
            else:
                break
        except:
            print('Invalid input. Try again.')

if __name__ == '__main__':
    main()
