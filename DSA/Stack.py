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
    
class LinkedLi:
  def __init__(self):
    self.head = None
    
  def push(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
    
  def pop(self, data):
    popped = self.head
    self.head = self.head.next
    return popped
    
  def printer(self):
    temp = self.head
    while temp:
      print(temp.data, end=" -> ")
      temp = temp.next
    print ("None")
    
    
lili = LinkedLi()

lili.push(5)
lili.push(3)
lili.push(9)
lili.push(10)

lili.printer()

    

    