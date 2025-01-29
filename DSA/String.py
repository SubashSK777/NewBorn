arr = [1,2,3,4]
p = 1
s = 1
res = [1]

for i in range(len(arr) - 1):
  p *= arr[i]
  res.append(p)
  print(arr[i])
  
for i in range(len(arr) - 1, -1, -1):
  s *= arr[i]
  res[i] *= s
  print(arr[i])
  
print(res[i])
  
  

