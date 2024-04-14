# Yêu cầu 1:
def except_int(string):
    integer = []
    for i in string:
        if i.isdigit():
            integer.append(i)
    new = ''.join(integer)
    print(new)

# Yêu cầu 2:
def remove_special(string):
    line = []
    for i in string:   
        if i.isalnum():
            line.append(i)
        elif i == ' ':
            line.append(i)
    print(''.join(line))

string = str(input('Enter a string: '))
except_int(string)
remove_special(string)
