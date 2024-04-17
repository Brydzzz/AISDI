class AVLNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.bf = 0


class AVLTree:

    def __init__(self, root=None, keys=None):
        self.root = root
        if keys:
            for element in keys:
                self.insert(element)

    def _updateBalanceFactor(self, node):
        if node.bf == -2 or node.bf == 2:
            self._rebalance(node)
            return

        if node.parent:
            if node == node.parent.left:
                node.parent.bf -= 1

            if node == node.parent.right:
                node.parent.bf += 1

            if node.parent.bf != 0:
                self._updateBalanceFactor(node.parent)

    def _rebalance(self, node):
        if node.bf > 0:  # node has more on the right side
            if node.right.bf < 0:  # node.right has more on the left side
                self.rightRotate(node.right)
                self.leftRotate(node)
            else:
                self.leftRotate(node)
        elif node.bf < 0:  # node has more on the left side
            if node.left.bf > 0:  # node.left has more on the right side
                self.leftRotate(node.left)
                self.rightRotate(node)
            else:
                self.rightRotate(node)

    def search(self, key) -> AVLNode:
        x = self.root
        while x and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    # rotate left at node x
    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x

        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

        x.bf = x.bf - 1 - max(0, y.bf)
        y.bf = y.bf - 1 + min(0, x.bf)

    # rotate right at node x
    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x

        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

        x.bf = x.bf + 1 - min(0, y.bf)
        y.bf = y.bf + 1 + max(0, x.bf)

    def insert(self, key):
        node = AVLNode(key)
        y = None
        x = self.root

        while x:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        # y is parent of x
        node.parent = y
        if not y:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        self._updateBalanceFactor(node)

    def display(
        self,
        right=False,
        node=None,
        indent=0,
    ):
        if not node:
            node = self.root
            print(f"\nroot: {node.key} bf:{node.bf}")
        elif right:
            print(f'{indent * " "}R:{node.key} bf:{node.bf}')
        else:
            print(f'{indent * " "}L:{node.key} bf:{node.bf}')
        indent += 4
        if node.left:
            self.display(False, node.left, indent)
        if node.right:
            self.display(True, node.right, indent)
        return
