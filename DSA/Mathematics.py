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

# n = 5

# fib = [0, 1]

# first = 0
# second = 0

# for i in range(2, n):
#   first = fib[-1]
#   second = fib[-2]
  
#   fib.append(first + second)
  
# print (fib[-1])

n = 153
size = len(str(n))
res = 0

while n != 0:
  n = n % 10
  n = n ** size
  res += n
  n = n // 10
  
if res == n:
  print("It is Armstrong")
else:
  print("Not an Armstrong")  
  