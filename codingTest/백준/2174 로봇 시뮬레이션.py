import sys
from collections import defaultdict

def rotate(cur_dir, turn_dir, cnt):
    directions = {'W': 0, 'S': 1, 'E': 2, 'N': 3}
    directList = ['W', 'S', 'E', 'N']

    dir_num = directions[cur_dir]
    if turn_dir == 'R':
        dir_num -= cnt
        if dir_num < 0:
            rot_cnt = cnt // 4
            dir_num += (rot_cnt + 1) * 4
            dir_num = dir_num % 4
    elif turn_dir == 'L':
        dir_num += cnt
        dir_num = dir_num % 4

    return directList[dir_num]

A, B = map(int, sys.stdin.readline().split())
N, M = map(int, sys.stdin.readline().split())

robots = defaultdict(list)
_map = [[0 for _ in range(A + 1)] for _ in range(B + 1)]

cnt = 1
for _ in range(N):
    temp = list(map(str, sys.stdin.readline().split()))
    x, y, dir = int(temp[0]), int(temp[1]), temp[2]
    _map[y][x] = cnt
    robots[cnt] = [y, x, dir]
    cnt += 1

dir_dict = {'W': (0, -1), 'S': (-1, 0), 'E': (0, 1), 'N': (1, 0)}
for _ in range(M):
    temp = list(map(str, sys.stdin.readline().split()))
    robot_num, cmd, cnt = int(temp[0]), temp[1], int(temp[2])
    ry, rx, dir = robots[robot_num]
    if cmd == 'L' or cmd == 'R':
        dir = rotate(dir, cmd, cnt)
        robots[robot_num] = [ry, rx, dir]
    else:
        for _ in range(cnt):
            ty, tx = ry + dir_dict[dir][0], rx + dir_dict[dir][1]
            if ty < 1 or ty > B or tx < 1 or tx > A:
                print('Robot %d crashes into the wall' % (robot_num))
                exit(0)
            elif _map[ty][tx] > 0 and _map[ty][tx] != robot_num:
                print('Robot %d crashes into robot %d' % (robot_num, _map[ty][tx]))
                exit(0)
            elif _map[ty][tx] == 0:
                _map[ry][rx] = 0
                _map[ty][tx] = robot_num
            ry, rx = ty, tx
        robots[robot_num] = [ry, rx, dir]

print('OK')