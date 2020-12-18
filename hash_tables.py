import linked_list_utility


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


if __name__ == "__main__":
    # problem 1
    lru_cache = LRUCache()
    lru_cache.set(1,2)
    lru_cache.set(2,22)
    lru_cache.get(1)
    lru_cache.get(44)
    lru_cache.set(2,33)

