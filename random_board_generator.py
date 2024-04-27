from random import choice, randint


def generate_random_board(x, y) -> None:
    list = ["J", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # title = f"random_board{x}x{y}.txt"
    with open("random_board.txt", mode="w") as file_handler:
        x1_pos = (randint(0, x), randint(0, y))
        x2_pos = (randint(0, x), randint(0, y))
        counter = 0
        while counter != y:
            line = ""
            while len(line) != x:
                if (len(line) == x1_pos[0] and counter == x1_pos[1]) or (
                    len(line) == x2_pos[0] and counter == x2_pos[1]
                ):
                    element = "X"
                else:
                    element = choice(list)
                line += element
            line += "\n"
            file_handler.writelines(line)
            counter += 1


if __name__ == "__main__":
    generate_random_board(200, 1000)
