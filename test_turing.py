import pytest
from turing import Turing


def test_incorrect_inst():
    inst = "init 1 R init\n init 0 0 R init"
    tape = "00"
    with pytest.raises(ValueError):
        Turing(tape, inst.split("\n"))


def test_incorrect_inst_empty():
    inst = ""
    tape = "00"
    with pytest.raises(ValueError):
        Turing(tape, inst.split("\n"))


def test_add_one():
    tape = "1011"
    add_1_inst = (
        "init 1 1 R init\ninit 0 0 R init\ninit _ _ L carry\n"
        "carry 1 0 L carry\ncarry 0 1 * halt\ncarry _ 1 * halt"
    )
    add_1_inst_list = add_1_inst.split("\n")

    m = Turing(tape, add_1_inst_list)
    assert m.run() == "1100"


def test_add_one_result_tape_longer():
    tape = "1111"
    add_1_inst = (
        "init 1 1 R init\ninit 0 0 R init\ninit _ _ L carry\n"
        "carry 1 0 L carry\ncarry 0 1 * halt\ncarry _ 1 * halt"
    )
    add_1_inst_list = add_1_inst.split("\n")

    m = Turing(tape, add_1_inst_list)
    assert m.run() == "10000"


def test_3rd_a_to_z():
    inst = [
        "init A A R foundFirstA",
        "init _ _ * halt1",
        "init 0 0 R init",
        "init 1 1 R init",
        "foundFirstA A A R foundSecondA",
        "foundFirstA _ _ * halt2",
        "foundFirstA 0 0 R foundFirstA",
        "foundFirstA 1 1 R foundFirstA",
        "foundSecondA A Z R init",
        "foundSecondA _ _ * halt3",
        "foundSecondA 0 0 R foundSecondA",
        "foundSecondA 1 1 R foundSecondA",
    ]
    tape = "AAAAA000A1A1A011"
    m = Turing(tape, inst)
    assert m.run() == "AAZAA000Z1A1A011"
