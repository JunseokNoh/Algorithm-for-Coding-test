import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maze = [list(map(int, input())) for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
visited = [[[True] * 2 for _ in range(m)] for _ in range(n)]
que = deque()
que.append([0, 0, 1, 1])
minval = sys.maxsize
while que:
    y, x, distance, cnt = que.popleft()

    if y == n - 1 and x == m-1:
        minval = distance
        break

    for u in range(4):
        yy = y + dy[u]
        xx = x + dx[u]
        if 0 <= yy < n and 0 <= xx < m  and visited[yy][xx][cnt]:
            if maze[yy][xx] == 0:
                que.append([yy, xx, distance + 1, cnt])
                visited[yy][xx][cnt] = False

            if cnt == 1 and maze[yy][xx] == 1:
                que.append([yy, xx, distance + 1, 0])
                visited[yy][xx][0] = False

if minval == sys.maxsize:
    print(-1)
else:
    print(minval)