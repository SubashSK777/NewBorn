def sqr_gen(n, i = 1):
    if i > n:
        return 
    else:
        print(i * i)
        return sqr_gen(n, i + 1)
    
n = int(input())

print(sqr_gen(n))