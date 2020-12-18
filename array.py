# ********** problem 4 ************ #
import bisect


# ********** problem 4 ************ #

# problem 1
def products(num_arr):
    if len(num_arr) == 0:
        return

    _prefix_arr, _suffix_arr = [], []
    # Generate prefix products
    for num in num_arr:
        if _prefix_arr:
            _prefix_arr.append(_prefix_arr[-1] * num)
        else:
            _prefix_arr.append(num)

    # Generate suffi products
    for num in reversed(num_arr):
        if _suffix_arr:
            _suffix_arr.append(_suffix_arr[-1] * num)
        else:
            _suffix_arr.append(num)

    results_arr = []
    for i in range(len(num_arr)):
        if i == 0:
            results_arr.append(_prefix_arr[i])
        elif i == len(num_arr) - 1:
            results_arr.append(_suffix_arr[i])
        else:
            results_arr.append(_prefix_arr[i - 1] * _suffix_arr[i + 1])

    return results_arr


# problem 2
def smallest_unsorted_window(num_arr):
    left, right = None, None
    n = len(num_arr)
    max_seen, min_seen = -float('inf'), float('inf')

    for i in range(n):
        max_seen = max(num_arr[i], max_seen)
        if num_arr[i] < max_seen:
            right = i

    for i in range(n - 1, -1, -1):
        min_seen = min(num_arr[i], min_seen)
        if num_arr[i] > min_seen:
            left = i

    return left, right


# problem 3
def calculate_max_subarray_sum(num_arr):
    # current_max = -float('inf')
    # for i in range(len(num_arr)-1):
    #   for j in range(i, len(num_arr)):
    #     current_max = max(current_max, sum(num_arr[i:j+1]))
    # return current_max
    max_till_now = max_ever = 0
    for num in num_arr:
        max_till_now = max(num, num + max_till_now)
        max_ever = max(max_ever, max_till_now)
    return max_ever


def calculate_min_subarray_sum(num_arr):
    min_till_now = min_ever = 0
    for num in num_arr:
        min_till_now = min(num, num + min_till_now)
        min_ever = min(min_ever, min_till_now)
    return min_ever


def calculate_max_subarray_sum_circ(num_arr):
    min_subarray_sum = calculate_min_subarray_sum(num_arr)
    max_subarray_sum = calculate_max_subarray_sum(num_arr)
    return max(max_subarray_sum, sum(num_arr) - min_subarray_sum)


# problem 4
def small_el_right_count(num_arr):
    # result = []
    # for i, num in enumerate(num_arr):
    #   count = sum(val < num for val in num_arr[i+1:])
    # # for i in range(len(num_arr)):
    #   # count = 0
    #   # for j in range(i+1, len(num_arr)):
    #   #   if (num_arr[j] < num_arr[i]):
    #   #     count += 1
    #   result.append(count)
    # print(result)
    seen = []
    result = []
    for num in reversed(num_arr):
        i = bisect.bisect_left(seen, num)
        result.append(i)
        bisect.insort(seen, num)
    return list(reversed(result))


if __name__ == "__main__":
    # problem 1
    arr = [1, 2, 3, 4, 5, 6]
    print(products(arr))

    # problem 2
    arr = [1, 24, 4, 5, 6, 7, 8]
    print(smallest_unsorted_window(arr))

    # problem 3
    arr = [34, -50, 42, 14, -5, 86]
    print(calculate_max_subarray_sum(arr))
    print(calculate_max_subarray_sum_circ(arr))

    # problem 4
    arr = [3, 4, 9, 6, 1]
    print(small_el_right_count(arr))
