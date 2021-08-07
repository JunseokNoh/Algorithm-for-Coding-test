import sys
N = int(sys.stdin.readline())
A = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

A.insert(0, [0] * (N))
for tmp in A :
    tmp.insert(0, 0)

cnt = 0
minval = sys.maxsize

def make_boundary(x,y,d1,d2):
    global minval
    zone = [0] * 5

    #1번구
    val = y
    for i in range(1, x+d1):#행
        if i >= x : val -=1
        for j in range(val,0, -1):
            #print(i,j)
            zone[0] += A[i][j]

    val = 0
    for i in range(1, x+d2+1):
        if i > x : val += 1
        for j in range( y+1+val, N+1, 1):
            zone[1] += A[i][j]

    val = y-d1-1
    for i in range(x+d1, N+1):
        if i <= x + d1 + d2 : val += 1
        for j in range(1, val):
            zone[2] += A[i][j]


    val = y+d2
    for i in range(x+d2+1, N+1):
        for j in range(val, N+1):
            zone[3] += A[i][j]
        if i <= x+d1+d2: val-=1

    left, right = y,y
    for i in range(x, x+d1+d2+1):
        for j in range(left, right+1):
            zone[4] += A[i][j]
        if i < x+d1 : left -=1
        else : left += 1

        if i < x+d2 : right += 1
        else : right -= 1

    minval = min(minval, max(zone) - min(zone))

for y in range(2, N):
    for x in range(1, N-1):
        for d2 in range(1, N - y + 1):
            for d1 in range(1, min(N-(x+d2) + 1, y)):
                make_boundary(x,y,d1,d2)

print(minval)