def check(password):
    if 6 <= len(password) <= 15:
        lower = 0
        number = 0
        upper = 0
        special = 0
        for i in password:
            if i.islower():
                lower = lower + 1
            elif i.isdigit():
                number = number + 1
            elif i.isupper():
                upper = upper + 1
            elif i == '$' or i == '#' or i == '@' or i == '&' or i == '?':
                special = special + 1
        if lower >= 2 and number >= 3 and upper >= 1 and special >= 1:
            return True
        else:
            return False
    else:
        return False

def main():
    while True:
        password = input('Enter password: ')
        if check(password):
            print('Valid password')
            break
        else:
            print('Invalid password. Try again.')

if __name__ == "__main__":
    main()
