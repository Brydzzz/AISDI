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


def test_operations_outside_left():
    inst = [
        "init 1 1 L init",
        "init 0 0 L init",
        "init _ _ L out1",
        "out1 _ 1 * halt",
    ]
    tape = "11001"
    m = Turing(tape, inst)
    print("\n")
    s = m.run()
    assert s == "1 11001"


def test_operations_outside_right():
    inst = [
        "init 1 1 R init",
        "init 0 0 R init",
        "init _ _ R out1",
        "out1 _ 1 * halt",
    ]
    tape = "10001"
    m = Turing(tape, inst)
    print("\n")
    s = m.run()
    assert s == "10001 1"


def test_operations_add():
    inst = [
        "init 0 0 R init",
        "init 1 1 R init",
        "init _ _ R one",
        "one 0 0 R one",
        "one 1 1 R one",
        "one _ _ L two",
        "two 0 1 L two",
        "two 1 0 L three",
        "two _ _ R five",
        "three 0 0 L three",
        "three 1 1 L three",
        "three _ _ L four",
        "four 0 1 R init",
        "four 1 0 L four",
        "four _ 1 R init",
        "five 1 _ R five",
        "five _ _ * halt",
    ]
    tape = "1010 111"
    m = Turing(tape, inst)
    print("\n")
    s = m.run()
    assert s == "10001"


def test_indeterminate():
    # if states repeat it should take the last instruction
    inst = ["init 0 1 R init", "init 0 0 R init", "init 1 1 * halt"]
    tape = "00001000"
    m = Turing(tape, inst)
    print("\n")
    s = m.run()
    assert s == "00001000"
