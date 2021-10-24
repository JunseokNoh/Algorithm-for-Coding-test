from collections import deque
N = int(input())
arr = [list(str(input())) for _ in range(N)]
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
hist = [True for _ in range(11)]
dist = [[0 for _ in range(11)] for _ in range(11)]
target = []
y,x = 0,0
result = 9999999999

def dfs(d,num,cnt, target, hist):
    global result
    if num == 10 and cnt >= 3 :
        result = min(result, d)
        return

    for coin, y,x in target:
        if num < coin and hist[coin] and dist[num][coin] > 0:
            hist[coin] = False
            if  1<= coin <= 9 :
                dfs(d+dist[num][coin], coin, cnt + 1, target,hist)
            else:
                dfs(d + dist[num][coin], coin, cnt, target, hist)
            hist[coin] = True

def find(y,x,ty,tx):
    que = deque([[0,y,x]])
    visited = [[True for _ in range(N)] for _ in range(N)]
    answer = 0
    while que :
        depth, y,x = que.popleft()
        if y == ty and x == tx :
            answer = depth
            break
        for dy, dx in dirs:
            yy, xx = y+dy, x+dx
            if 0 <= yy < N and 0 <= xx < N:
                if arr[yy][xx] != '#' and visited[yy][xx]:
                    visited[yy][xx] = False
                    que.append([depth+1,yy,xx])
    return answer

for i in range(N):
    for j in range(N):
        if arr[i][j].isdecimal():
            arr[i][j] = int(arr[i][j])
            target.append([arr[i][j], i,j])
        elif arr[i][j] == 'S':
            y,x = i,j
            target.append([0, i, j])
        elif arr[i][j] == 'E':
            target.append([10, i,j])

target.sort(key = lambda x : (x[0]))
for i in range(len(target)-1):
    for j in range(i+1, len(target)):
        n1, y1, x1 = target[i]
        n2, y2, x2 = target[j]
        d = find(y1,x1,y2,x2)
        dist[n1][n2] = d
        dist[n2][n1] = d

hist[0] = False
dfs(0,0,0, target, hist)
if result == 9999999999:
    print(-1)
else:
    print(result)
