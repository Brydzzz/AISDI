import argparse
from boardParser import BoardParser
from dijkstra import dijkstra


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="file with board")
    parser.add_argument("output_file", help="route output file")
    args = parser.parse_args()
    filename = args.filename
    with open(filename, "r") as file:
        b = BoardParser(file)
    gr = b.create_graph()
    x1, x2 = b.find_start_end()
    dijkstra(gr, x1, x2)
    b.print_route(x2)
    b.save_route(args.output_file, x2)


if __name__ == "__main__":
    main()
