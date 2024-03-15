def bubble_sort(arr):
    n = len(arr)
    swapped = False
    result = [0] * n
    for i, element in enumerate(arr):
        result[i] = element

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                swapped = True
                result[j], result[j + 1] = result[j + 1], result[j]
        if not swapped:
            return result
    return result
