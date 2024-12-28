from math import *

# n = 91

# for i in range(2, isqrt(n) + 1):
#   if n % i == 0:
#     print ("Not a Prime")
#     break
# else:
#   print("Prime")

# n = 5 

# res = 1

# for i in range(1, n + 1):
#   res *= i
  
# print(res)

n = 5

fib = [0, 1]

first = 0
second = 0

for i in range(n):
  first = fib[i]
  second = fib[i + 1]
  
  fib.append(first + second)
  
print (fib)

  