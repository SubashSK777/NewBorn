def square(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

def triangle(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()

def num_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            print(j + 1, end=" ")
        print()

def same_num_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            print(i + 1, end=" ")
        print()

def rev_triangle(n):
    for i in range(n, -1, -1):
        for j in range(i):
            print("*", end= " ")
        print()

def rev_num_tri(n):
    for i in range(n, -1, -1):
        for j in range(i):
            print(j + 1, end=" ")
        print()

def mid_tri(n):
    for i in range(n):
        for j in range()


#square(5)
#triangle(5)
#num_triangle(5)
#same_num_triangle(5)
#rev_triangle(5)
rev_num_tri(5)
