def remove(line):
    for i in line:
        if i.isspace():
            line = line.replace(' ', '')
    names = line.split(',')
    new = []
    for name in names:
        if name not in new:
            new.append(name)
    newline = ','.join(new)
    print(newline)

def main():
    line = input('Enter names of students: ')
    remove(line)

if __name__ == "__main__":
    main()

