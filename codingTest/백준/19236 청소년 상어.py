import sys
import copy

fish_arr = [[0 for _ in range(4)] for _ in range(4)]
dir_arr = [[0 for _ in range(4)] for _ in range(4)]
dirs = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]

def find_small_fish(fish_arr):
    fishes = []
    for i in range(4):
        for j in range(4):
            if fish_arr[i][j] > 0 :
                fishes.append(fish_arr[i][j])

    fishes.sort()
    return fishes

def fish_move(fish_arr, dir_arr):
    fishes = find_small_fish(fish_arr)
    for num in fishes:
        y,x = 0,0
        #물고기 찾기
        for i in range(4):
            for j in range(4):
                if fish_arr[i][j] == num :
                    y,x = i,j
                    break

        #step 1 갈 수 있는 방향을 찾는다.
        while True:
            dy, dx = dirs[dir_arr[y][x]]
            yy, xx = y + dy, x + dx
            if 0 > yy or yy >= 4 or 0 > xx or xx >= 4 or fish_arr[yy][xx] <= 0:
                dir_arr[y][x] += 1
                if dir_arr[y][x] == 8:
                    dir_arr[y][x] = 0
                continue
            if fish_arr[yy][xx] > 0 :
                fish_arr[y][x], fish_arr[yy][xx] = fish_arr[yy][xx], fish_arr[y][x]
                dir_arr[y][x], dir_arr[yy][xx] = dir_arr[yy][xx], dir_arr[y][x]
                break

def shark_move(sy,sx,sd,fish_arr,dir_arr,sumVal):
    global result
    target = []
    val = sumVal + fish_arr[sy][sx]
    fish_arr[sy][sx] = -1
    fish_move(fish_arr, dir_arr)

    #먹을 수 있는 물고기 찾기
    dy,dx = dirs[sd]
    while True:
        yy,xx = sy+dy, sx+dx
        if 0 > yy or yy >= 4 or 0 > xx or xx >= 4 :
            break
        if fish_arr[yy][xx] > 0:
            target.append((yy,xx,dir_arr[yy][xx]))

    if len(target) == 0 :
        result = max(result, val)
        return

    for y,x,d in target:
        shark_move(y,x,d,copy.deepcopy(fish_arr),copy.deepcopy(dir_arr),val)

for i in range(4):
    val = list(map(int,sys.stdin.readline().split()))
    for j in range(4):
        fish_arr[i][j] = val[2*j]
        dir_arr[i][j] = val[2*j+1] - 1

sy,sx,sd = 0, 0, dir_arr[0][0]
result = 0
# -1 : 상어, 0 : 아무것도 없음, 0 이상 -> 물고기 있는 것

shark_move(sy,sx,sd,fish_arr,dir_arr,0)

#물고기는 순서대로 이동
#물고기는 한 칸을ㅇ ㅣ동할 수 있으며
#이동ㅎ할 수 있는 칸은 빈칸과 물고기가 있는 칸ㄴ임
#상어가 있거나 공간을 넘어서는 이동 불가
#물고기는 방향이 이동할 수 있는 칸을 향할 때 까지 반시계 45도 씩 회전
#이동할 수 있는 칸이 없으면 이동 x
#물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꿈

# 상어의