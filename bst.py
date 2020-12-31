import bst_utility

# problem 1
def get_bounds(root, val, floor=None, ciel=None):
    if not root:
        return floor, ciel

    if val == root.data:
        return root.data, root.data
    elif val < root.data:
        floor, ciel = get_bounds(root.left, val, floor, root.data)
    elif val > root.data:
        floor, ciel = get_bounds(root.right, val, root.data, ciel)
    return floor, ciel


# problem 2
def make_bst(arr):
    if not len(arr):
        return None

    mid = len(arr) // 2

    root = bst_utility.TreeNode(arr[mid])
    root.left = make_bst(arr[:mid])
    root.right = make_bst(arr[mid+1:])

    return root

# problem 3
def make_trees(low, high):
    trees = []
    if low > high:
        trees.append(None)
        return trees

    for i in range(low, high+1):
        left = make_trees(low, i-1)
        right = make_trees(i+1, high)

        for l in left:
            for r in right:
                node = bst_utility.TreeNode(i, left=l, right=r)
                trees.append(node)

    return trees


if __name__ == "__main__":
    print("\n#####***** Solution 1 ******#####")
    bst_tree = bst_utility.BST()
    bst_tree.insert(20)
    bst_tree.insert(5)
    bst_tree.insert(30)
    bst_tree.insert(55)
    bst_tree.insert(23)
    bst_tree.insert(1)
    bst_tree.insert(10)
    bst_utility.print_tree(bst_tree.get_root())
    print(get_bounds(bst_tree.get_root(), 9));

    print("\n#####***** Solution 2 ******#####")
    sorted_arr = [1, 5, 10, 20, 23, 30, 55];
    bst_utility.print_tree(make_bst(sorted_arr), "PRE")

    print("\n#####***** Solution 3 ******#####")
    all_possible_trees = make_trees(1, 4)
    for tree in all_possible_trees:
        bst_utility.print_tree(tree, "PRE")
