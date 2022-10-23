lst = []

print("Type stop to exit the loop\n")

while lst != 1:
	ext = str(input("Enter Number: "))
	if ext == "stop":
		break
	nums = int(ext)
	lst.append(nums)

def bnry_srch(lst, x, low, high):

    while low <= high:
        mid = low + (high - low)//2
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

y = int(input("\nEnter Number to search: "))
bin_search = bnry_srch(lst, y, 0, len(lst)-1)

print(lst)

if bin_search == None:
	print("Number not found.")
else:
	print(y,"is located at index", bin_search)
