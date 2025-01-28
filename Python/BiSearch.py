nums = [1,2,3,4,5,7,8,9]

k = 6

#Find the value in the nums that is greater than or equal to k

left = 0
right = len(nums) - 1

while left < right:
  mid = (left + right) // 2
  
  if nums[mid] == k:
    print(mid)
    break
  
  elif nums[mid] > k:
    right = mid - 1