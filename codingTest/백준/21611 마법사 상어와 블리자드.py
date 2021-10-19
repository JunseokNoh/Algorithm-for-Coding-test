import sys

n,m = map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dirs = [(0,0),(-1,0),(1,0),(0,-1),(0,1)]
y,x = (n+1)//2 - 1, (n+1)//2 - 1

def throw_ice(y,x,d,s):
    dy,dx = dirs[d]
    for i in range(s):
        y, x = y + dy, x + dx
        arr[y][x] = -1

def move(n,s):
    dirs = [(0, -1), (1, 0),(0, 1),(-1, 0)]
    # 왼 아래 오른 위
    for _ in range(s):
        y,x = (n+1)//2 - 1, (n+1)//2 - 1
        d = 0
        dist = 1
        while True:
            flag = False
            for _ in range(dist):
                dy, dx = dirs[d]
                yy,xx = y + dy, x + dx
                if 0 <= yy < n and 0 <= xx < n:
                    if arr[y][x] == -1 and arr[yy][xx] > 0 :
                        arr[yy][xx], arr[y][x] = arr[y][x], arr[yy][xx]
                    elif arr[y][x] == -1 and arr[yy][xx] == 0:
                        flag = True
                        break
                else:
                    flag = True
                    break
                y,x = yy,xx
            if flag: break
            d += 1
            if d == 4 : d = 0
            if d == 2 or d == 0 :
                dist += 1

def find():
    result = []
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]    # 왼 아래 오른 위
    y, x = (n + 1) // 2 - 1, (n + 1) // 2 - 1
    d, dist = 0, 1
    temp = []
    while True:
        flag = False
        for _ in range(dist):
            dy, dx = dirs[d]
            yy, xx = y + dy, x + dx
            if 0 <= yy < n and 0 <= xx < n:
                if arr[y][x] != arr[yy][xx] :
                    if len(temp) >= 4 :
                        for i in temp :
                            result.append(i)
                    temp.clear()
                    temp.append([yy,xx])
                elif arr[y][x] == arr[yy][xx] :
                    temp.append([yy,xx])
                if arr[yy][xx] <= 0 :
                    flag = True
                    break
            else:
                flag = True
                break
            y, x = yy, xx
        if flag: break
        d += 1
        if d == 4: d = 0
        if d == 2 or d == 0:
            dist += 1

    if len(temp) >= 4:
        for i in temp:
            result.append(i)
    return result

def get_newVal():
    result = []
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 왼 아래 오른 위
    y, x = (n + 1) // 2 - 1, (n + 1) // 2 - 1
    d, dist = 0, 1
    temp = []
    while True:
        flag = False
        for _ in range(dist):
            dy, dx = dirs[d]
            yy, xx = y + dy, x + dx
            if 0 <= yy < n and 0 <= xx < n:
                if arr[y][x] != arr[yy][xx] and arr[y][x] > 0:
                    if len(temp) >= 1:
                        result.append(len(temp))
                        for r,c in temp:
                            result.append(arr[r][c])
                            break
                        temp.clear()
                elif arr[yy][xx] <= 0:
                    flag = True
                    break
                temp.append([yy, xx])
            else:
                flag = True
                break
            y, x = yy, xx
        if flag: break
        d += 1
        if d == 4: d = 0
        if d == 2 or d == 0:
            dist += 1

    return result

def get_newArr(result):
    temp = [[0 for _ in range(n)] for _ in range(n)]
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 왼 아래 오른 위
    y, x = (n + 1) // 2 - 1, (n + 1) // 2 - 1
    d, dist = 0, 1
    index = 0
    while True:
        flag = False
        for _ in range(dist):
            dy, dx = dirs[d]
            yy, xx = y + dy, x + dx
            if 0 <= yy < n and 0 <= xx < n and index < len(result):
                temp[yy][xx] = result[index]
                index += 1
            else:
                flag = True
                break
            y, x = yy, xx
        if flag: break
        d += 1
        if d == 4: d = 0
        if d == 2 or d == 0:
            dist += 1

    return temp

answer = 0
for _ in range(m):
    d, s = map(int, sys.stdin.readline().split())
    throw_ice(y,x,d,s)
    move(n, s)
    while True:
        result = find()
        if len(result) == 0 : break
        for r,c in result:
            answer += arr[r][c]
            arr[r][c] = -1
        move(n, len(result))
    result = get_newVal()
    arr = get_newArr(result)

print(answer)
# 상어는 di 방향으로 거리가 si 이하인 모든 칸에 얼음 파편을 던지고
# 그 칸에 있는 모든 구슬을 파괴한다.
