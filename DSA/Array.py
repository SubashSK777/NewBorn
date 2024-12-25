#ARRAYYYYYYYYYY
from array import *

arr = array('i', [])

n = int(input("Enter the Number of Inputs: "))

for i  in range(n):
  x = int(input("Enter the Number: "))
  arr.append(x)
  
print(arr)


# def store():
#   while True:
#     try:
#       x = int(input("Enter a Number: "))
#       arr.append(x)
#       store()
#     except: 
#       print(arr)
#       break

# store()

# NewArr = array(arr.typecode, [])

# i = 0

# while i < len(arr):
#   b = arr[i]*arr[i]
#   NewArr.append(b)
#   i += 1

# print(NewArr)

# NewArr = array(arr.typecode, (a for a in arr))
# for ab in NewArr:
#   print(ab*ab)

# for vals in arr:
#   print(vals*vals)
