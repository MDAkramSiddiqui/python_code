import linked_list_utility


# Problem 1
def reverse_link_list_recursive(node):
    head, _ = _reverse_handler(node)
    return head


def _reverse_handler(node):
    if node == None:
        return None, None

    if node.next == None:
        return node, node

    head, tail = _reverse_handler(node.next)
    node.next = None
    tail.next = node
    # since node is the new tail
    return head, node


def reverse_link_list(head):
    current, prev = head, None
    while current is not None:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp
    return prev


# problem 2
def add_two_node(node1, node2, carry=0):
    if not node1 and not node2 and not carry:
        return None

    node1_val = node1.data if node1 else 0
    node2_val = node2.data if node2 else 0
    total = node1_val + node2_val + carry

    node1_next = node1.next if node1 else None
    node2_next = node2.next if node2 else None
    carry_next = 1 if total >= 10 else 0

    return linked_list_utility.Node(total % 10, add_two_node(node1_next, node2_next, carry_next))


# problem 3
def rearrange_high_low_pattern_1(node):
    if not node:
        return None

    curr = node
    even = True
    while curr.next:
        if curr.data > curr.next.data and even:
            curr.data, curr.next.data = curr.next.data, curr.data

        if curr.data < curr.next.data and not even:
            curr.data, curr.next.data = curr.next.data, curr.data

        even = not even
        curr = curr.next

    return node


def rearrange_high_low_pattern_2(node):
    if not node:
        return None

    prev, curr = node, node.next
    while curr:
        if prev.data > curr.data:
            prev.data, curr.data = curr.data, prev.data

        if not curr.next:
            break

        if curr.data < curr.next.data:
            curr.data, curr.next.data = curr.next.data, curr.data

        prev = curr.next
        curr = curr.next.next

    return node


# problem 4
def find_intersecting_node(node1, node2):
    m = linked_list_utility.link_list_length(node1)
    n = linked_list_utility.link_list_length(node2)

    if m > n:
        for _ in range(m - n):
            node1 = node1.next

    if m < n:
        for _ in range(n - m):
            node2 = node2.next

    while (node1 != node2):
        node1 = node1.next
        node2 = node2.next

    return node1


if __name__ == "__main__":
    # problem 1
    root_node1 = linked_list_utility.generate_random_link_list()
    root_node2 = linked_list_utility.generate_random_link_list()
    print('\n######## Solution 1 ###########')
    linked_list_utility.print_link_list(root_node1)
    linked_list_utility.print_link_list(root_node2)
    root_node1 = reverse_link_list_recursive(root_node1)
    root_node2 = reverse_link_list(root_node2)
    linked_list_utility.print_link_list(root_node1)
    linked_list_utility.print_link_list(root_node2)

    # problem 2
    root_node1 = linked_list_utility.generate_random_link_list()
    root_node2 = linked_list_utility.generate_random_link_list()
    print('\n######## Solution 2 ###########')
    linked_list_utility.print_link_list(root_node1)
    linked_list_utility.print_link_list(root_node2)
    root_node = add_two_node(root_node1, root_node2)
    linked_list_utility.print_link_list(root_node)

    # problem 3
    root_node1 = linked_list_utility.generate_random_link_list()
    root_node2 = linked_list_utility.generate_random_link_list()
    print('\n######## Solution 3 ###########')
    linked_list_utility.print_link_list(root_node1)
    linked_list_utility.print_link_list(root_node2)
    root_node1 = rearrange_high_low_pattern_1(root_node1)
    root_node2 = rearrange_high_low_pattern_2(root_node2)
    linked_list_utility.print_link_list(root_node1)
    linked_list_utility.print_link_list(root_node2)

    # problem 4
    root_node1 = linked_list_utility.generate_random_link_list()
    root_node2 = linked_list_utility.generate_random_link_list()
    root_node2 = linked_list_utility.attach_random(root_node2, root_node1)
    print('\n######## Solution 4 ###########')
    linked_list_utility.print_link_list(root_node1)
    linked_list_utility.print_link_list(root_node2)
    common_node = find_intersecting_node(root_node1, root_node2)
    print(common_node.data)
