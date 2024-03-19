def merge_sort(arr):
    """
    This function makes sure that sorting doesn't mutate
    the original arr and returns a new one in a way that doesn't
    mess with the algorithm itself
    """
    length = len(arr)
    arr_copy = [0] * (length)
    for i in range(length):
        arr_copy[i] = arr[i]
    mergesort_main(arr_copy, 0, length - 1)
    return arr_copy


def merge(arr, p, q, r):
    """
    merges two sorted lists
    """
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[p + i]
    for j in range(0, n2):
        R[j] = arr[q + j + 1]
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergesort_main(arr, p, r):
    """
    recursive mergesort algorithm:
    arguments:
    arr - dynamically mutated list
    p - starting index
    r - ending index
    """
    if p < r:
        q = (p + r) // 2
        mergesort_main(arr, p, q)
        mergesort_main(arr, q + 1, r)
        merge(arr, p, q, r)
    return arr
