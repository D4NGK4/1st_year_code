class func:
    def __init__(self):
        self.elem = []

    def push(self,elem):
        self.elem.append(elem)
    
    def pop(self):
        return self.elem.pop()
    
    def list_size(self) -> int:
        return len(self.elem)

fn = func()
nums =  int(input("Enter Number: "))
if nums == 0:
    print("Binary: 0")
    exit()

new_num = nums

while nums != 0:
    new_num = nums % 2
    nums = nums // 2
    fn.push(new_num)

print("Binary: ", end="")

while fn.list_size() != 0:
    x = fn.pop()
    print(x, end=" ")



print("\n")



