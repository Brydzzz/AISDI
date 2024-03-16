from time import process_time
from matplotlib import pyplot as plt

from bubblesort import bubble_sort
from mergesort import merge_sort
from quicksort import quick_sort
from selectionsort import sorted_selection


def load_words(file):
    words = []
    with open(file, "r") as file_handler:
        for line in file_handler.readlines():
            temp = line.split()
            words.extend(temp)
    return words


def get_plot_point(word_list, size, function):
    t1 = process_time()
    function(word_list[:size])
    t2 = process_time()
    return size, t2 - t1


def get_subplot_data(word_list, function, step):
    algorithm_data = []
    print(f"Started gathering data with {function}")
    for i in range(1000, 10001, step):
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
    pan_t_words = load_words("pan_tadeusz.txt")
    merge_data = get_subplot_data(pan_t_words, merge_sort, 1000)
    quick_data = get_subplot_data(pan_t_words, quick_sort, 1000)
    bubble_data = get_subplot_data(pan_t_words, bubble_sort, 1000)
    selection_data = get_subplot_data(pan_t_words, sorted_selection, 1000)
    generate_plot_all(merge_data, quick_data, bubble_data, selection_data)
    generate_plot_fast_sorts(merge_data, quick_data)
    generate_plot_slow_sorts(bubble_data, selection_data)
