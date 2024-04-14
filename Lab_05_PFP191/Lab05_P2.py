# Q2.1
def count():
    file1 = open('poem.txt')
    Count = 0
    for line in file1:
        for word in line:
            Count = Count + 1
    print('Total words are', Count)

# Q2.2
def display_words():
    file2 = open('story.txt')
    for lines in file2:
        line = lines.split()
        for w in line:
            if len(w) < 4:
                print(w, end=' ')

def main():
    count()
    display_words()

if __name__ == '__main__':
    main()
