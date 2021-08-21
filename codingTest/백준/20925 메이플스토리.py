import sys

N, T = map(int,sys.stdin.readline().split())
records = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
time_table = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp = [[0 if records[i][0] == 0 else -1 for _ in range(T+1)] for i in range(N)]

for j in range(T):
    for i in range(N):
        if dp[i][j] == -1 : continue
        min_exp, exp = records[i][0], records[i][1]
        dp[i][j+1] = max(dp[i][j+1],dp[i][j] + exp)
        for k in range(N):
            if i != k and j + time_table[i][k] <= T and dp[i][j] >= records[k][0]:
                dp[k][j+time_table[i][k]] = max(dp[k][j+time_table[i][k]], dp[i][j])

print(dp)
print(max(map(max,dp)))