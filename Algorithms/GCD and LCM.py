def GCD(a,b):
    if b == 0:
        return a
    return GCD(b, a%b)

def LCM(a,b):
    for i in range(1, a*b + 1):
        if i%a == 0 and i%b == 0:
            return i

print(GCD(24,36))
print(LCM(24,36))

# Số nguyên tố
nums = range(2, 50)
for i in range(2, 8):
    print(i,)
    nums = list(filter(lambda x: x == i or x % i, nums))
    print(nums)