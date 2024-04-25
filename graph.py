class Vertice:
    def __init__(self, value) -> None:
        self.key = value
        self.parent: Vertice = None
        self.distance: int = None
        self.checked: bool = False

    def __repr__(self) -> str:
        return f"(Key: {self.key}, Distance: {self.distance})"


class Graph:
    def __init__(self) -> None:
        self.adj_list: dict[Vertice, list[tuple[Vertice, int]]] = {}

    def add_vertice(self, new_vertice: Vertice) -> None:
        self.adj_list[new_vertice] = []

    def add_edge(
        self, src_vertice: Vertice, target_vertice: Vertice, weight: int
    ):
        # TODO implement
        pass
