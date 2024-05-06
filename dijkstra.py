from heapq import heappush, heappop

from graph import Graph, Vertice


def dijkstra(graph: Graph, start: Vertice, end: Vertice) -> None:
    queue = [start]
    start.distance = 0
    while queue:
        source = queue[0]
        if source == end:
            break
        if source.checked is False:
            edges = graph.adj_list[source]
            for edge in edges:
                dest = edge[0]
                weight = edge[1]
                if weight + source.distance < dest.distance:
                    dest.parent = source
                    dest.distance = weight + source.distance
                    heappush(queue, dest)
            source.checked = True
        heappop(queue)
    mark_vertices(start, end)


def mark_vertices(start: Vertice, end: Vertice) -> None:
    start.marked = True
    end.marked = True
    vertice = end
    while vertice.parent:
        vertice.parent.marked = True
        vertice = vertice.parent
