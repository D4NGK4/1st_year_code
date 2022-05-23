from collections import deque

dq = deque()

dq.append(1)
dq.append(45)
dq.append(2)
dq.append(53)
dq.append(80)

print(dq, end="\n\n")

print("Elements Popped: ", dq.popleft(), dq.popleft(), dq.popleft(), end="\n\n")
print("Remaining Elements: ", dq)