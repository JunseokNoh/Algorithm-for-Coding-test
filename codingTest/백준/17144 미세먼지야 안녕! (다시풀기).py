import sys

def spread(r,c):
    target = []
    temp = [[0 for _ in range(c)] for _ in range(r)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    cleaner = []

    for i in range(r):
        for j in range(c):
            if A[i][j] > 0:
                target.append((i,j))
            elif A[i][j] == -1:
                temp[i][j] = -1
                cleaner.append((i,j))

    for i,j in target:
        total = 0
        val = A[i][j] // 5
        for dy,dx in dirs:
            y,x = i + dy, j + dx
            if 0 <= y < r and 0 <= x < c and A[y][x] != -1:
                total += val
                temp[y][x] += val
        temp[i][j] += A[i][j] - total

    return temp, cleaner

def clean(r,c,cleaner):
    #반시계방향 먼저
    r1,c1 = cleaner[0]
    for row in range(r1-2,-1, -1): A[row+1][0] = A[row][0]
    for col in range(1,c,1): A[0][col-1] = A[0][col]
    for row in range(1,r1+1): A[row-1][c-1] = A[row][c-1]
    for col in range(c-2,0,-1): A[r1][col+1] = A[r1][col]
    A[r1][c1+1] = 0

    r2,c2 = cleaner[1]
    for row in range(r2+2,r): A[row-1][0] = A[row][0]
    for col in range(1,c): A[r-1][col-1] = A[r-1][col]
    for row in range(r-2,r2-1,-1): A[row+1][c-1] = A[row][c-1]
    for col in range(c-2,0,-1): A[r2][col+1] = A[r2][col]
    A[r2][1] = 0

r,c,t = map(int,sys.stdin.readline().split())
A = [list(map(int,sys.stdin.readline().split())) for _ in range(r)]

for _ in range(t):
    A, cleaner = spread(r,c)
    clean(r,c,cleaner)

print(sum(map(sum,A)) + 2)