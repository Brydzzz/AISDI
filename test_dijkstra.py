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
