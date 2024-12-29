#ARRAYYYYYYYYYY

# from math import *

# n = 982451653

# for i in range(2, isqrt(n)):
#   if n % i == 0:
#     res = False
#     break
#   else:
#     res = True
  
# print(res)
  
  
# a = "nagaram".lower()
# b = "anagram".lower()

# a = sorted(a)
# b = sorted(b)

# if a == b:
#   print("True")
# else: 
#   print("False")
  

# a = "asdfghjkliuytre"
# print(a[0])

# n = [1, 2, 3, 4, 5, 5, 6, 6]

# n = sorted(set(n))

# if len(n) < 2:
#   print("No 2nd Largest")
  
# else:
#   print(n[-2])

# n = [3, 1, 5, 2, 7, 9, 4]

# if n == sorted(n):
#   print (True)
# else: 
#   print (False)

# n = [3, 1, 5, 2, 7, 9, 4, 3, 7, 9, 1, 1]


# frequency = {}

# for num in n:
#     if num in frequency:
#         frequency[num] += 1
#     else:
#         frequency[num] = 1

# print(frequency)
    


# from numpy import * 

# arr = array([1, 2, 3, 4, 5, 5, 6])

# out = [i for i, char in enumerate(arr) if char == 5 ]
# print(out)



# print (arr[::-1])
# print (sum(arr))
# print (max(arr))
# print (min(arr))

# arr1 = array([1, 2, 3, 4, 5])
# arr2 = array([6, 7, 8, 9, 0])

# print(concatenate([arr1, arr2]))

# n = int(input("Enter the Number of Inputs: "))

# for i  in range(n):
#   x = int(input("Enter the Number: "))
#   arr.append(x)
  
# find = int(input("Enter the Value to find: "))

# if find in arr:
#   print(f"The Value {find} is at Index {arr.index(find)}")
# else:
#   print("Value Not Found")

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
