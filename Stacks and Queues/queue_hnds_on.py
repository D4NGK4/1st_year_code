import random as rand

q = []

for i in range(10):
    num = rand.randint(1,100)
    q.append(num)

print("Queue Size: ",len(q),"\n")
print("Queue:", q,"\n")
print("Numbers to be Poped:",q.pop(0),q.pop(0),q.pop(0),"\n")
print("New queue size:", len(q),"\n")
print("New queue: ",q, "\n")
print("Is queue empty? ", end="")
if q == None:
    print("True")
else:
    print("False")
