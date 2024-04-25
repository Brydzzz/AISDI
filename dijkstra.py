from heapq import heappush, heappop


def dijkstra(graph, start, end) -> None:
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
                if dest.distance:
                    if weight + source.distance < dest.distance:
                        dest.parent = source
                        dest.distance = weight + source.distance
                        heappush(queue, dest)
                    # else:
                    #     dest.parent = source
                    #     dest.distance = weight + source.distance
                    #     heappush(queue, dest)
            heappop(queue)
            source.checked = True
        else:
            heappop(queue)
    mark_vertices(start, end)
    return


def mark_vertices(start, end) -> None:
    start.marked = True
    end.marked = True
    vertice = end
    while vertice.parent:
        vertice.parent.marked = True
        vertice = vertice.parent
