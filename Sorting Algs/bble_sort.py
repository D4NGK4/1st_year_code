import numpy as np
import random

list = []
for i in range(10):
    nums = int(input())
    list.append(nums)

def bubbleSort(array, *args):
    size = len(array)
    for i in range(size):
        swapped = False
        for j in range(size - i - 1):
            yield array, j, j+1, -1, -1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break

x = np.random.randint(0,100,5)
y = [i for i in bubbleSort(x)]
last = y[-1][0]

print(last)