candies = [2,3,5,1,3] 
n_candies = candies.copy()
extraCandies = 3

res = []
n = len(candies)

for i in range(n):
    n_candies[i] += extraCandies
    if n_candies[i] >= max(candies):
        res.append(True)
    else:
        res.append(False)

print(res)