import heapq
from collections import defaultdict

from heap_utility import max_heapq


# "#####***** Problem 1 ******#####"
class FindMedian:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def find_median(self):
        if len(self.max_heap) > len(self.min_heap):
            median = -heapq.heappop(self.max_heap)
            heapq.heappush(self.max_heap, -median)
            return median

        elif len(self.min_heap) > len(self.max_heap):
            median = heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, median)
            return median

        else:
            val_1 = -heapq.heappop(self.max_heap)
            val_2 = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val_1)
            heapq.heappush(self.min_heap, val_2)
            return (val_1 + val_2) / 2

    def add(self, num):
        if len(self.max_heap) + len(self.min_heap) <= 1:
            heapq.heappush(self.max_heap, -num)
            return

        median = self.find_median()
        if num > median:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)

    def rebalance(self):
        if len(self.max_heap) > (len(self.min_heap) + 1):
            temp = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, temp)
        elif len(self.min_heap) > (len(self.max_heap) + 1):
            temp = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -temp)

    def driver(self, arr):
        for num in arr:
            self.add(num)
            # print(self.max_heap, self.min_heap)
            self.rebalance()
            print(self.find_median())


class FindMedian2:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def find_median(self):
        if len(self.max_heap) > len(self.min_heap):
            median = max_heapq.heappop(self.max_heap)
            max_heapq.heappush(self.max_heap, median)
            return median

        elif len(self.min_heap) > len(self.max_heap):
            median = heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, median)
            return median

        else:
            val_1 = max_heapq.heappop(self.max_heap)
            val_2 = heapq.heappop(self.min_heap)
            max_heapq.heappush(self.max_heap, val_1)
            heapq.heappush(self.min_heap, val_2)
            return (val_1 + val_2) / 2

    def add(self, num):
        if len(self.max_heap) + len(self.min_heap) <= 1:
            max_heapq.heappush(self.max_heap, num)
            return

        median = self.find_median()
        if num > median:
            heapq.heappush(self.min_heap, num)
        else:
            max_heapq.heappush(self.max_heap, num)

    def rebalance(self):
        if len(self.max_heap) > (len(self.min_heap) + 1):
            temp = max_heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, temp)
        elif len(self.min_heap) > (len(self.max_heap) + 1):
            temp = heapq.heappop(self.min_heap)
            max_heapq.heappush(self.max_heap, temp)

    def driver(self, arr):
        for num in arr:
            self.add(num)
            # print(self.max_heap, self.min_heap)
            self.rebalance()
            print(self.find_median())

# Problem 2
def compute_similarity(a, b, visitors):
    return len(visitors[a] & visitors[b]) / len(visitors[a] | visitors[b])

def top_pairs(log, k):
    visitors = defaultdict(set)
    for site, user in log:
        visitors[site].add(user)

    pairs = []
    sites = list(visitors.keys())

    for i in range(k):
        heapq.heappush(pairs, (0, ("", "")))

    for i in range(len(sites)-1):
        for j in range(i+1, len(sites)-1):
            score = compute_similarity(sites[i], sites[j], visitors)
            heapq.heappushpop(pairs, (score, (sites[i], sites[j])))

    return [pair[1] for pair in pairs]

if __name__ == "__main__":
    print("\n#####***** Solution 1 - A ******#####")
    arr1 = [2, 1, 5, 7, 2, 0, 5]
    sol1 = FindMedian()
    sol1.driver(arr1)

    # using my own max_heap function for numeric values in a list
    print("\n#####***** Solution 1 - B ******#####")
    arr2 = [2, 1, 5, 7, 2, 0, 5]
    sol2 = FindMedian2()
    sol2.driver(arr2)
    # val = []
    # for num in arr2:
    #     max_heapq.heappush(val, num)
    #     print(val)
    #
    # for i in range(len(val)):
    #     max_heapq.heappop(val)
    #     print(val)

    print("\n#####***** Solution 2 ******#####")
    log = [
        ('a.com', 1), ('a.com', 3), ('a.com', 5), ('a.com', 6),
        ('b.com', 1), ('b.com', 3), ('b.com', 5), ('c.com', 1),
        ('d.com', 2), ('d.com', 7), ('e.com', 2), ('e.com', 6)
    ]

    print(top_pairs(log, 1))


