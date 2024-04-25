import argparse
from boardParser import BoardParser


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="file with board")
    args = parser.parse_args()
    filename = args.filename
    with open(filename, "r") as file:
        b = BoardParser(file)
    print(b.board)


if __name__ == "__main__":
    main()
