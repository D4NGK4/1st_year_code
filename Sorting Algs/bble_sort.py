print('Bubble Sort')
print('')
print('Submitted by: Dan Joshua M. Tagaan')
print('')

print('Enter 10 integers: ')
list = []
for i in range(10):
    nums = int(input())
    list.append(nums)

for i in range(len(list)-1):
    print(list)
    for j in range (len(list)-1-i):
        if list[j] > list[j+1]:
            list[j+1], list[j] = list[j], list[j+1]


print('')
print('Sorted list: ')
print(list)
print('Max: ', max(list))
print('Min: ', min(list))
print('Sum: ', sum(list))
