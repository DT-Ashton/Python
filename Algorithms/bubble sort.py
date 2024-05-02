def bubbleSort(arr): 
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        print(i, arr)
        if not swapped:
            print(swapped)
            break
    return arr

# Driver code to test above 
arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted arr:", bubbleSort(arr))
