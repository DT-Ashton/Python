def print_word(string):
    for w in string:
        if w.isspace():
            string = string.replace(" ", "")
    word = string.split(',')
    word.sort()
    line = ','.join(word)
    print(line)

def main():
    string = input('Enter some words separated by commas: ')
    print_word(string)

if __name__ == "__main__":
    main()

