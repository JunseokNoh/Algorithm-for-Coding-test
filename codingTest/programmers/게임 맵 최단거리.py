
def solution(maps):
    answer = -1
    que = []

    dy = [0,-1,0,1]
    dx = [1,0,-1,0]

    n = len(maps) #행
    m = len(maps[0]) #열

    que.append([0,0,1])
    maps[0][0] = 0
    while que :
        y, x, depth = que.pop(0)
        #print(y,x,depth)
        if y == n-1 and x == m-1 :
            answer = depth
            break

        for u in range(4):
            yy, xx = y + dy[u], x + dx[u]
            if 0<= yy < n and 0 <= xx < m :
                if maps[yy][xx] == 1 :
                    maps[yy][xx] = 0
                    que.append([yy,xx, depth+1])

    return answer



if __name__ == "__main__" :
    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    print(solution(maps))