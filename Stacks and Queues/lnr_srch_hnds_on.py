lst = []

print("Type stop to exit the loop\n")

while lst != 1:
	ext = str(input("Enter Number: "))
	if ext == "stop":
		break
	nums = int(ext)
	lst.append(nums)

def ln_srch(lst, x):
	for i in range(0,len(lst)):
		if lst[i] == x:
			return i
	return -1

y = int(input("\nEnter Number to search: "))
lin_search = ln_srch(lst,y)

print(lst)

if lin_search == None:
	print("Number not found.")
else:
	print(y,"is located at index", lin_search)
