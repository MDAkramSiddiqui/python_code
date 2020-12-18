import stack_and_queue_utitlity
from collections import deque


# problem 1
class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxes = []

    def push(self, x):
        self.stack.append(x)
        if self.maxes:
            self.maxes.append(max(x, self.maxes[-1]))
        else:
            self.maxes.append(x)

    def pop(self):
        if self.maxes:
            self.maxes.pop()
        return self.stack.pop()

    def max_val(self):
        if not maxes:
            return -1
        else:
            return self.maxes[-1]


# problem 2
def check_balanced_paran(val):
    stack = []
    for char in val:
        if char in ["(", "[", "{"]:
            stack.append(char)
        else:
            # in python empty list is also considered to be false value
            if not stack:
                return False
            if (char == ')' and stack[-1] != '(') or \
                    (char == ']' and stack[-1] != '[') or \
                    (char == '}' and stack[-1] != '{'):
                return False
            stack.pop()

    return len(stack) == 0


# Problem 3
def max_of_subarrays_1(arr, k):
    ans = []
    for i in range(len(arr) - k + 1):
        ans.append(max(arr[i:i + k]))
    return ans


def max_of_subarrays_2(arr, k):
    ans = []
    q = deque()
    for i in range(k):
        while q and arr[i] >= arr[q[-1]]:
            q.pop()
        q.append(i)

    for i in range(k, len(arr)):
        ans.append(arr[q[0]])
        # checking indices of the val stored in que and then removing
        while q and q[0] <= i - k:
            q.popleft()
        while q and arr[i] >= arr[q[-1]]:
            q.pop()
        q.append(i)
    ans.append(arr[q[0]])
    return ans


def reconstruct_array(arr):
    ans = []
    n = len(arr) - 1
    stack = []

    for i in range(n):
        if arr[i + 1] == "-":
            stack.append(i)
        else:
            ans.append(i)
            while stack:
                ans.append(stack.pop())
    stack.append(n)
    while stack:
        ans.append(stack.pop())
    return ans


if __name__ == "__main__":
    # problem 1
    print("\n#####***** Solution 1 ******#####")
    max_stack = MaxStack()
    maxes = []
    for i in (stack_and_queue_utitlity.get_random_array(10)):
        max_stack.push(i)
        maxes.append(max_stack.max_val())
    max_stack.pop()
    print(maxes)
    maxes.append(max_stack.max_val())
    print(maxes)

    print("\n#####***** Solution 2 ******#####")
    par1 = '([])[]({})'
    par2 = '[(])'
    print(par1, par2)
    print(check_balanced_paran(par1))
    print(check_balanced_paran(par2))

    print("\n#####***** Solution 3 ******#####")
    arr = stack_and_queue_utitlity.get_random_array()
    print(arr)
    print(max_of_subarrays_1(arr, 3))
    print(max_of_subarrays_2(arr, 3))

    print("\n#####***** Solution 4 ******#####")
    arr = [None, "+", "+", "-", "+"]
    arr2 = [None, "+", "-", "-", "-"]
    print(arr, arr2)
    print(reconstruct_array(arr))
    print(reconstruct_array(arr2))
