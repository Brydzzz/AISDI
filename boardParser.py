from graph import Graph, Vertice


class BoardParser:
    def __init__(self, board_file: str) -> None:
        self.file = board_file
        self.board: list[list[Vertice]] = self._create_2d_array()

    def _create_2d_array(self) -> list[list[Vertice]]:
        board = []
        with open(self.file) as f:
            for row in f:
                row_array = [Vertice(tile) for tile in row.strip()]
                board.append(row_array)
        return board

    def has_above(self, src_row: int, src_col: int) -> bool:
        return True

    def has_under(self, src_row: int, src_col: int) -> bool:
        return True

    def has_left(self, src_row: int, src_col: int) -> bool:
        return True

    def has_right(self, src_row: int, src_col: int) -> bool:
        return True

    def get_weight(self, vertice: Vertice) -> int:
        pass

    def create_graph(self) -> Graph:
        graph = Graph()
        for row_idx, row in enumerate(self.board):
            for col_idx, element in enumerate(row):
                graph.add_vertice(element)

                # above edge
                if self.has_above(row_idx, col_idx):
                    above_element = self.board[row_idx - 1, col_idx]
                    weight = self.get_weight(above_element)
                    graph.add_edge(element, above_element, weight)

                # under edge
                if self.has_under(row_idx, col_idx):
                    under_element = self.board[row_idx + 1, col_idx]
                    weight = self.get_weight(under_element)
                    graph.add_edge(element, under_element, weight)

                # left edge
                if self.has_left(row_idx, col_idx):
                    left_element = self.board[row_idx, col_idx - 1]
                    weight = self.get_weight(left_element)
                    graph.add_edge(element, left_element, weight)

                # right edge
                if self.has_right(row_idx, col_idx):
                    right_element = self.board[row_idx, col_idx + 1]
                    weight = self.get_weight(right_element)
                    graph.add_edge(element, right_element, weight)
