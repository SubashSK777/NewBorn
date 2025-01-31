class Stack:
  def __init__(self):
    self.stack = []
    
  def append(self, element):
    self.stack.append(element)
    
  def pop(self, element):
    self.stack.pop(element)
    
  def peek(self):
    if self.isEmpty():