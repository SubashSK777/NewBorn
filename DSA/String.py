arr = [1,2,3,4]

suf = 1

suf_res = []

for i in arr:
  suf *= i
  suf_res.append(suf)
  
print(suf_res)
  