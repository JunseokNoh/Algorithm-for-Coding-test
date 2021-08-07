n = int(input())
arr = [list(map(str,input())) for _ in range(n)]

def DFS(y,x, leng):
    if leng > 2 :
        leng = leng // 2

        result = []
        result.append(DFS(y, x, leng))
        result.append(DFS(y, x+leng, leng))
        result.append(DFS(y+leng, x, leng))
        result.append(DFS(y+leng, x+leng, leng))

        if len(result[0]) == 1 and result[0] == result[1] == result[2] == result[3]:
            return result[0]
        else:
            return '('+''.join(result)+')'
    else:
        temp = [arr[i][j] for i in range(y,y+leng) for j in range(x,x+leng)]
        if temp[0] == temp[1] == temp[2] == temp[3]:
            return temp[0]
        else:
            return '('+''.join(temp)+')'


print('%s'%DFS(0,0,n),end="")
