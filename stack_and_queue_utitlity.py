import time
import random
import math


def get_random_array(size=10):
    random.seed(time.time())
    arr = []
    for i in range(size):
        arr.append(math.floor(random.random() * 100))
    return arr
