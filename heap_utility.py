# Max heap for numeric values
class MaxHeap:
    def parent(self, pos):
        return pos // 2

    def left_child(self, pos):
        return pos * 2

    def right_child(self, pos):
        return pos * 2 + 1

    def swap(self, arr, pos_1, pos_2):
        arr[pos_1], arr[pos_2] = arr[pos_2], arr[pos_1]

    def is_leaf(self, arr, pos):
        if len(arr)//2 <= pos <= len(arr):
            return True
        return False

    def heappush(self, arr, val):
        arr.append(val)
        current = len(arr)-1

        while arr[current] > arr[self.parent(current)]:
            self.swap(arr, current, self.parent(current))
            current = self.parent(current)

    def heappop(self, arr):
        n = len(arr)
        root = arr[0]
        arr[0] = arr[n-1]
        arr.pop()

        self.heapify(arr, 0)
        return root

    def heapify(self, arr, current):
        if self.is_leaf(arr, current):
            return

        max_index = current

        if arr[self.left_child(current)] > arr[max_index]:
            max_index = self.left_child(current)
        if arr[self.right_child(current) > arr[max_index]]:
            max_index = self.right_child(current)

        if max_index != current:
            self.swap(arr, current, max_index)
            self.heapify(arr, max_index)

max_heapq = MaxHeap()