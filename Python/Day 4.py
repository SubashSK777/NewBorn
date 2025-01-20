nums = [20,100,10,12,5,13]

for i in range(1, len(nums)-1):
    if min(nums[:i]) < nums[i] and max(nums[i:]) > nums[i]:
        print("True")
print("False")      