arr = [1,2,4,8,8,8,8,8,6,5,3,2]
target = 8
#first occurance
def bi_search(arr, target):
  l = 0
  r = len(arr) - 1
  
  while l < r:
    m  =(l + r) // 2
    if arr[m] == target:
      r = m
    