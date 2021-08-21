import sys

N, T = map(int,sys.stdin.readline().split())
records = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
time_table = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp = [[0 for _ in range(T+1)] for _ in range(N)]

for j in range(0, T+1):
    for i, value in enumerate(records):
        min_exp, exp = value[0], value[1]
        dp[i][j+1] = dp[i][j] + exp
        for k in range(0,N):
            if i != k and j + time_table[i][k] <= T and dp[i][j] >= min_exp:
                dp[k][j+time_table[i][k]] = max(dp[k][j+time_table[i][k]], dp[i][j])

print(max(map(max, dp)))


