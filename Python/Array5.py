bol = [False, True, True, True, True]

l = 0
r = len(bol) - 1

while l < r:
  m = (l + r) // 2
  
  if bol[m] == True:
    r = m
    
  else:
    l = m + 1
    
print(l)
    