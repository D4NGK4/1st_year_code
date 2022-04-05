import numpy as np
import random

list = []
for i in range(10):
    nums = int(input())
    list.append(nums)
    
x = np.random.randint(0,100,5)

def insertion_sort(A):
	for i in range(1, len(list)-1):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break





