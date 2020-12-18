class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# problem 1
def unival_tree(node):
    _, count = unival_tree_helper(node)
    return count


def unival_tree_helper(node):
    print("----{}----".format(node.data)) if node else None
    if not node:
        return True, 0

    left_bool, count_left = unival_tree_helper(node.left)
    right_bool, count_right = unival_tree_helper(node.right)

    if left_bool and right_bool:
        node_left = node.left.data == node.data if node.left else True
        node_right = node.right.data == node.data if node.right else True
        if node_right and node_left:
            return True, count_right + count_left + 1
        else:
            return False, count_right + count_left
    else:
        return False, count_right + count_left


if __name__ == "__main__":
    print("\n#####***** Solution 1 ******#####")
    node = TreeNode(0)
    node.left = TreeNode(1)
    node.right = TreeNode(0)
    node.right.right = TreeNode(0)
    node.right.left = TreeNode(1)
    node.right.left.left = TreeNode(1)
    node.right.left.right = TreeNode(1)
    print(unival_tree(node))

    node2 = TreeNode('a')
    node2.left = TreeNode('a')
    node2.right = TreeNode('a')
    node2.right.right = TreeNode('a')
    node2.right.left = TreeNode('a')
    node2.right.right.right = TreeNode('b')
    print(unival_tree(node2))
