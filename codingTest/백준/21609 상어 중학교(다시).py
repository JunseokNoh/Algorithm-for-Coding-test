import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

def find_group():
    temp = [[arr[i][j] for j in range(n)] for i in range(n)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    groups = []
    for i in range(n):
        for j in range(n):
            if temp[i][j] > 0 :
                target = []
                que = deque([[i,j]])
                val = temp[i][j]
                visited = [[True for _ in range(n)] for _ in range(n)]
                while que :
                    y,x = que.popleft()
                    for dy,dx in dirs:
                        yy, xx = y + dy, x + dx
                        if 0 <= yy < n and 0 <= xx < n:
                            if visited[yy][xx] and (temp[yy][xx] == val or temp[yy][xx] == 0):
                                visited[yy][xx] = False
                                que.append([yy,xx])
                                target.append([yy,xx])

                cy,cx = n+1, n+1
                rain_cnt = 0
                for y,x in target:
                    if (y < cy or (y == cy and x < cx)) and temp[y][x] > 0:
                        cy, cx = y, x
                    if temp[y][x] > 0: temp[y][x] = -1
                    elif temp[y][x] == 0 : rain_cnt += 1
                if len(target) >= 2:
                    groups.append([len(target),rain_cnt,cy,cx,target])
    groups.sort(key = lambda x : (-x[0], -x[1], -x[2], -x[3]))
    return groups

def gravity():
    for j in range(n):
        for i in range(n-1,-1,-1):
            if arr[i][j] >= 0 :
                y = i
                x = j
                for k in range(1, n-i):
                    if arr[y+1][x] == -1 : break
                    if arr[y+1][x] == -2 :
                        arr[y+1][x], arr[y][x] = arr[y][x], arr[y+1][x]
                    y = y+1

def rotate():
    temp = [[0 for _ in range(n)] for _ in range(n)]
    r,c = 0,0
    for i in arr:
        r = 0
        for j in reversed(i):
            temp[r][c] = j
            r += 1
        c += 1
    return temp

answer = 0
while True:
    group = find_group()
    if len(group) == 0 : break
    answer += len(group[0][4]) ** 2
    for y,x in group[0][4]:
        arr[y][x] = -2
    gravity()
    arr = rotate()
    gravity()

print(answer)

#step 1 크기가 가장 큰 블록
# 모든 칸에는 블록이있다.
# 검은색(-1), 무지개(0), 일반
# 일반은 M가지 색상으로 나뉜다.
# 상하좌우로 인접하면 인접한 칸이다
# 블록의 그룹은 연결된 블록의 집합
# 그룹에는 적어도 하나의 일반 블록이 있어야하고 블록 색상은 모두 동일
# 검은 블록은 포함되면 안됨
# 기준 블록은 무지개 블록이 아닌 블록중에서 행과 열이 가장 작은 것이 기준 블록이 됨