arr = [-5, -3, -2, 1, 3, 5]

def BS(arr, target):
  N = len(arr)
  L = 0
  R = N
  
  while L < R:
    M = (L +R) // 2
    if arr[M] == target:
      return M
    elif arr[M] < target:
      