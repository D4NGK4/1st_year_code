print('Inertion Sort')
print('')

print('Enter 10 integers: ')
list = []
for i in range(10):
    nums = int(input())
    list.append(nums)


def insertionSort(array):
	index_len = range(1,len(array))
	for i in index_len:
		key_value = array[i]
		
		while array[i-1] > key_value and i>0:
			array[i], array[i-1] = array[i-1], array[i]
			i = i-1

	return list

print('')
insertionSort(list)
print(list)
print('Max: ', max(list))
print('Min: ', min(list))
print('Sum: ', sum(list))




