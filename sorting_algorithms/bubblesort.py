def bubble_sort(arr):
    """
    selection sort algorithm which doesn't mutate
    the input
    arguments:
    arr - array that we want to sort
    """
    n = len(arr)
    result = [0] * n
    for i in range(n):
        result[i] = arr[i]

    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                swapped = True
                result[j], result[j + 1] = result[j + 1], result[j]
        if not swapped:
            return result
    return result
