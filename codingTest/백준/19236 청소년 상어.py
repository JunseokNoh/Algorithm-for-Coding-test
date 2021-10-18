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

def fish_move(fish_arr, dir_arr, sy, sx):
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
        temp_d = dir_arr[y][x]
        for _ in range(8):
            dy, dx = dirs[temp_d]
            yy, xx = y + dy, x + dx
            if 0 > yy or yy >= 4 or 0 > xx or xx >= 4 or (yy == sy and xx == sx):
                temp_d += 1
                if temp_d == 8:
                    temp_d = 0
                continue
            if fish_arr[yy][xx] >= 0:
                dir_arr[y][x] = temp_d
                fish_arr[y][x], fish_arr[yy][xx] = fish_arr[yy][xx], fish_arr[y][x]
                dir_arr[y][x], dir_arr[yy][xx] = dir_arr[yy][xx], dir_arr[y][x]
                break

def shark_move(sy,sx,sd,fish_arr,dir_arr,sumVal):
    global result

    val = sumVal + fish_arr[sy][sx]
    result = max(result, val)

    fish_arr[sy][sx] = 0
    fish_move(fish_arr, dir_arr, sy, sx)

    #먹을 수 있는 물고기 찾기
    dy,dx = dirs[sd]
    while True:
        yy,xx = sy+dy, sx+dx
        if 0 <= yy < 4 and 0 <= xx < 4 :
            if fish_arr[yy][xx] > 0:
                shark_move(yy, xx, dir_arr[yy][xx], copy.deepcopy(fish_arr), copy.deepcopy(dir_arr), val)
        else : break
        sy, sx = yy,xx

for i in range(4):
    val = list(map(int,sys.stdin.readline().split()))
    for j in range(4):
        fish_arr[i][j] = val[2*j]
        dir_arr[i][j] = val[2*j+1] - 1

result = 0
shark_move(0,0,dir_arr[0][0],fish_arr,dir_arr,0)

print(result)