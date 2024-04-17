from bst import BSTNode, BSTree


def check_tree(node):
    if node.left:
        if node.left.key >= node.key:
            return False
    if node.right:
        if node.right.key < node.key:
            return False
    if node.left:
        check_tree(node.left)
    if node.right:
        check_tree(node.right)
    return True


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


def test_bst_insert_less_simple2():
    node2 = BSTNode(2)
    bs = BSTree(node2)
    bs.insert(1)
    bs.insert(3)
    bs.insert(6)
    bs.insert(2)
    bs.insert(-1)
    assert check_tree(node2) is True


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


def test_bst_search_no_element():
    node2 = BSTNode(2)
    bs = BSTree(node2)
    bs.insert(1)
    bs.insert(3)
    bs.insert(6)
    bs.insert(2)
    bs.insert(-1)
    assert bs.search(-7) is None


def test_delete_bst_leaf():
    node5 = BSTNode(5)
    bs = BSTree(node5)
    bs.insert(3)
    bs.insert(7)
    bs.insert(2)
    bs.insert(4)
    bs.insert(6)
    bs.insert(8)
    bs.delete(8)
    assert bs.root.right.right is None
    assert check_tree(node5) is True


def test_delete_bst_one_son():
    node5 = BSTNode(5)
    bs = BSTree(node5)
    bs.insert(3)
    bs.insert(7)
    bs.insert(2)
    bs.insert(4)
    bs.insert(6)
    bs.insert(8)
    bs.insert(10)
    bs.delete(8)
    assert bs.root.right.right.right is None
    assert check_tree(node5) is True


def test_delete_bst_two_sons():
    node5 = BSTNode(5)
    bs = BSTree(node5)
    bs.insert(3)
    bs.insert(7)
    bs.insert(2)
    bs.insert(4)
    bs.insert(6)
    bs.insert(8)
    bs.insert(10)
    bs.insert(9)
    bs.insert(11)
    bs.delete(10)
    assert check_tree(node5) is True


def test_delete_bst_two_sons2():
    node5 = BSTNode(5)
    bs = BSTree(
        node5, [1, 20, 15, 25, 24, 23, 22, 23.5, 24.5, 24.25, 24.1, 24.6]
    )
    bs.delete(24)
    assert check_tree(node5) is True


def test_delete_bst_two_sons3():
    node5 = BSTNode(5)
    bs = BSTree(
        node5,
        [1, 20, 15, 25, 24, 23, 22, 23.5, 24.5, 24.25, 24.1, 24.6, 24.15],
    )
    bs.delete(24)
    assert check_tree(node5) is True


def test_display():
    node5 = BSTNode(5)
    bs = BSTree(
        node5,
        [1, 20, 15, 25, 24, 23, 22, 23.5, 24.5, 24.25, 24.1, 24.6, 24.15],
    )
    bs.display()
