from random import randint
from quicksort import sorted_quicksort


def generate_random_list(size):
    random_list = [0] * size
    for i in range(size - 1):
        random_list[i] = randint(0, size + 1)
    return random_list


def test_quick_basic():
    to_be_sort = [6, 7, 9, 1, 3, 5, 4]
    assert sorted_quicksort(to_be_sort) == sorted(to_be_sort)


def test_quick_words():
    to_be_sort = ["Tomek", "lubi", "pierogi", "a", "Brygida", "kocha", "zupy"]
    assert sorted_quicksort(to_be_sort) == sorted(to_be_sort)


def test_quick_random_100():
    to_be_sort = generate_random_list(100)
    assert sorted_quicksort(to_be_sort) == sorted(to_be_sort)


def test_quick_random_500():
    to_be_sort = generate_random_list(500)
    assert sorted_quicksort(to_be_sort) == sorted(to_be_sort)
