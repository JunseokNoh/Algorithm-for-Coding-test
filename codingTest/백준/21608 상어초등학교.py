import sys
from collections import defaultdict

N = int(sys.stdin.readline())
room = [[0 for _ in range(N)] for _ in range(N)]
dict_table = defaultdict(list)
result = [[0 for _ in range(N)] for _ in range(N)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for _ in range(N*N):
    arr = list(map(int,sys.stdin.readline().split()))
    dict_table[arr[0]].extend(arr[1:5])

def likedList(i, j, arr):
    cnt = 0; zeroCnt = 0
    for dy, dx in dir:
        y = i + dy
        x = j + dx
        if 0 <= y < N and 0 <= x < N:
            if room[y][x] in arr:
                cnt += 1
            if room[y][x] == 0:
                zeroCnt += 1

    return cnt, zeroCnt

def result_cal(row,col,num):
    for dy, dx in dir:
        y = row + dy
        x = col + dx
        if 0 <= y < N and 0 <= x < N:
            if room[y][x] != 0 and num in dict_table[room[y][x]]:
                result[y][x] += 1

for num in dict_table.keys():
    liked = []
    for i in range(N):
        for j in range(N):
            if room[i][j] == 0:
                like_cnt, zero_cnt = likedList(i,j,dict_table[num])
                liked.append([like_cnt, zero_cnt, i, j])


    liked.sort(key = lambda x : (-x[0],-x[1], x[2], x[3]))
    liked_cnt, row, col = liked[0][0], liked[0][2], liked[0][3]
    room[row][col] = num
    result[row][col] += liked_cnt
    result_cal(row,col,num)

score = { 0:0, 1:1, 2:10, 3:100, 4:1000 }
sumval = 0
for i in range(N):
    for j in range(N):
        sumval += score[result[i][j]]

print(sumval)