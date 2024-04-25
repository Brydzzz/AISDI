from graph import Graph, Vertice


class BoardParser:
    def __init__(self, board_file_handle) -> None:
        self.board: list[list[Vertice]] = self._create_2d_array(
            board_file_handle
        )

    def _create_2d_array(self, board_file_handle) -> list[list[Vertice]]:
        board = []
        for row in board_file_handle:
            row_array = [Vertice(tile) for tile in row.strip()]
            board.append(row_array)
        return board

    def has_above(self, src_row: int, src_col: int) -> bool:
        if src_row == 0:
            return False
        return True

    def has_under(self, src_row: int, src_col: int) -> bool:
        if src_row + 1 == len(self.board):
            return False
        return True

    def has_left(self, src_row: int, src_col: int) -> bool:
        if src_col == 0:
            return False
        return True

    def has_right(self, src_row: int, src_col: int) -> bool:
        if src_col + 1 == len(self.board[src_row]):
            return False
        return True

    def get_weight(self, vertice: Vertice) -> int:
        if vertice.key == "J" or vertice.key == "X":
            return 0
        return int(vertice.key)

    def create_graph(self) -> Graph:
        graph = Graph()
        for row_idx, row in enumerate(self.board):
            for col_idx, element in enumerate(row):
                graph.add_vertice(element)

                # above edge
                if self.has_above(row_idx, col_idx):
                    above_element = self.board[row_idx - 1][col_idx]
                    weight = (
                        0
                        if element.key == "J"
                        else self.get_weight(above_element)
                    )
                    graph.add_edge(element, above_element, weight)

                # under edge
                if self.has_under(row_idx, col_idx):
                    under_element = self.board[row_idx + 1][col_idx]
                    weight = (
                        0
                        if element.key == "J"
                        else self.get_weight(under_element)
                    )
                    graph.add_edge(element, under_element, weight)

                # left edge
                if self.has_left(row_idx, col_idx):
                    left_element = self.board[row_idx][col_idx - 1]
                    weight = (
                        0
                        if element.key == "J"
                        else self.get_weight(left_element)
                    )
                    graph.add_edge(element, left_element, weight)

                # right edge
                if self.has_right(row_idx, col_idx):
                    right_element = self.board[row_idx][col_idx + 1]
                    weight = (
                        0
                        if element.key == "J"
                        else self.get_weight(right_element)
                    )
                    graph.add_edge(element, right_element, weight)
        return graph
