def quick_sort(arr):
    """
    This function makes sure that sorting doesn't mutate
    the original arr and returns a new one in a way that doesn't
    mess with the algorithm itself
    """
    length = len(arr)
    arr_copy = [0] * (length)
    for i in range(length):
        arr_copy[i] = arr[i]
    quicksort_main(arr_copy, 0, length - 1)
    return arr_copy


def quicksort_main(arr, p, r):
    """
    recursive quicksort algorithm:
    arguments:
    arr - dynamically mutated list
    p - starting index
    r - ending index
    """
    if p < r:
        q = partition(arr, p, r)
        quicksort_main(arr, p, q - 1)
        quicksort_main(arr, q + 1, r)


def partition(arr, p, r):
    """
    partition function, which puts smaller than pivot
    values on the left side of it, and bigger than pivot
    values on the right side
    """
    pv = arr[r]
    j = p
    for i in range(p, r):
        if arr[i] < pv:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    arr[j], arr[r] = arr[r], arr[j]
    return j
