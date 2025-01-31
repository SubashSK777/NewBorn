class StackArray:
  def __init__(self):
    self.stack = []
    
  def add(self, element):
    self.stack.append(element)
    
  def pop(self, element):
    self.stack.pop(element)
    
  def peek(self):
    if self.stack.isEmpty():
      return "Stack is Empty"
    else:
      return self.stack[-1]
    
  def Empty(self):
    return len(self) == 0
  
  def Length(self):
    if self.isEmpty():
      return