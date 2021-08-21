input = __import__('sys').stdin.readline

n, t = map(int, input().split())
c, e = [], []
for i in range(n) :
    ci, ei = map(int, input().split())
    c.append(ci)
    e.append(ei)
a = [list(map(int, input().split())) for i in range(n)]
dp = [[0]*(t+1) for i in range(n)]
for i in range(n) :
    if c[i] > 0 :
        dp[i][0] = -112312312345

ans = -1
for now in range(1, t+1) :
    for here in range(n) :
        dp[here][now] = dp[here][now - 1] + e[here]
        for there in range(n) :
            if here != there and now - a[there][here] >= 0 and dp[there][now - a[there][here]] >= c[here] :
                dp[here][now] = max(dp[here][now], dp[there][now - a[there][here]])
        ans = max(ans, dp[here][now])
print(dp)
print(ans)