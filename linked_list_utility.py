import random
import math
import time


# *** DOUBLE LINKED LIST ***
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


def print_link_list(node, is_dict=False):
    node_data = []
    if not is_dict:
        while node:
            node_data.append(node.data)
            node = node.next
        print(node_data)
    else:
        while node:
            if node.key:
                dict = {node.key: node.val}
                node_data.append(dict)
            node = node.next
        print(node_data)


def generate_random_link_list():
    node = None
    random.seed(time.time())
    n = 0
    while not n:
        n = math.floor(random.random() * 10)

    node = Node(math.floor(random.random() * 10), None, None)
    root_node = node
    while n > 0:
        new_node = Node(math.floor(random.random() * 10), None, None)
        node.next = new_node
        node = node.next
        n -= 1

    return root_node


def link_list_length(node):
    if not node:
        return 0
    return 1 + link_list_length(node.next)


def attach_random(a, b):
    while not a.next:
        a = a.next

    b_len = link_list_length(b)
    random.seed(time.time())
    n = math.floor(random.random() * b_len - 1)

    while n > 0:
        b = b.next
        n -= 1

    a.next = b

    return a
