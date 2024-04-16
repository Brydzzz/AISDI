from bst import BSTree
from time import process_time
import gc
from matplotlib import pyplot as plt
from random import randint


def generate_random_list(size: int) -> list[int]:
    random_list = [0] * size
    for i in range(size - 1):
        random_list[i] = randint(0, size + 1)
    return random_list


def gather_bst_insert_data(
    nums_to_insert: list[int], step: int
) -> list[tuple[int, int]]:
    length = len(nums_to_insert)
    data = []
    for n in range(1, length, step):
        nums = nums_to_insert[:n]
        bst_tree = BSTree()
        gc_old = gc.isenabled()
        gc.disable()
        t1 = process_time()
        for num in nums:
            bst_tree.insert(num)
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


def main():
    nums = generate_random_list(400000)

    # gather BST insert data
    print("Started gathering data for BSTree insert()")
    bst_insert_data = gather_bst_insert_data(nums, 10000)
    print("Finished gathering data for BSTree insert()")

    # gather BST search data
    # gather BST delete data

    # plot BST insert data
    create_bst_insert_plot(bst_insert_data)
    # plot BST search data
    # plot BST delete data
    pass


if __name__ == "__main__":
    main()
