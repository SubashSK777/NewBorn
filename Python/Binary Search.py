arr = [1, 2, 2, 2, 3, 4, 5]

def binary_search(arr, target):
	L = 0
	R = len(arr) - 1
	while L <= R:
		M = (L + R)//2
		if arr[M]  == target:
			return M 
		elif arr[M] < target:
			L = M + 1
		else:
			R = M - 1

	return -1 


res = binary_search(arr, 2)

print(res)