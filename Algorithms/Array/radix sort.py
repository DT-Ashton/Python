def radixSort(arr):
    # A two-dimensional array with index 0 to 9 to hold values with the current radix in focus
    radixArray = [[], [], [], [], [], [], [], [], [], []]
    maxVal = max(arr)
    exp = 1
    while maxVal // exp > 0:  # any number beyond the decimal point are disregarded, and an integer is returned.
        while len(myArray) > 0:
            value = arr.pop()
            # decided where to put a value in the radixArray based on its radix, or digit in focus
            radixIndex = (value // exp) % 10
            radixArray[radixIndex].append(value)
        print('radix arr:', radixArray)

        for bucket in radixArray:
            while len(bucket) > 0:
                val = bucket.pop()
                arr.append(val)
        print(f'my arr: {arr} \n')
        exp *= 10

myArray = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", myArray)
radixSort(myArray)
print("Sorted array:", myArray)
