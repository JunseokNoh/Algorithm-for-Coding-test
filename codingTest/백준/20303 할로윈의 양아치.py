import sys
from collections import deque, defaultdict

N,M,K = map(int,sys.stdin.readline().split())
child = list(map(int,sys.stdin.readline().split()))
child.insert(0,0)
graph = defaultdict(list)
hist = [True for _ in range(N+1)]
dp = [[0 for _ in range(K+1)] for _ in range(2)]
table = []

for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for key in graph.keys():
    if hist[key]:
        hist[key] = False
        que = deque([key])
        cnt, result = 0,0
        while que :
            from_node = que.popleft()
            cnt += 1
            result += child[from_node]
            for to_node in graph[from_node]:
                if hist[to_node]:
                    hist[to_node] = False
                    que.append(to_node)
        table.append((cnt,result))

print(table)
for cnt, result in table:
    for i in range(0, K+1):
        if i >= cnt:
            dp[1][i] = max(dp[0][i], dp[0][i-cnt] + result)
        else:
            dp[1][i] = dp[0][i]

    for i in range(0, K+1):
        dp[0][i] = dp[1][i]

print(dp[1][K-1])