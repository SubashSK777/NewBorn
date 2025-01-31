class StackArray:
  def __init__(self):
    self.stack = []
    
  def add(self, element):
    self.stack.append(element)
    
  def pop(self, element):
    if self.isEmpty():
      return "Stack is Empty"
    self.stack.pop(element)
    
  def peek(self):
    if self.isEmpty():
      return "Stack is Empty"
    else:
      return self.stack[-1]
    
  def length(self):
    return len(self.stack)
  
  def Empty(self):
    return len(self.stack) == 0
  
  
list1 = Stack()

list1.add(7)
list1.add(4)
list1.add(8)
print(list1)
  
  

  
  