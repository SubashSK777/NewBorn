#ARRAYYYYYYYYYY
from array import *

arr = array('i', [1, 2, 3, 4, 5])

NewArr = array(arr.typecode, [])
i = 0

while i < len(arr):
  b = arr[i]*arr[i]
  NewArr.append(b)
  i += 1

print

# NewArr = array(arr.typecode, (a for a in arr))
# for ab in NewArr:
#   print(ab*ab)

# for vals in arr:
#   print(vals*vals)
