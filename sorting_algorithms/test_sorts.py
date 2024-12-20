from random import randint
from quicksort import quick_sort
from bubblesort import bubble_sort
from selectionsort import selection_sort
from mergesort import merge_sort


def generate_random_list(size):
    random_list = [0] * size
    for i in range(size - 1):
        random_list[i] = randint(0, size + 1)
    return random_list


def test_quick_basic():
    to_be_sort = [6, 7, 9, 1, 3, 5, 4]
    assert quick_sort(to_be_sort) == sorted(to_be_sort)


def test_quick_words():
    to_be_sort = ["Tomek", "lubi", "pierogi", "a", "Brygida", "kocha", "zupy"]
    assert quick_sort(to_be_sort) == sorted(to_be_sort)


def test_quick_random_100():
    to_be_sort = generate_random_list(100)
    assert quick_sort(to_be_sort) == sorted(to_be_sort)


def test_quick_random_500():
    to_be_sort = generate_random_list(500)
    assert quick_sort(to_be_sort) == sorted(to_be_sort)


def test_selection_basic():
    to_be_sort = [4, 2, 7, 8, 9, 1, 2]
    assert selection_sort(to_be_sort) == sorted(to_be_sort)


def test_selection_words():
    to_be_sort = [
        "Programowanie",
        "bywa",
        "przyjemne",
        "szczególnie",
        "gdy",
        "wychodzi",
    ]
    assert selection_sort(to_be_sort) == sorted(to_be_sort)


def test_selection_random_100():
    to_be_sort = generate_random_list(100)
    assert selection_sort(to_be_sort) == sorted(to_be_sort)


def test_selection_random_500():
    to_be_sort = generate_random_list(500)
    assert selection_sort(to_be_sort) == sorted(to_be_sort)


def test_bubble_basic():
    to_be_sort = [8, 6, 3, 12, 67, 1, 2]
    assert bubble_sort(to_be_sort) == sorted(to_be_sort)


def test_bubble_words():
    to_be_sort = ["Dua", "Lipa", "wydaje", "nowy", "album", "w", "maju"]
    assert bubble_sort(to_be_sort) == sorted(to_be_sort)


def test_bubble_random_100():
    to_be_sort = generate_random_list(100)
    assert bubble_sort(to_be_sort) == sorted(to_be_sort)


def test_bubble_random_500():
    to_be_sort = generate_random_list(500)
    assert bubble_sort(to_be_sort) == sorted(to_be_sort)


def test_merge_basic():
    to_be_sort = [4, 2, 7, 8, 9, 1, 2]
    assert merge_sort(to_be_sort) == sorted(to_be_sort)


def test_merge_words():
    to_be_sort = ["Nie", "wolno", "zapominać", "o", "znaku", "równości"]
    assert merge_sort(to_be_sort) == sorted(to_be_sort)


def test_merge_random_100():
    to_be_sort = generate_random_list(100)
    assert merge_sort(to_be_sort) == sorted(to_be_sort)


def test_merge_random_500():
    to_be_sort = generate_random_list(500)
    assert merge_sort(to_be_sort) == sorted(to_be_sort)
