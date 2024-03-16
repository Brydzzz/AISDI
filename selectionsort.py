def sorted_selection(arr):
    length = len(arr)
    arr_copy = [0] * length
    for i in range(length):
        arr_copy[i] = arr[i]
    return selection_sort(arr_copy)


def selection_sort(arr):
    """
    selection sort algorithm which doesn't mutate
    the input
    arguments:
    arr - what we want to sort
    """
    length = len(arr)
    arr_copy = [0] * length
    for i in range(length):
        arr_copy[i] = arr[i]
    length = len(arr_copy)
    for i in range(length):
        min_index = i
        for n in range(i, length):
            if arr_copy[n] < arr_copy[min_index]:
                min_index = n
        arr_copy[i], arr_copy[min_index] = arr_copy[min_index], arr_copy[i]
    return arr_copy
