from bst import BSTree
from time import process_time
import gc
from matplotlib import pyplot as plt
from random import randint, choice


def generate_random_list(size: int) -> list[int]:
    random_list = [0] * size
    for i in range(size - 1):
        random_list[i] = randint(0, size + 1)
    return random_list


def gather_bst_insert_data(
    keys_to_insert: list[int], step: int
) -> list[tuple[int, int]]:
    length = len(keys_to_insert)
    data = []
    for n in range(1, length, step):
        keys = keys_to_insert[:n]
        bst_tree = BSTree()
        gc_old = gc.isenabled()
        gc.disable()
        t1 = process_time()
        for key in keys:
            bst_tree.insert(key)
        t2 = process_time()
        if gc_old:
            gc.enable()
        data.append((n, t2 - t1))
    return data


def create_bst_insert_plot(data: list[tuple[int, int]]) -> None:
    size_values = [point[0] for point in data]
    time_values = [point[1] for point in data]
    plt.plot(size_values, time_values, marker="o", linestyle="-")
    plt.title("BSTree Insert")
    plt.ylabel("Time [s]")
    plt.xlabel("Number of n elements")
    plt.grid()
    plt.savefig("bst_insert_plot.png")
    plt.clf()


def gather_bst_search_data(
    keys_in_bst: list[int], step: int, key_to_search: int
) -> list[tuple[int, int]]:
    length = len(keys_in_bst)
    data = []
    for n in range(1, length, step):
        keys = keys_in_bst[:n]
        bst_tree = BSTree(list=keys)
        gc_old = gc.isenabled()
        gc.disable()
        t1 = process_time()
        bst_tree.search(key_to_search)
        t2 = process_time()
        if gc_old:
            gc.enable()
        data.append((n, t2 - t1))
    return data


def create_bst_search_plot(data: list[tuple[int, int]]) -> None:
    size_values = [point[0] for point in data]
    time_values = [point[1] for point in data]
    plt.plot(size_values, time_values, marker="o", linestyle="-")
    plt.title("BSTree Search")
    plt.ylabel("Time [s]")
    plt.ylim(top=10 ** (-4))
    plt.xlabel("Number of n elements")
    plt.grid()
    plt.savefig("bst_search_plot.png")
    plt.clf()


def gather_bst_delete_data(
    keys_in_bst: list[int], step: int, key_to_delete: int
) -> list[tuple[int, int]]:
    length = len(keys_in_bst)
    data = []
    for n in range(1, length, step):
        keys = keys_in_bst[:n]
        bst_tree = BSTree(list=keys)
        gc_old = gc.isenabled()
        gc.disable()
        t1 = process_time()
        bst_tree.delete(key_to_delete)
        t2 = process_time()
        if gc_old:
            gc.enable()
        data.append((n, t2 - t1))
    return data


def create_bst_delete_plot(data: list[tuple[int, int]]) -> None:
    size_values = [point[0] for point in data]
    time_values = [point[1] for point in data]
    plt.plot(size_values, time_values, marker="o", linestyle="-")
    plt.title("BSTree Delete")
    plt.ylabel("Time [ms]")
    plt.ylim(bottom=0, top=10 ** (-4))
    plt.xlim(left=0)
    plt.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
    plt.xlabel("Number of n elements")
    plt.grid()
    plt.savefig("bst_delete_plot.png")
    plt.clf()


def main():
    keys = generate_random_list(40000)
    key_to_search = choice(keys)
    key_to_delete = choice(keys)

    # gather BST insert data
    print("Started gathering data for BSTree insert()")
    bst_insert_data = gather_bst_insert_data(keys, 10000)
    print("Finished gathering data for BSTree insert()")
    # plot BST insert data
    create_bst_insert_plot(bst_insert_data)

    # gather BST search data
    print("Started gathering data for BSTree search()")
    bst_search_data = gather_bst_search_data(keys, 5000, key_to_search)
    print("Finished gathering data for BSTree search()")
    # plot BST search data
    create_bst_search_plot(bst_search_data)

    # gather BST delete data
    print("Started gathering data for BSTree delete()")
    bst_delete_data = gather_bst_search_data(keys, 1000, key_to_delete)
    print("Finished gathering data for BSTree delete()")
    # plot BST delete data
    create_bst_delete_plot(bst_delete_data)


if __name__ == "__main__":
    main()
