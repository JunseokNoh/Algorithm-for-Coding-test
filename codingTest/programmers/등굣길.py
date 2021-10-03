
def solution(m, n, puddles):
    dp = [[1 for _ in range(m)] for _ in range(n)]
    for y,x in puddles:
        dp[x-1][y-1] = 0

    for i in range(2, n):
        dp[i][0] = min(dp[i-1][0], dp[i][0])

    for j in range(2,m):
        dp[0][j] = min(dp[0][j-1], dp[0][j])

    for i in range(1,n):
        for j in range(1,m):
            if dp[i][j] != 0 :
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) %  1000000007

    return dp[n-1][m-1] % 1000000007

if __name__ == "__main__":
    #print(solution(4,3,[[2,2]]))
    print(solution(4,3,[[1,2],[2,1]]))