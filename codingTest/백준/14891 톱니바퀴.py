from collections import deque
arr = []
for _ in range(4):
    arr.append(deque(list(map(int, input()))))
K = int(input())

def rotate(i, dir):
    #시계방향
    if dir == 1 :
        arr[i].insert(0,arr[i].pop())
    #반시계방향
    elif dir == -1:
        arr[i].append(arr[i].popleft())

for _ in range(K):
    i, dir = map(int,input().split())
    rotate_arr = [[i-1,dir]]

    #오른쪽
    x = i-1
    histdir = dir
    while x + 1 <= 3:
        if arr[x][2] != arr[x+1][6] :
            histdir = -histdir
            rotate_arr.append([x+1, histdir])
        elif arr[x][2] == arr[x+1][6]:
            break
        x += 1

    #왼
    x = i-1
    histdir = dir
    while x - 1 >= 0 :
        if arr[x][6] != arr[x-1][2]:
            histdir = -histdir
            rotate_arr.append([x -1, histdir])
        elif arr[x][6] == arr[x-1][2]:
            break
        x -= 1
    for x, dd in rotate_arr:
        rotate(x,dd)

print(arr[0][0] * 1 + arr[1][0] * 2 + arr[2][0] * 4 + arr[3][0] * 8)
