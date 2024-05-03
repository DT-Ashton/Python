def mergeSort(arr):  # Diving array into 2 halves
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    sortedLeft = mergeSort(left)  # Sorting first half
    sortedRight = mergeSort(right)  # Sorting second half

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    print(left, right)

    result.extend(left[i:])
    result.extend(right[j:])
    print(result, '\n')

    return result

arr = [3, 7, 6, -10, 15, 23.5, 55, -13]
print("Original:", arr)
sortedArr = mergeSort(arr)
print("Sorted array:", sortedArr)
