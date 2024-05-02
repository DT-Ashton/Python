def insertionSort(my_array):
    for i in range(1, len(my_array)):
        insert_index = i
        current_value = my_array[i]
        for j in range(i - 1, -1, -1):
            if my_array[j] > current_value:
                my_array[j + 1] = my_array[j]
                insert_index = j
            else:
                break
        print(f'value {current_value} insert to index {insert_index}:')
        my_array[insert_index] = current_value
        print(i, my_array)
        
# Driver code to test above 
arr = [12, 11, 13, 5, 6]
print('original:', arr)
insertionSort(arr)
print("Sorted array:", arr)
