def check(p):
 l = False
 n = False
 u = False
 s = False
 if len(p) >= 6 and len(p) <= 12:
    for i in p:
        if i.islower():
            l = True
        elif i.isdigit():
            n = True
        elif i.isupper():
            u = True
        elif i == '$' or i == '@' or i == '#':
            s = True
    if l and n and u and s:
        print('Password is strong enough.')
        return True
    else:
        print('Password should contain upper case letter, number and special character.')
        return False
 else:
     print('Password must contain 6 - 12 characters.')
     return False

while True:
    p = input('Enter password: ')
    value = check(p)
    if value == True:
        print('Valid password')
        break
    else:
        print('Invalid password. Try again.')