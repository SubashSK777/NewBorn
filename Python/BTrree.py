from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" -> ")
            self.inorder(root.right)
        

    def preorder(self, root):
        if root:
            print(root.data, end=" -> ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" -> ")

    def levelorder(self, root):
        queue = deque()

        if root is None:
            return "Nothing"

        queue.append(root)

        while queue:
            popped = queue.popleft()
            print(popped.data, end=" -> ")
            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)
                


BiSuresh = BinaryTree()

BiSuresh.root = Node(5)
BiSuresh.root.left = Node(4)
BiSuresh.root.right = Node(7)
BiSuresh.root.left.left = Node(8)
BiSuresh.root.right.right = Node(0)

BiSuresh.inorder(BiSuresh.root)
print()
BiSuresh.preorder(BiSuresh.root)
print()
BiSuresh.postorder(BiSuresh.root)
print()
BiSuresh.levelorder(BiSuresh.root)
        
        


        