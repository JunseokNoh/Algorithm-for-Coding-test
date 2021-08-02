import sys
from itertools import permutations
N,K = map(int,sys.stdin.readline().split())
_map = []
for _ in range(N):
    _map.append(list(map(int,sys.stdin.readline().split())))
p2 = list(map(int,sys.stdin.readline().split()))#경희
p3 = list(map(int,sys.stdin.readline().split()))#민호
target = [i+1 for i in range(N)]

def DFS(pi1,pi2,index,win,player):
    global result
    if win[0] == K:
        result = 1
        return
    if win[1] == K or win[2] == K:
        return
    if index[0] == N:
        return
    pi3 = 3 - (pi1+pi2)
    pv1 = player[pi1][index[pi1]] - 1
    pv2 = player[pi2][index[pi2]] - 1
    index[pi1] += 1
    index[pi2] += 1
    if _map[pv1][pv2] == 2 or (_map[pv1][pv2] == 1 and pi1 > pi2) : #pi1이 이겼을 경우
        win[pi1] += 1
        DFS(pi1, pi3, index, win,player)
    elif (_map[pv1][pv2] == 1 and pi1 < pi2) or _map[pv1][pv2] == 0: #pi2가 이겼을 경우
        win[pi2] += 1
        DFS(pi2, pi3, index, win,player)

for p1 in permutations(target,N):#지우
    player = [p1,p2,p3]
    index = [0,0,0] #지우, 경희, 민호가 다음 번에 낼 손동작 index
    win = [0,0,0] #지우, 경희, 민호 이긴 횟수
    result = 0
    DFS(0,1,index,win,player)
    if result == 1:
        print(1)
        break
else:
    print(0)