import string
#-----------------------------------------------------------------------------
def countConsonant(c1, c2):
    # Begin your statements
    c1 = c1.lower()
    c2 = c2.lower()
    Count = 0
    if c1 > c2:
        c1, c2 = c2, c1
    consonant = [b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, y, z]
    for c in range(c1, c2 + 1):
        if c in consonant:
            if
            Count = Count + 1



    #End your statements
#end countConsonant
#==========DO NOT ADD NEW OR CHANGE THE STATEMENTS IN THE MAIN FUNCTION========
def main():
    print("TEST Q3 (2 marks):")
    c1 = input("Enter c1 = ")
    c2 = input("Enter c2 = ")
    count = countConsonant(c1, c2)
    print("\nOUTPUT:")
    print(count)
#end main
if __name__ == "__main__":
    main()
#==============================================================================
