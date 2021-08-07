import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

_input = []
_map = [[] for _ in range(N+1)]
degree_table = [0 for _ in range(N+1)]
que = deque()
for _ in range(M) :
    X,Y,K = map(int, sys.stdin.readline().split())
    _map[Y].append([X,K])
    degree_table[X] += 1

cnt_table = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    if degree_table[i] == 0 :
        que.append(i)
        cnt_table[i][i] = 1

while que:
    from_node = que.popleft()
    for to_node, amount in _map[from_node]:
        cnt_table[to_node] = [i + (j * amount) for i,j in zip(cnt_table[to_node], cnt_table[from_node])]
        degree_table[to_node] -= 1
        if degree_table[to_node] == 0 :
            que.append(to_node)

for i,j in enumerate(cnt_table[N]):
    if j > 0 :
        print(i, j)

