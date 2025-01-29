arr = [1,2,3,4]

pre = 1

pre_res = []

for i in arr:
  pre *= i
  pre_res.append(pre)
  
print(pre_res)
  