import sys
from collections import deque

R,C = map(int,sys.stdin.readline().split())
_map = [list(map(str,sys.stdin.readline().rstrip("\n"))) for _ in range(R)]
fire_que,ji_que = deque(), deque()
ji_map = [[True for _ in range(C)] for _ in range(R)]

for i in range(R):
    for j in range(C) :
        if _map[i][j] == 'J':
            _map[i][j] = '.'
            ji_map[i][j] = False
            ji_que.append([i, j, 0])
        else:
            if _map[i][j] == 'F':
                fire_que.append([i,j,0])

dy = [-1,0,1,0]
dx = [0,1,0,-1]
before_fire_cnt, before_ji_cnt = 0, -1
while ji_que:
    jy,jx,cnt = ji_que.popleft()

    if jy == R-1 or jy == 0 or jx == C-1 or jx == 0:
        print(cnt+1)
        break

    if before_ji_cnt != cnt :
        before_ji_cnt = cnt
        while fire_que:
            fy, fx,fire_cnt = fire_que.popleft()
            if before_fire_cnt != fire_cnt:
                before_fire_cnt = fire_cnt
                fire_que.appendleft([fy,fx,fire_cnt])
                break
            for u in range(4):
                ffy = fy + dy[u]
                ffx = fx + dx[u]
                if 0 <= ffy < R and 0 <= ffx < C and _map[ffy][ffx] == '.':
                    _map[ffy][ffx] = 'F'
                    fire_que.append([ffy,ffx,fire_cnt+1])

    for u in range(4):
        jjy = jy + dy[u]
        jjx = jx + dx[u]
        if 0 <= jjy < R and 0 <= jjx < C and _map[jjy][jjx] == '.' and ji_map[jjy][jjx]:
            ji_map[jjy][jjx] = False
            ji_que.append([jjy,jjx,cnt+1])
else:
    print("IMPOSSIBLE")