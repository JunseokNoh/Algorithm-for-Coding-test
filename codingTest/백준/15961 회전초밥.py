import sys
from collections import defaultdict

N, d, k, c = map(int, sys.stdin.readline().split())
belt = [int(sys.stdin.readline()) for _ in range(N)]
table = defaultdict(int)
table[c] = 1
cnt = 1
for i in range(k):
    if table[belt[i]] == 0 :
        cnt += 1
    table[belt[i]] += 1
result = cnt
for start in range(N):
    end = (start+k)%N
    table[belt[start]] -= 1
    if table[belt[start]] == 0 :
        cnt -= 1
    if table[belt[end]] == 0:
        cnt += 1
    table[belt[end]] += 1

    result = max(result, cnt)
print(result)