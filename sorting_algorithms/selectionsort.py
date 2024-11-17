def selection_sort(arr):
    """
    selection sort algorithm which doesn't mutate
    the input
    arguments:
    arr - array that we want to sort
    """
    length = len(arr)
    arr_copy = [0] * length
    for i in range(length):
        arr_copy[i] = arr[i]
    for i in range(length):
        min_index = i
        for n in range(i, length):
            if arr_copy[n] < arr_copy[min_index]:
                min_index = n
        arr_copy[i], arr_copy[min_index] = arr_copy[min_index], arr_copy[i]
    return arr_copy
