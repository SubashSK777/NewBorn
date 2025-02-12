matrix = [[1,3]]

arr = []

for i in range(len(matrix)):
  for j in range(len(matrix)):
    arr.append(matrix[i][j])
    
print(arr)
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
      
      
  

