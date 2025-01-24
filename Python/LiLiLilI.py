class Node:
  def __init__(self, data = None, next = None):
    self.data = data
    self.next = next
    
class LiLi:
  def __init__(self, head = None):
    self.head = head
    
  def insert_athead(self, data, head):
    new_node = Node(data, head)
    
    
    
lits = LiLi()

lits