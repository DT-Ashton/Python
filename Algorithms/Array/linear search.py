def search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i   # If x is present then return its location
    return -1          # otherwise, return -1

arr = [2, 3, 4, 10, 40]
target = 10
result = search(arr, target)
if result == -1:
    print(f"{target} not found in array")
else:
    print(f"{target} found at index {result}")
