def binarySearch (arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid  # If x is present then return its location
        elif arr[mid] < target:
            left = mid + 1
        else:   # if not, return -1
            right = mid - 1
    return -1

arr = [2, 3, 4, 10, 40]
target = 10
result = binarySearch(arr, target)
if result == -1:
    print(f"{target} not found in array")
else: 
    print(f"{target} found at index {result}")
