#ARRAYYYYYYYYYY
from array import *

arr = array('i', [1, 2, 3, 4, 5])

i = 0

while i < len(arr):
  print(arr[i]*arr[i])
  i += 1



# NewArr = array(arr.typecode, (a for a in arr))
# for ab in NewArr:
#   print(ab*ab)

# for vals in arr:
#   print(vals*vals)
