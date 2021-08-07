import sys
from _collections import deque

N,M,T = map(int,sys.stdin.readline().split())
stencil = [ [ ] for _ in range(1) ] * (N+1)
stencil = deque(stencil)
for i in range(1,N+1):
    stencil[i] = list(map(int,sys.stdin.readline().split()))
total = N * M

def move(x,d,k):
    for i in range(x,N+1,x):
        #시계 방향
        if d == 0 :
            for _ in range(k):
                stencil[i].insert(0, stencil[i].pop())
        elif d == 1:
            for _ in range(k):
                stencil[i].append(stencil[i].pop(0))
def delete():
    global total
    hist = set()
    #수평 방향먼저
    for i in range(1,N+1):
        for j in range(M):
            y1,x1 = i, j+1
            y2,x2 = i, j-1
            if x1 == M : x1 = 0
            if x2 == -1 : x2 = M-1
            if 0 < stencil[i][j] == stencil[y1][x1] > 0:
                hist.add((i,j))
                hist.add((y1,x1))
            if 0 < stencil[i][j] == stencil[y2][x2] > 0:
                hist.add((i, j))
                hist.add((y2, x2))
    #수직 방향
    for i in range(M):
        for j in range(1,N+1):
            y1,x1 = j+1,i
            y2,x2 = j-1,i
            if y1 <= N and 0<stencil[j][i] == stencil[y1][x1] > 0 :
                hist.add((j,i))
                hist.add((y1,x1))
            if 0 < y2 and 0 < stencil[j][i] == stencil[y2][x2] > 0:
                hist.add((j,i))
                hist.add((y2,x2))
    if len(hist) >0 :
        for y,x in hist:
            stencil[y][x] = 0
            total  -= 1
    else :
        if total != 0 :
            avg = sum(map(sum, stencil)) /  total
            for i in range(1,N+1):
                for j in range(M):
                    if stencil[i][j] > avg : stencil[i][j] -=1
                    elif 0< stencil[i][j] < avg : stencil[i][j] += 1
for i in range(T):
    x, d, k = map(int,sys.stdin.readline().split())
    move(x,d,k)
    delete()
print(sum(map(sum,stencil)))