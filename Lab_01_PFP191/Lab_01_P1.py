month = int(input('Enter month in number: '))
if month <= 3:
    print("It's Spring")
elif month <= 6:
    print("It's Summer")
elif month <= 9:
    print("It's Fall")
elif month <= 12:
    print("It's Winter")
else:
    print('The month is not recognized')
