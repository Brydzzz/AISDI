from bst import BSTNode, BSTree


def test_bst_insert_simple():
    node2 = BSTNode(2)
    bs = BSTree(node2)
    bs.insert(1)
    bs.insert(3)
    assert bs.root.left.key == 1
    assert bs.root.right.key == 3


def test_bst_insert_less_simple():
    node2 = BSTNode(2)
    bs = BSTree(node2)
    bs.insert(1)
    bs.insert(3)
    bs.insert(6)
    bs.insert(2)
    bs.insert(-1)
    assert bs.root.right.right.key == 6
    assert bs.root.right.left.key == 2
    assert bs.root.left.left.key == -1


def test_bst_search_simple1():
    node2 = BSTNode(2)
    bs = BSTree(node2)
    bs.insert(1)
    bs.insert(3)
    bs.insert(6)
    bs.insert(2)
    bs.insert(-1)
    assert bs.search(6) == bs.root.right.right


def test_bst_search_simple2():
    node2 = BSTNode(2)
    bs = BSTree(node2)
    bs.insert(1)
    bs.insert(3)
    bs.insert(6)
    bs.insert(2)
    bs.insert(-1)
    assert bs.search(-1) == bs.root.left.left
