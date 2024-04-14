def reversed_words(string):
    word = string.split()
    new = ' '.join(reversed(word))
    return new

string = str(input('Enter a sentence: '))
print(reversed_words(string))
