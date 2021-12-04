

n = 50

coins = [1,5,10,25]
dp = [0 for _ in range(n+1)]
dp[0] = 1

for coin in coins:
    for money in range(coin,n+1 ㅠㅜ ):
        dp[money] += dp[money-coin]

print(dp[1:])
