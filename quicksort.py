def sorted_quicksort(sorted_arr):
    """
    This function makes sure that sorting doesn't mutate
    the original sorted_arr and returns a new one in a way that doesn't
    mess with the algorithm itself
    """
    length = len(sorted_arr)
    sorted_arr_copy = [0] * (length)
    for i in range(length):
        sorted_arr_copy[i] = sorted_arr[i]
    quicksort(sorted_arr_copy, 0, length - 1)
    return sorted_arr_copy


def quicksort(sorted_arr, p, r):
    if p < r:
        q = partition(sorted_arr, p, r)
        quicksort(sorted_arr, p, q - 1)
        quicksort(sorted_arr, q + 1, r)


def partition(sorted_arr, p, r):
    pv = sorted_arr[r]
    j = p
    for i in range(p, r):
        if sorted_arr[i] <= pv:
            sorted_arr[j], sorted_arr[i] = sorted_arr[i], sorted_arr[j]
            j += 1
    sorted_arr[j], sorted_arr[r] = sorted_arr[r], sorted_arr[j]
    return j
