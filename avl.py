class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.balance_factor: int = 0


class AVLTree:
    def __init__(self, root=None, list=None):
        self.root = root
        if list:
            for element in list:
                self.insert(element)

    def add_node(self, key) -> AVLNode:
        x = self.root
        y = None
        z = AVLNode(key)
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
        z.parent = y
        return z

    def left_rotate(self, root, pivot):
        # right = currentNode.right
        # z = right.left
        # currentNode.right = z
        # if z is not None:
        #     z.parent = currentNode
        # if right:
        #     right.left = currentNode
        # if currentNode.parent is None:
        #     self.root = right
        # currentNode.parent = right
        # # right = currentNode.right
        # # if currentNode.parent == None:
        # #     self.root = right
        # # currentNode.right = right.left
        # # right.left = currentNode
        if not root.parent:
            self.root = pivot
            pivot.parent = None
        else:
            if root.parent.right == root:
                root.parent.right = pivot
            else:
                root.parent.left = pivot
        root.parent = pivot
        root.right = pivot.right
        pivot.left = root

    def right_rotate(self, root, pivot):
        if not root.parent:
            self.root = pivot
            pivot.parent = None
        else:
            if root.parent.right == root:
                root.parent.right = pivot
            else:
                root.parent.left = pivot
        root.parent = pivot
        root.left = pivot.right
        pivot.right = root

        # left = currentNode.left
        # if currentNode.parent == None:
        #     self.root = left
        # currentNode.left = left.right
        # left.right = currentNode
        # left = currentNode.left
        # z = currentNode.right
        # currentNode.left = z
        # if z is not None:
        #     z.parent = currentNode
        # if left:
        #     left.right = currentNode
        # if currentNode.parent is None:
        #     self.root = left
        # currentNode.parent = left

    def insert(self, key):
        z = self.add_node(key)
        old = z
        z = z.parent
        # if z.parent.right == z:
        #     z.parent.balance_factor -= 1
        # else:
        #     z.parent.balance_factor += 1
        # z = z.parent.parent
        # while z:
        #     if z.right == old:
        #         if z.right.balance_factor != 0:
        #             z.balance_factor -= 1
        #             old = z
        #     if z.left == old:
        #         if z.left.balance_factor != 0:
        #             z.balance_factor += 1
        #             old = z
        #     z = z.parent
        while z:
            if z.right == old:
                z.balance_factor -= 1
            if z.left == old:
                z.balance_factor += 1

            if (
                z.balance_factor == 0
                or z.balance_factor == 2
                or z.balance_factor == -2
                or z == self.root
            ):
                break
            old = z
            z = z.parent
        if z.balance_factor == -2:
            if z.right:
                if z.right.balance_factor == 1:  # RL
                    if old.left.balance_factor == 0:
                        z.balance_factor = 0
                        old.balance_factor = 0
                    elif old.left.balance_factor > 0:
                        z.balance_factor = 0
                        old.balance_factor = -1
                    else:
                        z.balance_factor = 1
                        old.balance_factor = 0
                    old.left.balance_factor = 0
                    older = old.left
                    self.right_rotate(old, older)
                    self.left_rotate(z, older)
                else:  # RR
                    old.balance_factor = 0
                    z.balance_factor = 0
                    self.left_rotate(z, old)
        if z.balance_factor == 2:
            if z.left:
                if z.left.balance_factor == 1:  # LL
                    old.balance_factor = 0
                    z.balance_factor = 0
                    self.right_rotate(z, old)
                else:  # LR
                    if old.right.balance_factor == 0:
                        z.balance_factor = 0
                        old.balance_factor = 0
                    elif old.right.balance_factor > 0:
                        z.balance_factor = -1
                        old.balance_factor = 0
                    else:
                        z.balance_Factor = 0
                        old.balance_factor = 1
                    old.right.balance_factor = 0
                    older = old.right
                    self.left_rotate(old, older)
                    self.right_rotate(z, older)

    def search(self, key):
        x = self.root
        while x is not None and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def display(
        self,
        right=False,
        node=None,
        indent=0,
    ):
        if not node:
            node = self.root
            print(f"{node.key}{node.balance_factor}")
        elif right:
            print(f'{indent * " "}R:{node.key} bf:{node.balance_factor}')
        else:
            print(f'{indent * " "}L:{node.key} bf:{node.balance_factor}')
        indent += 4
        if node.left:
            self.display(False, node.left, indent)
        if node.right:
            self.display(True, node.right, indent)
        return
