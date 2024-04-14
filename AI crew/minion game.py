def minion_game(string):
    string = string.upper()
    vowels = ['A', 'E', 'I', 'O', 'U']
    score_stuart = score_kevin = 0

    for i in range(len(string)):
        if string[i] in vowels:
            score_stuart += len(string) - i
        else:
            score_kevin += len(string) - i

    if score_stuart > score_kevin:
        print('Stuart', score_stuart)
    elif score_kevin > score_stuart:
        print('Kevin', score_kevin)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
