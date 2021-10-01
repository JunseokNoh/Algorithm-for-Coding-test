import sys

n,m = map(int,sys.stdin.readline().split())
A = [[0 for _ in range(n+1)]]

def move(row, col, num, count):
    # 왼쪽
    if num == 1 or num == 2 or num == 8:
        col -= count
        if col <= 0:
            cycle = abs(col) // n
            col += (cycle + 1) * n
    # 위
    if num == 2 or num == 3 or num == 4 :
        row -= count
        if row <= 0:
            cycle = abs(row) // n
            row += (cycle+1) * n
    # 오른쪽
    if num == 4 or num == 5 or num == 6:
        col += count
        col %= n
        if col == 0: col = n
    # 아래
    if num == 6 or num == 7 or num == 8:
        row += count
        row %= n
        if row == 0: row = n

    return (row, col)

for _ in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    temp.insert(0, 0)
    A.append(temp)

current_dir = [(n,1), (n,2), (n-1,1), (n-1, 2)]

for _ in range(m):
    d, dist = map(int,sys.stdin.readline().split())
    new_dir = []
    for dir in current_dir:
        new_dir.append(move(dir[0], dir[1], d,dist))
    current_dir = new_dir

    #step 1
    for y,x in current_dir:
        A[y][x] += 1
    visited = [[True for _ in range(n+1)] for _ in range(n+1)]
    #step 2
    for y,x in current_dir:
        for dy, dx in [(-1,-1), (-1,1), (1,-1), (1,1)]:
            yy,xx = y+dy, x+dx
            if 1 <= yy <= n and 1 <= xx <= n and A[yy][xx] > 0 :
                A[y][x] += 1
        visited[y][x] = False
    new_dir = []
    #step 3
    for i in range(1, n+1):
        for j in range(1, n+1):
            yx = str(i) + str(j)
            if visited[i][j] and A[i][j] >= 2 :
                A[i][j] -= 2
                new_dir.append([i,j])
    current_dir = new_dir

print(sum(map(sum, A)))