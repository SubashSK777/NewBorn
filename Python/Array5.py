bol = [True, True, True, True, True, False, False, False, False]

l = 0
r = len(bol) - 1

while l < r:
  m = (l + r) // 2
  
  if bol[m] == True:
    r = m
    
    