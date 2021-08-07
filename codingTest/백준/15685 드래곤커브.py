import sys
N = int(sys.stdin.readline())
dir = [[1,0],[0,-1],[-1,0],[0,1]]

arr = [[0]*101 for _ in range(101)]
def check_arr(hist):
    for x,y in hist:
        arr[y][x] = 1

def dragon_curve(x,y,d,g):
    hist = []
    hist.append([x,y])
    if 0<= x+dir[d][0] <= 100 and 0<= y+dir[d][1] <= 100 :
        hist.append([x+dir[d][0], y+dir[d][1]])
    if g == 0 :
        check_arr(hist)
        return
    else :
        for i in range(g):
            #기준
            tx, ty = hist[len(hist)-1]
            for i in range(len(hist)-2,-1,-1 ):
                dx, dy = hist[i][0] - tx, hist[i][1] - ty
                if 0<= tx-dy <= 100 and 0<= ty+dx <= 100 :
                    hist.append([tx-dy,ty+dx])
        check_arr(hist)
for _ in range(N):
    x,y,d,g = map(int,sys.stdin.readline().split())
    dragon_curve(x,y,d,g)

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1 and arr[i][j+1] == 1 and arr[i+1][j] == 1 and arr[i+1][j+1] == 1 :
           cnt += 1
print(cnt)