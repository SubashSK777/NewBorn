class StackArray:
  def __init__(self):
    self.stack = []
    
  def add(self, element):
    self.stack.append(element)
    
  def pop(self, element):
    self.stack.pop(element)
    
  def peek(self):
    if self.isEmpty():
      return "Stack is Empty"
    else:
      return self.stack[-1]
    
  def isEmpty(self):
    return len(self.stack) == 0
  
  def Length(self):
    if self.isEmpty():
      return "Stack is Empty"
    else:
      return len(self)
    
# list1 = StackArray()

# list1.add(3)
# list1.add(5)
# print(list1.peek())

# print(list1.stack)

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LiLi:
  def __init__(self):
    self.head = None
    self.size = 0

  def insertAtBeginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
    self.size += 1

  def popAtBeginning(self):
    popped = self.head.data
    self.head = self.head.next
    self.size -= 1
    return popped

  def peek(self):
    if self.size == 0:
      return "Stack is Empty"
    else:
      return self.head.data

  def 



    

    