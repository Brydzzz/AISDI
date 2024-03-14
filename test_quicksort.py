from random import randint
import pytest
from quicksort import sorted_quicksort


def generate_random_list(size):
    random_list = [0] * size
    for i in range(size - 1):
        random_list[i] = randint(0, size + 1)
    return random_list


def test_quicksort_1000():
    to_be_sort = generate_random_list(1000)
    assert sorted_quicksort(to_be_sort) == sorted(to_be_sort)
