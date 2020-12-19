class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def insert(self, x):
        if not self.root:
            self.root = TreeNode(x)
        else:
            self._insert(x, self.root)

    def _insert(self, x, root):
        if x < root.data:
            if not root.left:
                root.left = TreeNode(x)
            else:
                self._insert(x, root.left)
        else:
            if not root.right:
                root.right = TreeNode(x)
            else:
                self._insert(x, root.right)

    def find(self, x):
        if not self.root:
            return False
        else:
            return self._find(x, self.root)

    def _find(self, x, root):
        if not root:
            return False

        if x == root.data:
            return True
        elif x < root.data:
            return self._find(x, root.left)
        else:
            return self._find(x, root.right)


if __name__ == "__main__":
    pass
