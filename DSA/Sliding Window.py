# arr = [2, 1, 5, 1, 3, 2]
# n = len(arr)
# k = 3

# curr_sum = 0

# for i in range(k):
#   curr_sum += arr[i]
  
# max_sum = curr_sum 

# for i in range(k, n):
#   curr_sum += arr[i]
#   curr_sum -= arr[n - k]
  
#   new_sum = curr_sum 
#   max_sum = max(max_sum, new_sum)
  
# print(max_sum)
  
  

def threeSum(nums):
    res = []
    
    nums.sort()

    i = 0


    while i < len(nums) - 2:
      j = i + 1
      k = len(nums) - 1
      print(i)
      target = 0 - nums[i]
      while j < k:
          print(j,k)
          if nums[j] + nums[k] > target:
              k -= 1
          elif nums[j] + nums[k] < target:
              j += 1 
          elif nums[j] + nums[k] == target:
              res.append([nums[i], nums[j], nums[k]])

      i += 1
    return res       
  
nums=[-1,0,1,2,-1,-4]
print(threeSum(nums))