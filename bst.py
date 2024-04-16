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
        while x:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        if not y:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def find_closest(self, key) -> tuple[BSTNode, BSTNode]:
        x = self.root
        y = None
        while x and key != x.key:
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x, y

    def search(self, key) -> BSTNode:
        return self.find_closest(key)[0]

    def min_in_right(self, node) -> BSTNode:
        p = None
        temp = None
        temp = node.right
        while temp.left:
            p = temp
            temp = temp.left
        return temp, p

    def delete(self, key) -> None:
        if self.root is None:
            return self.root
        x, y = self.find_closest(key)
        if not x:
            return x
        if not x.left or not x.right:
            new_x = None
            if not x.left:
                new_x = x.right
            else:
                new_x = x.left
            if not y:
                return new_x
            if x == y.left:
                y.left = new_x
            else:
                y.right = new_x

            x = None
        else:
            temp, p = self.min_in_right(x)
            if p:
                p.left = temp.right
            else:
                x.right = temp.right
            x.key = temp.key
            temp = None
        return self.root

    def display(
        self,
        right=False,
        node=None,
        indent=0,
    ):
        if not node:
            node = self.root
            print(f"\nRoot:{node.key}")
        elif right:
            print(f'{indent * " "}R:{node.key}')
        else:
            print(f'{indent * " "}L:{node.key}')
        indent += 4
        if node.left:
            self.display(False, node.left, indent)
        if node.right:
            self.display(True, node.right, indent)
        return
