def partition(arr, low, high):  # swaps the pivot element into the sub-array and returns the pivot index
    i = low-1  # index of element that is smaller than the pivot
    pivot = arr[high]
    print('\npivot:', pivot, arr)
    for j in range(low, high):
        if arr[j] < pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
            print(f'swap {i} with {j}: {arr}')
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quickSort(arr, low, high):
    if low < high:
        # pi is pivot index
        pi = partition(arr, low, high)
        # Separately sort elements before partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

arr = [3, 5, 6, 2, 1, 4]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:", arr)
