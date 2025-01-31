stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print("Stack:", stack)

element = stack.pop()

print("Pop:", element)

peek = stack[-1]

print("Peek:", peek)

print("Stack:", stack)

isEmpty = not bool(stack)

print(isEmpty)