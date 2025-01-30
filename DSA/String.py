arr = [1,2,4,8,8,8,8,8,6,5,3,2]
target = 8
#first occurance
def fbi_search(arr, target):
  l = 0
  r = len(arr) - 1
  
  while l < r:
    m  =(l + r) // 2
    if arr[m] == target:
      r = m
    else:
      l = m + 1
  return l


def lbi_search(arr, target):
  l = 0 
  r = len(arr) - 1
  
  while l < r:
    m = (l + r) // 2
    if arr[m] == target:
      l = m + 1
    else:
      r = m - 1
  return l
      
print(fbi_search(arr, target))
print(lbi_search(arr, target))