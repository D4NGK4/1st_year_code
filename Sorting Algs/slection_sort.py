print('Selection Sort')
print('')

print('Enter 10 integers: ')
list = []
for i in range(10):
    nums = int(input())
    list.append(nums)

def selection_sort(A):
	for i in range (0, len(A) - 1):
		minIndex = i
		for j in range (i+1, len(A)):
			if A[j] < A[minIndex]:
				minIndex = j
		if minIndex != i:
			A[i], A[minIndex] = A[minIndex], A[i]

print('')
selection_sort(list)
print(list)
print('Max: ', max(list))
print('Min: ', min(list))
print('Sum: ', sum(list))