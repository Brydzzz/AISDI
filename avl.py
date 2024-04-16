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

    def left_rotate(self, currentNode):
        if currentNode.right_child is not None:
            right = currentNode.right_child
            currentNode.right_child = right.left_child
            right.left_child = currentNode

    def right_rotate(self, currentNode):
        if currentNode.left_child is not None:
            left = currentNode.left_child
            currentNode.left_child = left.right_child
            left.right_child = currentNode

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
                    self.right_rotate(old.left)
                    self.left_rotate(old.left)
                else:  # RR
                    old.balance_factor = 0
                    z.balance_factor = 0
                    self.left_rotate(old)
        if z.balance_factor == 2:
            if z.left:
                if z.left.balance_factor == 1:  # LL
                    old.balance_factor = 0
                    z.balance_factor = 0
                    self.right_rotate(old)
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
                    self.left_rotate(old.right)
                    self.right_rotate(old.right)
