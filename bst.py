class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BSTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, key) -> None:
        x = self.root
        y = None
        z = BSTNode(key)
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def search(self, key) -> BSTNode:
        x = self.root
        while x is not None and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def delete(self, key) -> None:
        pass

    def display(self):
        pass
