import sys
n, k = map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

hist = [False if i == k else True for i in range(n) ]

minval = [sys.maxsize]

def DFS(r, c,time, depth):
    if depth == n-1:
        minval[0] = min(minval[0], time)
        return

    if time > minval[0] :
        return

    for j in range(n):
        if j != c and hist[j]:
            hist[j] = False
            DFS(c, j, time + arr[c][j], depth+1)
            hist[j] = True



for tt in range(n):
    for i in range(n):
        for j in range(n):
            if i == j : continue
            arr[i][j] = min(arr[i][j], arr[i][tt] + arr[tt][j])

for c in range(n):
    if k != c and hist[c]:
        hist[c] = False
        DFS(k, c, arr[k][c],1)
        hist[c] = True

print(minval[0])