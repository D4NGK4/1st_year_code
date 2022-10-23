print('Hands-on Midterms')
print('')
print('Submitted by: Dan Joshua M. Tagaan')
print('')


num_of_inputs = int(input('Enter number of inputs: '))

list = []

for i in range(num_of_inputs):
    nums = int(input('Enter number: '))
    list.append(nums)

print('')
print('Unsorted List: ')
print(list)

for i in range(len(list)-1):
    for j in range (len(list)-1-i):
        if list[j] > list[j+1]:
            list[j+1], list[j] = list[j], list[j+1]

print('Sorted list: ')
print(list)
