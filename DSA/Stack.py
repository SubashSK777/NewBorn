class StackArray:
  def __init__(self):
    self.stack = []
    
  def add(self, element):
    self.stack.append(element)
    
  def pop(self, element):
    self.stack.pop(element)
    
  def peek(self):
    if self.stack.isEmpty:
      return "Stack is Empty"
    else:
      return self.stack[-1]
    
  def Empty(self):
    return len(self) == 0
  
  def Length(self):
    if self.isEmpty:
      return "Stack is Empty"
    else:
      return len(self)
    
list1 = StackArray()

list1.add(3)
list1.add(5)
list1.peek()

print(list1.stack)
