pa = 9000000
pd = 3600000
# case 2:
income = 440000000
print('Your income in this year:', income)
n = 4
print('Number of dependent:', n)
tf = 12*(pa + n*pd)
print('Tax-free income:', tf)
ti = income - tf
if ti <= 0:
    ti = 0
    it = 0
elif ti <= 5000000:
    it = ti*5/100
elif ti <= 10000000:
    it = 250000 + (ti - 5000000)*10/100
elif ti <= 18000000:
    it = 750000 + (ti - 10000000)*15/100
else:
    it = 1950000 + (ti - 18000000)*20/100
print('Taxable income:', ti)
print('Income tax:', it)
