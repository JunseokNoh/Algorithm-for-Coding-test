def DFS(n,index, computers, arr):

    for j in range(index + 1,n):
        if computers[index][j] == 1:
            arr.append(computers[index][j])
            DFS(n,computers[index][j], computers, arr)


def solution(n, computers):
    answer = 0
    arr = []
    for i in range(0, n):
        for j in range(i + 1, n):
            #print(i,j)
            if computers[i][j] == 1:
                arr.append(i)
                arr.append(computers[i][j])
                #print(n,computers[i][j],computers, arr)
                DFS(n,computers[i][j], computers, arr)

    return answer

a = [[1,1,1,0], [1,1,0,1], [1,0,1,1], [0,1,1,1]]
print(solution(3, a))
