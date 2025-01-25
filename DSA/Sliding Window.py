arr = [2, 1, 5, 1, 3, 2]
n = len(arr)
k = 3

curr_sum = 0

for i in range(k):
  curr_sum += arr[i]
  
max_sum = curr_sum 

for i in range(k, n):
  curr_sum += arr[i]
  curr_sum -= arr[n - k]
  
  new_sum = curr_sum 
  max_sum = max(max_sum, avg)
  
print(max_avg)
  