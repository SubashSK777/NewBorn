class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LiLiQu:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail == None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.head == None:
            return "Queue is Empty"
        else:
            temp = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail == None
            self.size -= 1
            return temp
        
    def printer(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
        
quququ = LiLiQu()

quququ.enqueue('a')
quququ.enqueue('b')
quququ.enqueue('c')
quququ.enqueue('d')

quququ.printer()

quququ.dequeue()
quququ.dequeue()

quququ.printer()
        
    