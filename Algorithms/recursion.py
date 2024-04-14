# recursion
def P(a,n):
    if n == 0:
        return 1
    else:
        return a * P(a,n -1)
print(P(2,3))
print(P(4,3))