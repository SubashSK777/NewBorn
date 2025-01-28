nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

target = 16

l = 0

r = len(nums) - 1

while l <= r:
  m = (l + r) // 2
  
  if nums[m] * nums[m] == target:
    
    break
  
  elif nums[m] * nums[m] > target:
    r = m - 1
    
  else:
    l = m + 1
    
print(1//2)
  

