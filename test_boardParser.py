from io import StringIO

from boardParser import BoardParser

# test_file = StringIO("J112J\n12X21\nJ041J\n12X11\nJ111J")

"""
X14
J21
X38
"""
test_file_2 = StringIO("X14\nJ21\nX38")


def test_board_parser_ctor():
    bp = BoardParser(test_file_2)
    assert bp.board[0][0].key == "X"
    assert bp.board[0][1].key == "1"
    assert bp.board[0][2].key == "4"
    assert bp.board[1][0].key == "J"
    assert bp.board[1][1].key == "2"
    assert bp.board[1][2].key == "1"
    assert bp.board[2][0].key == "X"
    assert bp.board[2][1].key == "3"
    assert bp.board[2][2].key == "8"


def test_board_parser_has_above_true():
    test_file_2 = StringIO("X14\nJ21\nX38")
    bp = BoardParser(test_file_2)
    assert bp.has_above(src_row=1, src_col=0) is True


def test_board_parser_has_under_true():
    test_file_2 = StringIO("X14\nJ21\nX38")
    bp = BoardParser(test_file_2)
    assert bp.has_under(src_row=1, src_col=0) is True


def test_board_parser_has_left_true():
    test_file_2 = StringIO("X14\nJ21\nX38")
    bp = BoardParser(test_file_2)
    assert bp.has_left(src_row=1, src_col=1) is True


def test_board_parser_has_right_true():
    test_file_2 = StringIO("X14\nJ21\nX38")
    bp = BoardParser(test_file_2)
    assert bp.has_right(src_row=1, src_col=0) is True


def test_board_parser_has_above_false():
    test_file_2 = StringIO("X14\nJ21\nX38")
    bp = BoardParser(test_file_2)
    assert bp.has_above(src_row=0, src_col=0) is False


def test_board_parser_has_under_false():
    test_file_2 = StringIO("X14\nJ21\nX38")
    bp = BoardParser(test_file_2)
    assert bp.has_under(src_row=2, src_col=0) is False


def test_board_parser_has_left_false():
    test_file_2 = StringIO("X14\nJ21\nX38")
    bp = BoardParser(test_file_2)
    assert bp.has_left(src_row=1, src_col=0) is False


def test_board_parser_has_right_false():
    test_file_2 = StringIO("X14\nJ21\nX38")
    bp = BoardParser(test_file_2)
    assert bp.has_right(src_row=1, src_col=2) is False


def test_board_parser_get_weight_key_is_num():
    test_file_2 = StringIO("X14\nJ21\nX38")
    bp = BoardParser(test_file_2)
    v = bp.board[0][2]
    assert bp.get_weight(v) == 4


def test_board_parser_get_weight_key_is_joker():
    test_file_2 = StringIO("X14\nJ21\nX38")
    bp = BoardParser(test_file_2)
    v = bp.board[1][0]
    assert bp.get_weight(v) == 0


def test_board_parser_get_weight_key_is_X():
    test_file_2 = StringIO("X14\nJ21\nX38")
    bp = BoardParser(test_file_2)
    v = bp.board[0][0]
    assert bp.get_weight(v) == 0


def test_board_parser_graph():
    test_file_2 = StringIO("X14\nJ21\nX38")
    bp = BoardParser(test_file_2)
    gr = bp.create_graph()
    vertices = list(gr.adj_list.keys())
    x = vertices[0]
    j = vertices[3]
    one = vertices[1]
    one_second = vertices[5]
    four = vertices[2]
    three = vertices[7]
    two = vertices[4]
    x2 = vertices[6]
    eigth = vertices[8]
    assert gr.adj_list[x][0] == (j, 0)
    assert gr.adj_list[x][1] == (one, 1)
    assert gr.adj_list[one][0] == (two, 2)
    assert gr.adj_list[one][1] == (x, 0)
    assert gr.adj_list[one][2] == (four, 4)
    assert gr.adj_list[j][0] == (x, 0)
    assert gr.adj_list[j][1] == (x2, 0)
    assert gr.adj_list[j][2] == (two, 0)
    assert gr.adj_list[eigth][0] == (one_second, 1)
    assert gr.adj_list[eigth][1] == (three, 3)
    assert gr.adj_list[two][0] == (one, 1)
    assert gr.adj_list[two][1] == (three, 3)
    assert gr.adj_list[two][2] == (j, 0)
    assert gr.adj_list[two][3] == (one_second, 1)
    assert gr.adj_list[four][0] == (one_second, 1)
    assert gr.adj_list[four][1] == (one, 1)
    assert gr.adj_list[x2][0] == (j, 0)
    assert gr.adj_list[x2][1] == (three, 3)


def test_find_start_end():
    test_file_2 = StringIO("X14\nJ21\nX38")
    bp = BoardParser(test_file_2)
    gr = bp.create_graph()
    vertices = list(gr.adj_list.keys())
    start, end = bp.find_start_end()
    assert start == vertices[0]
    assert end == vertices[6]
