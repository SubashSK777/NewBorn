bol = [False, False, False, False, False, True, True, True, True]

l = 0
r = len(bol) - 1

while l < r:
    m = (l + r + 1) // 2  # Bias mid towards right
    if bol[m]:  # If mid is True
        l = m  # Narrow range to [m, r]
    else:  # If mid is False
        r = m - 1  # Narrow range to [l, m-1]

print(l)  # This gives the index of the last True
