import sys

N, M, K = map(int,sys.stdin.readline().split())
arr = [[[] for _ in range(N+1)] for _ in range(N+1)]
fires_infos = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]

def move(row, col, s, d):
    if d == 7 or d == 0 or d == 1:
        row -= s
        if row <= 0:
            row = abs(row)
            row = N - (row % N)

    if d == 7 or d == 6 or d == 5:
        col -= s
        if col <= 0 :
            col = abs(col)
            col = N - (col % N)

    if d == 5 or d == 4 or d == 3:
        row += s
        row %= N
        if row == 0 : row = N

    if d == 1 or d == 2 or d == 3:
        col += s
        col %= N
        if col == 0: col = N

    return row, col

def check(val):
    odd, even = 0, 0
    for item in val:
        if item % 2 == 0 : even += 1
        else: odd += 1
    if odd > 0 and even > 0 :
        return False
    else:
        return True

for _ in range(K):
    arr = [[[] for _ in range(N+1)] for _ in range(N+1)]
    for fires_info in fires_infos:
        r,c,m,s,d = fires_info
        r,c = move(r,c,s,d)
        arr[r][c].append([r,c,m,s,d])

    new_fires_infos = []
    for i in range(1,N+1):
        for j in range(1,N+1):
            fire_cnt = len(arr[i][j])
            if fire_cnt == 1:
                new_fires_infos.extend([arr[i][j]][0])
            if fire_cnt >= 2:
                new_m = 0; new_s = 0; new_d = []
                for r,c,m,s,d in arr[i][j]:
                    new_m += m
                    new_s += s
                    new_d.append(d)

                new_m = new_m//5
                new_s = new_s//fire_cnt
                if check(new_d): d_list = [0,2,4,6]
                else: d_list = [1,3,5,7]
                if new_m > 0:
                    for k in range(4):
                        new_fires_infos.append([i,j,new_m,new_s,d_list[k]])

    fires_infos = new_fires_infos

sumval = 0
for info in fires_infos:
    sumval += info[2]
print(sumval)