def selectionSort(my_array):
    n = len(my_array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if my_array[j] < my_array[min_index]:
                min_index = j
        print(f'min {my_array[min_index]} swap with {my_array[i]}:')
        my_array[i], my_array[min_index] = my_array[min_index], my_array[i]
        print(i, my_array, '\n')
    print("Sorted array:", my_array)

arr = [64, 34, 25, 12, 22, 11, 90, 5]
print("original: ", arr)
selectionSort(arr)
