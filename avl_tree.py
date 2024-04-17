class AVLNode:
    def __init__(self, key):
        self.key = key
        self.parent: AVLNode = None
        self.left: AVLNode = None
        self.right: AVLNode = None
        self.bf: int = 0


class AVLTree:

    def __init__(self, root: AVLNode = None, keys=None):
        self.root = root
        if keys:
            for element in keys:
                self.insert(element)

    def _updateBalanceFactor(self, node: AVLNode) -> None:
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

    def _rebalance(self, node: AVLNode) -> None:
        if node.bf > 0:  # node has more on the right side
            if node.right.bf < 0:  # node.right has more on the left side
                pivot = node.right
                sec = pivot.left
                self.rightRotate(node.right)
                self.leftRotate(node)
                if sec.bf == -1:
                    node.bf = 0
                    pivot.bf = 1
                    sec.bf = 0
                elif sec.bf == 1:
                    node.bf = -1
                    pivot.bf = 0
                    sec.bf = 0
                else:
                    node.bf = 0
                    pivot.bf = 0
                    sec.bf = 0
            else:
                pivot = node.right
                self.leftRotate(node)
                pivot.bf = 0
                node.bf = 1

        elif node.bf < 0:  # node has more on the left side
            if node.left.bf > 0:  # node.left has more on the right side
                pivot = node.left
                sec = pivot.right
                self.leftRotate(node.left)
                self.rightRotate(node)
                if sec.bf == -1:
                    node.bf = 1
                    pivot.bf = 0
                    sec.bf = 0
                elif sec.bf == -1:
                    node.bf = 0
                    pivot.bf = -1
                    sec.bf = 0
                else:
                    node.bf = 0
                    pivot.bf = 0
                    sec.bf = 0
            else:
                pivot = node.left
                self.rightRotate(node)
                node.bf = 0
                pivot.bf = 0

    def search(self, key) -> AVLNode:
        x = self.root
        while x and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    # rotate left at node x
    def leftRotate(self, x: AVLNode) -> None:
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

    # rotate right at node x
    def rightRotate(self, x: AVLNode) -> None:
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

    def insert(self, key) -> None:
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
        right: bool = False,
        node: AVLNode = None,
        indent=0,
    ) -> None:
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
