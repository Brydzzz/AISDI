class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BSTree:
    def __init__(self, root=None, list=None):
        self.root = root
        if list:
            for element in list:
                self.insert(element)

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
        y = None
        while x is not None and key != x.key:
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x, y

    def delete(self, key) -> None:
        if self.root is None:
            return self.root
        x, y = self.search(key)
        if not x:
            return x
        if not x.left or not x.right:
            new_x = None
            if x.left is None:
                new_x = x.right
            else:
                new_x = x.left
            if y is None:
                return new_x
            if x == y.left:
                y.left = new_x
            else:
                y.right = new_x

            x = None
        else:
            p = None
            temp = None
            temp = x.right
            while temp.left is not None:
                p = temp
                temp = temp.left
            if p is not None:
                p.left = temp.right
            else:
                x.right = temp.right
            x.key = temp.key
            temp = None
        return self.root

    def display(self):
        pass
