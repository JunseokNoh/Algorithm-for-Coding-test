import sys
N,C  = map(int,sys.stdin.readline().split())
house = [int(sys.stdin.readline()) for _ in range(N)]
house.sort()

start, end = 1, house[-1] - house[0]
result = 0
while start <= end :
    mid = (start + end) // 2
    before_house = house[0]
    cnt = 1
    for i in range(1, len(house)):
        if before_house + mid <= house[i]:
           cnt += 1
           before_house = house[i]
    if cnt < C :
        end = mid - 1
    else :
        result = mid
        start = mid + 1

print(result)
