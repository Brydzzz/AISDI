from random import choice, randint
import argparse


def generate_random_board(x: int, y: int, filename: str) -> None:
    list = ["J", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    with open(filename, mode="w") as file_handler:
        x1_pos = (randint(1, x - 1), randint(1, y - 1))
        x2_pos = (randint(1, x - 1), randint(1, y - 1))
        row_number = 0
        while row_number != y:
            line = ""
            while len(line) - 1 != x:
                if (
                    len(line) - 1 == x1_pos[0] and row_number == x1_pos[1]
                ) or (len(line) - 1 == x2_pos[0] and row_number == x2_pos[1]):
                    element = "X"
                else:
                    element = choice(list)
                line += element
            line += "\n"
            file_handler.writelines(line)
            row_number += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "x", metavar="number_of_rows", help="Number of board rows", type=int
    )
    parser.add_argument(
        "y",
        metavar="number_of_columns",
        help="Number of board columns",
        type=int,
    )
    parser.add_argument(
        "output", metavar="output_file", help="file where board will be saved"
    )
    args = parser.parse_args()
    generate_random_board(args.x, args.y, args.output)
