from avl import AVLNode, AVLTree


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


# def test_balance_factor2():
#     node3 = AVLNode(10)
#     av = AVLTree(node3, [5, 15, 14, 13, 13.5])
#     # balance factor of 14
#     assert node3.right.left.balance_factor == 2


# def test_balance_factor3():
#     node3 = AVLNode(10)
#     av = AVLTree(node3, [5, 15, 14, 13, 13.5])
#     av.insert(14.5)
#     # balance factor of 14
#     assert node3.right.left.balance_factor == 1


# def test_balance_factor4():
#     node3 = AVLNode(10)
#     av = AVLTree(node3, [5, 15, 14, 13, 13.5])
#     av.insert(14.5)
#     av.insert(14.75)
#     # balance factor of 14
#     assert node3.right.left.balance_factor == 0


# def test_balance_factor5():
#     node3 = AVLNode(10)
#     av = AVLTree(node3, [5, 15, 14, 13])
#     # balance factor of 14
#     assert node3.right.balance_factor == 2
