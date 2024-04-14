# Q3.1
def count_upper():
    file1 = open('story.txt')
    Count = 0
    for line in file1:
        for char in line:
            if char.isupper():
                Count = Count + 1
    print(Count)

# Q3.2
def count_words():
    file2 = open('article.txt')
    count = 0
    for lines in file2:
        line = lines.split()
        this = line.count('this')
        these = line.count('these')
        count = count + this + these
    print(count)

def main():
    count_upper()
    count_words()

if __name__ == '__main__':
    main()
