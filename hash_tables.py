import linked_list_utility
import stack_and_queue_utitlity
from collections import defaultdict


# problem 1
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = Node(None, 'head')
        self.tail = Node(None, 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head

    def get_head(self):
        return self.head.next

    def get_tail(self):
        return self.tail.prev

    def add(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.next = self.tail
        node.prev = prev_node
        self.tail.prev = node

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node


class LRUCache:
    def __init__(self, max_size=10):
        self.max_size = max_size
        self.dict = {}
        self.list = LinkedList()

    def set(self, key, val):

        if key in self.dict:
            node = self.dict[key]
            node.val = val
        else:
            new_node = Node(key, val)
            self.list.add(new_node)
            self.dict[key] = new_node

        if len(self.dict) > self.max_size:
            del_node = self.list.get_head()
            del self.dict[del_node.key]
            self.list.remove(del_node)

        self.print()

    def get(self, key):
        if key in self.dict:
            node = self.dict[key]
            self.list.remove(node)
            self.list.add(node)
            return node.val
        self.print()
        return None

    def print(self):
        linked_list_utility.print_link_list(self.list.get_head(), True)


# problem 2
def min_cuts(wall):
    hash = defaultdict(int)

    for row in wall:
        length = 0
        for size in row[:-1]:
            length += size
            hash[length] += 1

    return len(wall) - max(hash.values())


# problem 3
class SparseArray:
    def __init__(self, arr, max_size):
        self.__hash = {}
        self.__max_size = max_size
        for i, e in enumerate(arr):
            if e != 0:
                self.__hash[i] = e
        print("INIT:", self.__hash)

    def get(self, i):
        if i in self.__hash:
            print("GET:", self.__hash)
            return self.__hash.get(i, 0)
        print("GET:", self.__hash)
        return 0

    def set(self, i, val):
        self.__check_bounds(i)
        if val != 0:
            self.__hash[i] = val
        elif i in self.__hash:
            del self.__hash[i]
        print("SET:", self.__hash)
        return

    def __check_bounds(self, i):
        if i < 0 or i > self.__max_size:
            raise IndexError('Out of bounds')


if __name__ == "__main__":
    print("\n#####***** Solution 1 ******#####")
    lru_cache = LRUCache()
    lru_cache.set(1, 2)
    lru_cache.set(2, 22)
    lru_cache.get(1)
    lru_cache.get(44)
    lru_cache.set(2, 33)

    print("\n#####***** Solution 2 ******#####")
    fixed_arr = [[3, 5, 1, 1], [5, 5], [2, 3, 3, 2], [4, 4, 2], [1, 3, 3, 3], [1, 1, 6, 1, 1]]
    print(fixed_arr)
    print(min_cuts(fixed_arr))

    print("\n#####***** Solution 3 ******#####")
    sparse_arr = stack_and_queue_utitlity.get_sparse_array()
    print(sparse_arr)
    sparse_obj = SparseArray(sparse_arr, 1000)
    print(sparse_obj.get(33))
    sparse_obj.set(57, 0)
