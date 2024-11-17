from time import process_time
from matplotlib import pyplot as plt
import gc
import sys

from bubblesort import bubble_sort
from selectionsort import selection_sort
from mergesort import merge_sort
from quicksort import quick_sort


def load_words(file):
    words = []
    with open(file, "r") as file_handler:
        for line in file_handler.readlines():
            temp = line.split()
            words.extend(temp)
    return words


def get_plot_point(word_list, size, function):
    sliced_list = word_list[:size]
    gc_old = gc.isenabled()
    gc.disable()
    t1 = process_time()
    function(sliced_list)
    t2 = process_time()
    if gc_old:
        gc.enable()
    return size, t2 - t1


def get_subplot_data(word_list, function, step, max_words):
    algorithm_data = []
    print(f"Started gathering data with {function}")
    for i in range(1000, max_words, step):
        point = get_plot_point(word_list, i, function)
        algorithm_data.append(point)
    print(f"Finished gathering data with {function}")
    return algorithm_data


def generate_subplot(data):
    time_values = [point[1] for point in data]
    size_values = [point[0] for point in data]
    plt.plot(size_values, time_values, marker="o", linestyle="-")


def generate_plot_all(merge_data, quick_data, bubble_data, selection_data):
    generate_subplot(merge_data)
    generate_subplot(quick_data)
    generate_subplot(bubble_data)
    generate_subplot(selection_data)
    plt.title("Sorting Algorithms Comparison")
    plt.ylabel("Time [s]")
    plt.xlabel("N number of elements")
    plt.legend(["Merge Sort", "Quick Sort", "Bubble Sort", "Selection Sort"])
    plt.grid()
    plt.savefig("all_comparison.png")
    plt.clf()


def generate_plot_slow_sorts(bubble_data, selection_data):
    generate_subplot(bubble_data)
    generate_subplot(selection_data)
    plt.title("Sorting Algorithms Comparison")
    plt.ylabel("Time [s]")
    plt.xlabel("N number of elements")
    plt.legend(["Bubble Sort", "Selection Sort"])
    plt.grid()
    plt.savefig("slow_comparison.png")
    plt.clf()


def generate_plot_fast_sorts(merge_data, quick_data):
    generate_subplot(merge_data)
    generate_subplot(quick_data)
    plt.title("Sorting Algorithms Comparison")
    plt.ylabel("Time [s]")
    plt.xlabel("N number of elements")
    plt.legend(["Merge Sort", "Quick Sort"])
    plt.grid()
    plt.savefig("fast_comparison.png")
    plt.clf()


if __name__ == "__main__":
    sys.setrecursionlimit(20000)
    pan_t_words = load_words("pan_tadeusz.txt")
    pan_t_words_len = len(pan_t_words)
    merge_data = get_subplot_data(pan_t_words, merge_sort, 1000, 10001)
    quick_data = get_subplot_data(pan_t_words, quick_sort, 1000, 10001)
    bubble_data = get_subplot_data(pan_t_words, bubble_sort, 1000, 10001)
    selection_data = get_subplot_data(
        pan_t_words, selection_sort, 1000, 10001
    )
    merge_data_bigger_size = get_subplot_data(
        pan_t_words, merge_sort, 3000, pan_t_words_len
    )
    quick_data_bigger_size = get_subplot_data(
        pan_t_words, quick_sort, 3000, pan_t_words_len
    )
    generate_plot_all(merge_data, quick_data, bubble_data, selection_data)
    generate_plot_slow_sorts(bubble_data, selection_data)
    generate_plot_fast_sorts(merge_data_bigger_size, quick_data_bigger_size)
