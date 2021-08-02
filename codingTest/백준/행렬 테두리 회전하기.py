def initValue(row, col):
    arr = [[0 for _ in range(row + 1)] for _ in range(col + 1)]
    cnt = 1
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            arr[i][j] = cnt
            cnt += 1
    return arr


def initValue(row, col):
    arr = [[0 for _ in range(row + 1)] for _ in range(col + 1)]
    cnt = 1
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            arr[i][j] = cnt
            cnt += 1
    return arr


def rotate(x1, y1, x2, y2, arr):
    que = []

    for i in range(y1, y2): que.append(arr[x1][i])
    for j in range(x1, x2 + 1): que.append(arr[j][y2])
    for i in range(y2 - 1, y1 - 1, -1): que.append(arr[x2][i])
    for j in range(x2 - 1, x1, -1): que.append(arr[j][y1])

    que.insert(0, que.pop())

    val = min(que)
    for i in range(y1, y2): arr[x1][i] = que.pop(0)
    for j in range(x1, x2 + 1): arr[j][y2] = que.pop(0)
    for i in range(y2 - 1, y1 - 1, -1): arr[x2][i] = que.pop(0)
    for j in range(x2 - 1, x1, -1): arr[j][y1] = que.pop(0)

    return val


def solution(rows, columns, queries):
    answer = []

    arr = initValue(rows, columns)

    for x1, y1, x2, y2 in queries:
        answer.append(rotate(x1, y1, x2, y2, arr))

    return answer

if __name__ == "__main__":
    rows = 100
    columns = 97
    queries = [[1,1,100,97]]
    print(solution(rows,columns, queries))
