from math import *

n = 91

for i in range(2, isqrt(n) + 1):
  if n % i == 0:
    print ("Not a Prime")
    break
  else:
    print("Prime")