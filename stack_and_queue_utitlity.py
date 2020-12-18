import time
import random
import math

random.seed(time.time())


def get_random_array(size=10, factor=100):
    arr = []
    for i in range(size):
        arr.append(math.floor(random.random() * factor))
    return arr


def get_random_2d_array(size=6):
    arr = []
    for i in range(size):
        arr.append(get_random_array(math.floor(random.random()*10), 10))
    return arr

def get_sparse_array(size=1000):
    arr = []
    for i in range(size):
        arr.append(0)
    non_zero_len = 0
    while not non_zero_len:
        non_zero_len = math.floor(random.random() * 20)

    for i in range(non_zero_len):
        index = 0
        while not index:
            index = math.floor(random.random()*size)
        arr[index] = math.floor(random.random()*size)

    return arr