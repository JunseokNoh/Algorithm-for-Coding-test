import sys
from collections import deque

N, M, oil = map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
r,c = map(int,sys.stdin.readline().split())
r -= 1; c -= 1
infos = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
persons = [[[] for _ in range(N)] for _ in range(N)]
person_arr = [[0 for _ in range(N)] for _ in range(N)]
dest_arr = [[0 for _ in range(N)] for _ in range(N)]

dir = [(1,0), (-1,0), (0,1), (0,-1)]
for info in infos:
    r1,c1,r2,c2 = info
    persons[r1-1][c1-1] = [r2-1,c2-1]
    person_arr[r1-1][c1-1] = 2
    dest_arr[r2-1][c2-1] = 3

def find(row,col,target, tr,tc):
    que = deque([[0,row,col]])
    visited = [[True for _ in range(N)] for _ in range(N)]
    visited[row][col] = False
    result = []
    while que:
        depth, y, x = que.popleft()
        if target == 2 and person_arr[y][x] == 2:
            if depth > 0:
                result.sort(key=lambda x: (x[1], x[2]))
                person_arr[result[0][1]][result[0][2]] = 0
                return result[0]
            elif depth == 0:
                person_arr[y][x] = 0
                return [0, y, x]
        elif target == 3 and dest_arr[y][x] == 3 and y == tr and x == tc:
            return [depth, y, x]

        for dy, dx in dir:
            yy = y + dy; xx = x + dx
            if 0 <= yy < N and 0 <= xx < N and visited[yy][xx] and arr[yy][xx] == 0:
                if target == 2 and person_arr[yy][xx] == 2 :
                    result.append([depth+1, yy, xx])
                visited[yy][xx] = False
                que.append([depth+1, yy,xx])
    return [-1, -1 , -1]

for _ in range(M):
    dist, y, x = find(r,c,2,-1,-1)
    if dist == -1 :
        print(-1)
        break
    r,c = y,x; oil -= dist
    if oil <= 0 :
        print(-1)
        break
    tr, tc = persons[r][c]
    dist, y, x = find(r,c,3,tr,tc)
    if dist == -1 :
        print(-1)
        break
    r,c = y,x; oil -= dist
    if oil < 0 :
        print(-1)
        break
    oil += dist * 2
else:
    print(oil)

