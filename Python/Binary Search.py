arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7

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
  return "Not Found"


print(binary_search(arr, target))
      
      
  

