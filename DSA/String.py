arr = [1,2,3,4]
p = 1
s = 1
res = [1]

for i in range(len(arr) - 1):
  p *= arr[i]
  res.append(p)
  
for i in range(len(arr), -1, -1):
  s *= arr[i]
  
  
print(res)
  
  

