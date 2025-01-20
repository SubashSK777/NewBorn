nums = [1,2,3,4]

pre = 1
res = [1]
prod = 1
for i in range(0, len(nums)-1):
    prod *= nums[i]
    res.append(prod)
    
    
for i in range(len(nums), 1, -1):
    res[i] *= nums[i]
    res.append
    
print(res)