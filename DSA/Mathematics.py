from math import *

# n = 91

# for i in range(2, isqrt(n) + 1):
#   if n % i == 0:
#     print ("Not a Prime")
#     break
# else:
#   print("Prime")

n = 5 

res = 1

for i in range(n):
  res *= i
  
print(res)