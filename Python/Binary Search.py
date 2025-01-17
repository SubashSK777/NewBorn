arr = [-3, -1, 0, 2, 4, 6, 8, 10]

print(binary_search)
def binary_search(arr):
  L = 0
  R = len(arr) - 1
  target = 7
  while L < R:
    M = L + R // 2
    
    if arr[M] == target:
      return M
    elif arr[M] < target:
      L = M + 1
    else:
      R = M - 1
  return M