class Node:
  def __init__(self, data):
    self.data  = data
    self.next = None
    
class LiLi:
  def __init__(self):
    self.head = None
    
  def beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
    
  def end(self, data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
    else:
      temp = self.head
      while temp.next:
        temp = temp.next
      temp.next = new_node
      
  def search(self, target):
    if self.head == None:
      return "List is Empty"
    temp = self.head
    
    while temp:
      if temp.data == target:
        return "Target Found"
      else:
        temp = temp.next
        
    return "Target Not Found"
      
  def after(self, data, target):
    new_node = Node(data)
    temp = self.head
    if self.head == None: 
      print("List is Empty")
      return
    while temp:
      if temp.data == target:
        new_node.next = temp.next
        temp.next = new_node
        print("Target Inserted")
        return
      else:
        temp = temp.next
    print("Target Not Found")
    return  
  
  def before(self, data, target):
    new_node = Node(data)
    temp = self.head
    if self.head == None:
      print("List is Empty")
      return
    if self.head.data == target:
      self.beginning(data)
      return
    
    while temp:
      if temp.next.data == target:
        new_node.next = temp.next
        temp.next = new_node
        print("Target Inserted")
        return
      else:
        temp = temp.next
    print("Target Not Found")
    return
      
  def res(self):
    temp = self.head
    while temp:
      print(temp.data, end = " -> ")
      temp = temp.next
      
    return
  

lst1 = LiLi()

lst1.end(3)
lst1.end(4)
lst1.end(5)
lst1.end(7)
# print(lst1.search(0))
lst1.after(2,3)
lst1.before(6,3)


lst1.res()

    