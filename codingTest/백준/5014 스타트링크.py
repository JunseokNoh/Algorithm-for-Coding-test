import sys
from collections import deque

F,S,G,U,D = map(int,sys.stdin.readline().split())

hist = [True for _ in range(F+1)]
que = deque()
que.append([S,0])
hist[S] = False

while que:
    current, cnt = que.popleft()

    if current == G :
        print(cnt)
        break

    if current + U <= F and hist[current+U]:
        hist[current+U] = False
        que.append([current+U, cnt + 1])

    if current - D >= 1 and hist[current-D]:
        hist[current-D] = False
        que.append([current-D, cnt + 1])
else :
    print('use the stairs')