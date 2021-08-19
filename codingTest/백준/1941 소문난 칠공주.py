import sys

def DFS(depth,y,x, s_cnt, y_cnt):
    global cnt
    if depth == 7 and s_cnt >= 4 and s_cnt + y_cnt == 7:
        cnt += 1
        return

    for dy, dx in dir:
        yy,xx = dy+y, dx+x
        if hist[yy][xx]:
            if table[yy][xx] == 'S':
                DFS(depth+1, yy, xx, s_cnt+1, y_cnt)
            else:
                DFS(depth+1, yy, xx, s_cnt, y_cnt + 1)

table = [list(map(str, sys.stdin.readline().rstrip("\n"))) for _ in range(5)]
hist = [[True for _ in range(5)] for _ in range(5)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 0
arr = []
for i in range(5):
    for j in range(5):
        if table[i][j] == 'S' and hist[i][j]:
            hist[i][j] = False
            arr.append((i,j))
            DFS(1,i,j,1,0)
            arr.pop()
            hist[i][j] = True


