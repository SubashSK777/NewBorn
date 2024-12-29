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

# n = 153
# org_n = n
# res = 0

# size = len(str(n)) 

# while n != 0:
#   digit = n % 10
#   res += digit ** size
#   n = n // 10
  
# if res == org_n:
#   print("It is an Armstrong")
# else:
#   print("Not an Armstrong")
  
  
# str1 = "Nagaram".lower()
# str2 = "Anagram".lower() 

# res = True

# if len(str1) == len(str2) and sorted(str1) == sorted(str2):
#   res = True
# else: 
#   res = False
  
# print (res)
  
# n = 153
# org_n = n
# size = len(str(n))
# res = 0

# while n != 0:
#   sub = n % 10
#   res += sub ** size
#   n = n // 10
  
# if res == org_n:
#   print("It is an Armstrong")
# else:
#   print("It is not an Armstrong")


# a = "Nagaram".lower()
# b = "Anagram".lower()

# a = set(a)
# b = set(b)

# if a == b:
#   print ("It is an Anagram")
  
# else: 
#   print ("It is Not an Anagram")

# a = "Madam".lower()

# if a == a[::-1]:
#   print("It is a Palindrome")
# else:
#   print("It is not a Palindrome")

n = 5
res = 1
for i in range(n + 1):
  res