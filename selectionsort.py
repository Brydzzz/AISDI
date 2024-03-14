def sorted_selection(sorted_arr):
    length = len(sorted_arr)
    sorted_arr_copy = [0] * length
    for i in range(length):
        sorted_arr_copy[i] = sorted_arr[i]
    return selection_sort(sorted_arr_copy)


def selection_sort(sorted_arr):
    """
    selection sort algorithm which doesn't mutate
    the input
    arguments:
    sorted_arr - what we want to sort
    """
    i = 0
    length = len(sorted_arr)
    for _ in range(length):
        smallest = sorted_arr[i]
        s_index = i
        for n in range(i, length):
            if sorted_arr[n] < smallest:
                smallest = sorted_arr[n]
                s_index = n
        sorted_arr[i], sorted_arr[s_index], sorted_arr[s_index], sorted_arr[i]
        i += 1
        return sorted_arr
