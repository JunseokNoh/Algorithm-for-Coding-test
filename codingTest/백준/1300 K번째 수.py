import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

start, end = 1, K
result = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(1,N+1):
        cnt += min(mid//i, N)
    if cnt < K :
        start = mid + 1
    else :
        result = mid
        end = mid - 1

print(result)