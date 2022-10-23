print('Bubble Sort')
print('')
print('Submitted by: Dan Joshua M. Tagaan')
print('')

num_of_inputs = int(input('Enter number of inputs: '))

print('Enter 10 integers: ')
list = []
for i in range(num_of_inputs):
    nums = int(input('Enter number: '))
    list.append(nums)

for i in range(len(list)-1):
    for j in range (len(list)-1-i):
        if list[j] > list[j+1]:
            list[j+1], list[j] = list[j], list[j+1]


print('')
print('Unsorted list:')
print(str(unsorted))
print('Sorted list: ')
print(str(list))
