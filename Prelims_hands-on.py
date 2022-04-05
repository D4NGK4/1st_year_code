print('Submitted by: Dan Josuha M. Tagaan')
print('')
print('IT1R12')
print('')
print('')
print('Enter Five Integers: ')

l1 = []
for i in range(5):
    nums = int(input())
    l1.append(nums)    


average = float(sum(l1)) / 5

print('')
print('Output all integers: ' + str(l1))
print('')
print('Maximum: ' + str(max(l1)))
print('')
print('Minimum: ' + str(min(l1)))
print('')
print('Average: ' + str(average))
print('')
print('Sum: ' + str(sum(l1)))
print(''), l1.reverse()
print('Reverse: ' + str(l1))
print(''), l1.sort()
print('Sorted: ' + str(l1))