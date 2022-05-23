class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insertion(self, newElement):
    newNode = Node(newElement)
    if(self.head == None):
      self.head = newNode
      return
    else:
      temp = self.head
      while(temp.next != None):
        temp = temp.next
      temp.next = newNode

  def deletion(self):
    if(self.head != None):
      temp = self.head
      self.head = self.head.next
      temp = None 

  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("Linked List: ", end=" ")
      while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next
      print()
    else:
      print("The list is empty.")
              
MyList = LinkedList()

MyList.insertion(10)
MyList.insertion(20)
MyList.insertion(30)
MyList.insertion(40)
MyList.PrintList()

MyList.deletion()
MyList.PrintList()  