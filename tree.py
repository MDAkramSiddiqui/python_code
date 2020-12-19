from collections import defaultdict, deque


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


def print_tree(root, type="IN"):
    if type == "POST":
        print(print_tree_postorder(root, []))
    elif type == "IN":
        print(print_tree_inorder(root, []))


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


# problem 2
def reconstruct_tree(pre_order, in_order):
    if not (pre_order or in_order):
        return None

    if len(pre_order) == len(in_order) == 1:
        return TreeNode(pre_order[0])

    root = TreeNode(pre_order[0])
    root_index = in_order.index(pre_order[0])

    root.left = reconstruct_tree(pre_order[1:root_index + 1], in_order[0:root_index])
    root.right = reconstruct_tree(pre_order[1 + root_index:], in_order[root_index + 1:])

    return root


# problem 3
PLUS = "+"
MINUS = "-"
MULT = "*"
DIVIDE = "/"


def evaluate_arithematic_tree(root):
    if not root:
        return None

    if root.data == PLUS:
        return evaluate_arithematic_tree(root.left) + evaluate_arithematic_tree(root.right)
    elif root.data == MINUS:
        return evaluate_arithematic_tree(root.left) - evaluate_arithematic_tree(root.right)
    elif root.data == MULT:
        return evaluate_arithematic_tree(root.left) * evaluate_arithematic_tree(root.right)
    elif root.data == DIVIDE:
        return evaluate_arithematic_tree(root.left) / evaluate_arithematic_tree(root.right)
    else:
        return root.data


# problem 4
def min_sum_level(root, level, hash):
    if not root:
        return

    hash[level] += root.data
    _ = min_sum_level(root.left, level + 1, hash)
    _ = min_sum_level(root.right, level + 1, hash)

    return hash


def min_sum_level_2(root):
    if not root:
        return None

    queue = deque([])
    queue.append((root, 0))
    hash = defaultdict(int)

    while queue:
        node, level = queue.popleft()
        hash[level] += node.data

        if node.left:
            queue.append((node.left, level + 1))

        if node.right:
            queue.append((node.right, level + 1))

    # return min(hash, key=hash.get)
    return hash


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

    print("\n#####***** Solution 2 ******#####")
    pre_order = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
    in_order = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
    print(pre_order)
    print(in_order)
    print_tree(reconstruct_tree(pre_order, in_order), "POST")

    print("\n#####***** Solution 3 ******#####")
    node3 = TreeNode('+')
    node3.left = TreeNode('+')
    node3.right = TreeNode('-')
    node3.left.left = TreeNode(3)
    node3.left.right = TreeNode(2)
    node3.right.left = TreeNode(4)
    node3.right.right = TreeNode(5)
    print_tree(node3)
    print(evaluate_arithematic_tree(node3))

    print("\n#####***** Solution 4 ******#####")
    node4 = TreeNode(1)
    node4.left = TreeNode(2)
    node4.right = TreeNode(3)
    node4.right.left = TreeNode(4)
    node4.right.right = TreeNode(5)
    hash = defaultdict(int)
    hash = min_sum_level(node4, 0, hash)
    print_tree(node4)
    print(hash)
    print(min(hash.keys(), key=(lambda k: hash[k])))
    hash2 = min_sum_level_2(node4)
    print(hash2)
    print(min(hash2, key=hash2.get))
