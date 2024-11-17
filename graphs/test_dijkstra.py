# from graph import Vertice, Graph
from dijkstra import dijkstra
from boardParser import BoardParser
from io import StringIO

"""
X1J
921
X38
"""


def test_dijkstra():
    test_file_2 = StringIO("X1J\n921\nX38")
    bp = BoardParser(test_file_2)
    gr = bp.create_graph()
    vertices = list(gr.adj_list.keys())
    x = vertices[0]
    x2 = vertices[6]
    j = vertices[2]
    three = vertices[7]
    two = vertices[4]
    one = vertices[1]
    dijkstra(gr, x, x2)
    assert x2.parent == three
    assert x2.distance == 6
    assert two.parent == one
    assert one.parent == x
    assert j.distance == 1
    assert three.parent == two


"""
X1J
941
X31
"""


def test_dijkstra_2():
    test_file_2 = StringIO("X1J\n941\nX31")
    bp = BoardParser(test_file_2)
    gr = bp.create_graph()
    vertices = list(gr.adj_list.keys())
    x = vertices[0]
    x2 = vertices[6]
    j = vertices[2]
    three = vertices[7]
    two = vertices[4]
    one = vertices[1]
    one_second = vertices[5]
    one_third = vertices[8]
    dijkstra(gr, x, x2)
    assert x2.parent == three
    assert x2.distance == 5
    assert two.parent == one
    assert one.parent == x
    assert j.distance == 1
    assert three.parent == one_third
    assert one_third.parent == one_second
    assert one_second.parent == j
    assert j.parent == one


def test_dijkstra_print_route():
    test_file_2 = StringIO("X1J\n941\nX31")
    bp = BoardParser(test_file_2)
    gr = bp.create_graph()
    vertices = list(gr.adj_list.keys())
    x = vertices[0]
    x2 = vertices[6]
    dijkstra(gr, x, x2)
    bp.print_route(x2)
