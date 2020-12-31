class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def print_tree_postorder(root, ans):
    if not root:
        return
    print_tree_postorder(root.left, ans)
    print_tree_postorder(root.right, ans)
    ans.append(root.data)
    return ans


def print_tree_inorder(root, ans):
    if not root:
        return
    print_tree_inorder(root.left, ans)
    ans.append(root.data)
    print_tree_inorder(root.right, ans)
    return ans

def print_tree_preorder(root, ans):
    if not root:
        return
    ans.append(root.data)
    print_tree_preorder(root.left, ans)
    print_tree_preorder(root.right, ans)
    return ans


def print_tree(root, type="IN"):
    if type == "POST":
        print(print_tree_postorder(root, []))
    elif type == "IN":
        print(print_tree_inorder(root, []))
    else:
        print(print_tree_preorder(root, []))


class BST:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert(self.root, data)

    def _insert(self, root, data):
        if data < root.data:
            if not root.left:
                root.left = TreeNode(data)
            else:
                self._insert(root.left, data)
        else:
            if not root.right:
                root.right = TreeNode(data)
            else:
                self._insert(root.right, data)

    def find(self, data):
        if not self.root:
            return False
        else:
            self._find(self.root, data)

    def _find(self, root, data):
        if not root:
            return False
        elif root.data == data:
            return True
        elif data < root.data:
            self._find(root.left, data)
        else:
            self._find(root.right, data)
