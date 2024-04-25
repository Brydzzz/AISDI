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
    bp = BoardParser(test_file_2)
    assert bp.has_above(src_row=1, src_col=0) is True


def test_board_parser_has_under_true():
    bp = BoardParser(test_file_2)
    assert bp.has_under(src_row=1, src_col=0) is True


def test_board_parser_has_left_true():
    bp = BoardParser(test_file_2)
    assert bp.has_left(src_row=1, src_col=1) is True


def test_board_parser_has_right_true():
    bp = BoardParser(test_file_2)
    assert bp.has_right(src_row=1, src_col=0) is True


def test_board_parser_has_above_false():
    bp = BoardParser(test_file_2)
    assert bp.has_above(src_row=0, src_col=0) is False


def test_board_parser_has_under_false():
    bp = BoardParser(test_file_2)
    assert bp.has_under(src_row=2, src_col=0) is False


def test_board_parser_has_left_false():
    bp = BoardParser(test_file_2)
    assert bp.has_left(src_row=1, src_col=0) is False


def test_board_parser_has_right_false():
    bp = BoardParser(test_file_2)
    assert bp.has_right(src_row=1, src_col=2) is False


def test_board_parser_get_weight_key_is_num():
    bp = BoardParser(test_file_2)
    v = bp.board[0][2]
    assert bp.get_weight(v) == 4


def test_board_parser_get_weight_key_is_joker():
    bp = BoardParser(test_file_2)
    v = bp.board[1][0]
    assert bp.get_weight(v) == 0


def test_board_parser_get_weight_key_is_X():
    bp = BoardParser(test_file_2)
    v = bp.board[0][0]
    assert bp.get_weight(v) == 0


def test_board_parser_graph():
    # TODO ładny test zrobić
    pass
