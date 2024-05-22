import argparse
from turing import Turing


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("tape", help="Tape for the Touring machine")
    parser.add_argument("file", help="File with instructions")
    args = parser.parse_args()
    file = args.file
    with open(file, "r") as f:
        i_list = f.readlines()
    MACHINE = Turing(args.tape, i_list)
    MACHINE.run()


if __name__ == "__main__":
    main()
