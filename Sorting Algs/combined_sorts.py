#Gif, how do i use my own list on the sorting stuff? Like i have that input func above and i want to-
#use the numbers on the list there in the sorting thing.

print('Enter 10 integers: ')

list = []
for i in range(10):
    nums = int(input(''))
    list.append(nums)
print('')
print('Unsorted list: ' + str(list))
print('')

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

def selection_sort(A):
	for i in range (0, len(A) - 1):
		minIndex = i
		for j in range (i+1, len(A)):
			if A[j] < A[minIndex]:
				minIndex = j
		if minIndex != i:
			A[i], A[minIndex] = A[minIndex], A[i]

def insertion_sort(A):
	for i in range(1, len(list)-1):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

