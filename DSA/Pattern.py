n = 5

# for i in range(1, n + 1):
#   print(i)
  
# for j in range(n, 0, -1):
#   print(j)

# for i in range(n):
#   if i % 2 != 0:
#     print (i)

# for i in range(n):
#   for j in range(i + 1):
#     print ("*", end = " ")
#   print("\n")
  

for i in range(n):
  for j in range(n - i - 1):
    print(" ", end = " ")
  for k in range(2*i + 1):
    print("*", end = " ")
  print("\n")