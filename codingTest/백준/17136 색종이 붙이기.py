import sys

def check(i,j,size,table):
    target = []
    for y in range(size) :
        for x in range(size) :
            yy, xx = i+y, j+x
            if yy < 0 or yy >= 10 or xx < 0 or xx >= 10 :
                return False, []

            if table[yy][xx] == 0 :
                return False, []
            else :
               target.append((yy, xx))

    temp = [[table[y][x] for x in range(10)] for y in range(10)]
    for y,x in target:
        temp[y][x] = 0

    return True, temp

def DFS(table, rest_cnt, papers):
    global result
    if rest_cnt == 0 :
        result = min(result,25 - sum(papers))
        return
    #print(table,rest_cnt,papers)
    for i in range(10):
        for j in range(10):
            if table[i][j] == 1:
                flag = False
                for size in range(1,6):
                    if papers[size] > 0:
                        check_result, temp = check(i,j,size,table)
                        if check_result:
                            papers[size] -= 1
                            DFS(temp,rest_cnt-(size**2),papers)
                            papers[size] += 1
                        flag = True
                if flag:
                    return

table = [list(map(int,sys.stdin.readline().split())) for _ in range(10)]
rest_cnt = 0

for i in range(10):
    for j in range(10):
        if table[i][j] == 1 :
            rest_cnt += 1

papers = [0,5,5,5,5,5]
result = 26


DFS(table, rest_cnt, papers)
if result == 26:
    print(-1)
else:
    print(result)