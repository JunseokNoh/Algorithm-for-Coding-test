import sys
from _collections import deque, defaultdict
N, T = map(int,sys.stdin.readline().split())
visited = defaultdict(list)
for _ in range(N):
    x,y = tuple(map(int,sys.stdin.readline().split()))
    visited[x].append(y)
que = deque([[0,0,0]])
while que :
    x,y,cnt = que.popleft()
    if y == T:
        print(cnt)
        break
    for xx in range(x-2,x+3,1):
        for yy in range(y-2,y+3,1):
            if xx < 0 or yy < 0 : continue
            if yy in visited[xx] :
                visited[xx].remove(yy)
                que.append([xx,yy,cnt+1])
else:
    print(-1)