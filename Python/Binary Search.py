matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

arr = []
for i in matrix:
  for j in matrix:
    arr.append
  

target = 10

def binary_search(arr, target):
  left, right = 0, len(arr) - 1
  
  while left <= right:
    mid = (left + right) // 2
    
    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      right = mid - 1
    else:
      left = mid + 1
  return mid


print(binary_search(arr, target))
      
      
  

