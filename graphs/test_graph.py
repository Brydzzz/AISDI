# TODO write tests for Vertice and Graph classes
from graph import Vertice


def test_vertice_lt():
    a = Vertice("a")
    a.distance = 10
    b = Vertice("b")
    b.distance = 20
    assert a < b
    assert not b < a


def test_vertice_max_distancelt():
    a = Vertice("a")
    a.distance = 10
    b = Vertice("b")
    assert a < b
    assert not b < a
