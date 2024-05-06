from random import choice, randint


def generate_random_board(x, y) -> None:
    list = ["J", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # title = f"random_board{x}x{y}.txt"
    with open("random_board.txt", mode="w") as file_handler:
        x1_pos = (randint(1, x - 1), randint(1, y - 1))
        x2_pos = (randint(1, x - 1), randint(1, y - 1))
        print(x1_pos, x2_pos)
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
    generate_random_board(20, 20)
