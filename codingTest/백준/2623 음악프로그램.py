import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())
table = [[] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]
que = deque()
for _ in range(M):
    temp = list(map(int,sys.stdin.readline().split()))
    for i in range(1,temp[0]):
        table[temp[i]].append(temp[i+1])
        degree[temp[i+1]] += 1

for i in range(1,N+1):
    if degree[i] == 0 :
        que.append(i)

remain_node = N
print_list = []
while que:
    from_node = que.popleft()
    print_list.append(from_node)
    remain_node -= 1
    for to_node in table[from_node]:
        degree[to_node] -= 1
        if degree[to_node] == 0 :
            que.append(to_node)

if remain_node == 0 :
    for i in print_list:
        print(i)
else:
    print(0)