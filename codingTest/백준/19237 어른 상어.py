import sys

N, M, K = map(int, sys.stdin.readline().split())
# N : 가로세로 , M : 상어 수, K : 최대 이동 수
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
current_dir = list(map(int, sys.stdin.readline().split()))
time_cnt = 0
total_shark_cnt = M
shark_prior_dir = [list(map(int, sys.stdin.readline().split())) for _ in range(M * 4)]
#current_dir = shark_init_dir
current_shark_loc = [[] for _ in range(M)]
#smell = [[0] * N for _ in range(N)]
smell_shark = [[-1] * N for _ in range(N)]
smell_time = [[0] * N for _ in range(N)]

shark_location_hist = []
shark_list = [i for i in range(M)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if grid[i][j] > 0:
            current_shark_loc[grid[i][j] - 1] = [i, j, grid[i][j] - 1]
            smell_shark[i][j] = grid[i][j] - 1
            smell_time[i][j] = K
            shark_location_hist.append([i, j])


def move(shark_num):
    global total_shark_cnt
    iy, ix, shark_num_tmp = current_shark_loc[shark_num]
    tmp_dir = current_dir[shark_num]  # 1,2,3,4 : 위 아래 왼쪽 오른쪽
    tmp_prior = shark_prior_dir[(shark_num * 4) + tmp_dir - 1]
    shark_self_smell = []

    for i in tmp_prior:
        y, x = iy + dy[i - 1], (ix + dx[i - 1])
        if 0 <= y < N and 0 <= x < N:
            if smell_shark[y][x] == -1:  # 향기가 없으면
                current_shark_loc[shark_num] = [y, x, shark_num]
                current_dir[shark_num] = i
                break
            elif smell_shark[y][x] == shark_num:  # 자신의 향기일 경우 히스토리 저장:
                shark_self_smell.append([y, x, i])
    else:  # 사방이 향기로 가득차 있으면 자신의 향기로 이동
        if len(shark_self_smell) > 0:
            y, x, dir = shark_self_smell.pop(0)
            current_shark_loc[shark_num] = [y, x, shark_num]
            current_dir[shark_num] = dir
            if [y, x] not in shark_location_hist:
                shark_location_hist.append([y, x])

def smell_timer():
    tmp_shark_location_hist = []
    for i, j in shark_location_hist:
        if smell_time[i][j] > 0:
            smell_time[i][j] -= 1
            if smell_time[i][j] == 0:
                smell_shark[i][j] = -1
                smell_time[i][j] = 0
            else:
                tmp_shark_location_hist.append([i, j])
    return tmp_shark_location_hist
    # 이 방법으로 하면 느리니까
    # 상어마다 향기의 위치를 다 파악해서 줄여야 할듯


while 1:
    if time_cnt >= 1000:
        print(-1)
        sys.exit()
        break

    delete_list = []
    #1동시에 상어를 다 움직인다
    for i in range(len(shark_list) - 1, -1, -1):
        if shark_list[i] != -1 :
        # 살아있는 shark들만 move
            move(shark_list[i])

    shark_location_hist = smell_timer()

    for i in range(len(shark_list) - 1, -1, -1):
        if shark_list[i] != -1:
            y, x, shark_num = current_shark_loc[shark_list[i]]
            if smell_shark[y][x] > 0 and smell_shark[y][x] > shark_num:
                target_num = smell_shark[y][x]
                shark_list[target_num] = -1
                total_shark_cnt -= 1
            smell_shark[y][x] = shark_num
            smell_time[y][x] = K
            if [y, x] not in shark_location_hist:
                shark_location_hist.append([y, x])
    time_cnt += 1

    if total_shark_cnt == 1: break
print(time_cnt)
