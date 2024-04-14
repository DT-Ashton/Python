# Q1.1
def display():
    file1 = open('poem.txt')
    for line in file1:
        line = line.rstrip()
        print(line)

# Q1.2
def count():
    file2 = open('story.txt')
    Count = 0
    for lines in file2:
        if not lines.startswith('T'):
            Count = Count + 1
    print("Number of lines not starting with 'T'= ", Count)

def main():
    display()
    count()

if __name__ == '__main__':
    main()
