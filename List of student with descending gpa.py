def take_value(value):
    return value[1]

def sort_list(StudentList):
    for gpa, n in sorted(StudentList.items(), key=take_value, reverse=True):
        # Cách 2: sorted(StudentList.items(), key=lamda value: value[1], reverse=True):
        print(gpa, n)
            
while True:
    try:
        StudentList = dict()
        for i in range(10):
            name = input("Enter student's full name: ")
            GPA = float(input("Enter GPA: "))
            StudentList[name] = GPA
        sort_list(StudentList)
        break
    except:
        print('Invalid input. Try again.')
