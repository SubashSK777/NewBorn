class StackArray:
  def __init__(self):
    self.stack = []
    
  def add(self, element):
    self.stack.append(element)
    
  def pop(self, element):
    self.stack.pop(element)
    
  def peek(self):
    if self.