arr = [1,2,3,4]

pre = 1

pre_res = []

for i in range(len(arr)):
  pre *= arr[i]
  pre_res.append(pre)
  
print(pre_res)

suf = 1

suf_res = [1]

for i in range(len(arr) - 1, 0, -1):
  suf *= arr[i]
  suf_res.append(suf)
  
print(suf_res)
  
  
  