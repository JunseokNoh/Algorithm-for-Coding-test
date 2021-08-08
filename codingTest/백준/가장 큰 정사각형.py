import sys

N,M = map(int,sys.stdin.readline().split())
table = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]
dp = [[0 for _ in range(M)] for _ in range(N)]

val = 0
for i in range(N):
    for j in range(M):
        if i == 0 or j == 0 :
            dp[i][j] = table[i][j]
        elif table[i][j] == 0 :
            dp[i][j] = 0
        elif table[i][j] == 1:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        val = max(dp[i][j], val)

print(val**2)
