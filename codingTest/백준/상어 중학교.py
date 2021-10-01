import sys
from collections import deque

def drop_down():
    for col in range(n):
        for row in range(n-1,-1,-1):
            index = row
            if arr[row][col] >= 0:
                while True:
                    if index + 1 >= n: break
                    if arr[index+1][col] == -1 or arr[index+1][col] >= 0: break
                    if arr[index+1][col] == -2:
                        arr[index][col], arr[index+1][col] = arr[index+1][col], arr[index][col]
                    index = index+1

def turn_left():
    temp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[n-1-j][i] = arr[i][j]
    return temp

n,m = map(int,sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dir = [(1,0), (-1,0), (0,1), (0,-1)]
score = 0

# 블록 그룹이 존재하는 동안
while True:
    block_group = []
    #step1 블록 그룹 찾기
    copyed_arr = [[arr[i][j] for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if 0 < copyed_arr[i][j] <= m:
                blocks = [[i,j]]
                target = copyed_arr[i][j]
                rainbow = 0
                visited = [[True for _ in range(n)] for _ in range(n)]
                visited[i][j] = False
                que = deque([[i,j]])
                ty,tx = i, j #기준 블록 구하기 위해 필요
                while que:
                    row, col = que.popleft()
                    for dy, dx in dir:
                        yy, xx = row + dy, col + dx
                        if 0 <= yy < n and 0 <= xx < n and visited[yy][xx]:
                            visited[yy][xx] = False
                            if copyed_arr[yy][xx] == 0 :
                                rainbow += 1
                                que.append([yy,xx])
                                blocks.append([yy, xx])
                            elif copyed_arr[yy][xx] == target:
                                que.append([yy,xx])
                                blocks.append([yy, xx])
                                if yy < ty: ty,tx = yy,xx
                                elif yy == ty and xx < tx: ty, tx = yy, xx
                if len(blocks) >= 2:
                    block_group.append([blocks, rainbow, ty,tx])
                    for y,x in blocks:
                        if copyed_arr[y][x] > 0 :
                            copyed_arr[y][x] = -2

    if block_group:
        block_group.sort(key=lambda x: (-len(x[0]), -x[1], -x[2], -x[3]))
        for y,x in block_group[0][0]:
            arr[y][x] = -2
        score += len(block_group[0][0]) *  len(block_group[0][0])
        #step 2 중력이 작용한다
        drop_down()
        #step 3 반시계방향
        arr = turn_left()
        #step 4 다시 중력 작용
        drop_down()
    else:
        break
print(score)