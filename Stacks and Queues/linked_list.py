class ListNode:
    def __init__(self, value, pointer):
        self.value = value
        self.pointer = pointer

node4 = ListNode(31,None)
node3 = ListNode(37,node4)
node2 = ListNode(62,node3)
node1 = ListNode(23,node2)

print(node1.value)
print(node2.value)
print(node3.value)
print(node4.value)