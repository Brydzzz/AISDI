from avl import AVLNode, AVLTree


def check_tree(node):
    if node.left:
        if node.left.key >= node.key or node.balance_factor not in [0, 1, -1]:
            return False
    if node.right:
        if node.right.key < node.key or node.balance_factor not in [0, 1, -1]:
            return False
    if node.left:
        check_tree(node.left)
    if node.right:
        check_tree(node.right)
    return True


def test_insert_rotate_left_simple():
    node3 = AVLNode(3)
    av = AVLTree(node3, [4, 5])
    assert av.root.key == 4


def test_insert_rotate_right_simple():
    node3 = AVLNode(3)
    av = AVLTree(node3, [2, 1])
    assert av.root.key == 2


def test_insert_rotate_right_left():
    node = AVLNode(7)
    av = AVLTree(node, [10, 8])
    assert av.root.key == 8


def test_insert_rotate_left_right():
    node = AVLNode(7)
    av = AVLTree(node, [5, 6])
    assert av.root.key == 6


def test_avl_tree_search():
    node3 = AVLNode(10)
    av = AVLTree(node3, [5, 15])
    av.insert(14)
    av.insert(13)
    assert check_tree(node3) is True
    assert av.search(13)


def test_avl_tree_display():
    node3 = AVLNode(10)
    av = AVLTree(node3, [5, 15, 14, 13])
    assert check_tree(node3) is True
    av.display()


def test_avl_tree_display2():
    node3 = AVLNode(5)
    av = AVLTree(
        node3,
        [1, 20, 15, 25, 24, 23, 22, 23.5, 24.5, 24.25, 24.1, 24.6, 24.15],
    )
    assert check_tree(node3) is True
    av.display()
