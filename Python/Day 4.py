nums = [20,100,10,12,5,13]

for i in range(len(nums)):
    for j in range(i, len(nums)):
        if nums[i] < nums[j]:
            for k in range(j, len(nums)):
                if nums[j] < nums[k]:
                    print("True")
                    
print("Error")
        