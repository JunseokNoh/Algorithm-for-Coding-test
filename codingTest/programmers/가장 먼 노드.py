
from collections import deque

def solution(n, edge):
    table = [True]* (n+1)
    result = [0] * (n+1)
    dictList = dict()

    for i in range(1, n+1) :
        dictList[i] = []

    que = deque()

    for y,x in edge:
        dictList[y].append(x)
        dictList[x].append(y)

    table[1] = False
    for i in dictList[1]:
        table[i] = False
        que.append([i, 1])

    maxval = 0
    while que:
        node, depth = que.popleft()
        result[depth] += 1

        for i in dictList[node]:
            if table[i]:
                table[i] = False
                que.append([i, depth+1])
        maxval = depth

    return result[maxval]

if __name__ == "__main__":
    n = 6
    vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n,vertex))
