#ARRAYYYYYYYYYY
from array import *

arr = array('i', [1, 2, 3, 4, 5])

NewArr = array(arr.typecode, ())

for vals in arr:
  print(vals*vals)
