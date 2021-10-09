answer = 0

def DFS(row, n, queens):
    global answer
    if row == n :
        answer += 1
        return

    for col in range(n):
        queens[row] = col
        flag = True
        for r, c in enumerate(queens):
            if r >= row : break
            if row - r == abs(col - c) or (r < row and c == col):
                #row보다 작은 queen들 중에서 대각선에 있거나, 같은 열에 있을 경우는 중단
                flag = False
                break
        if flag:
            DFS(row+1, n, queens)

def solution(n):
    queens = [-1 for _ in range(n)]
    DFS(0,n,queens)
    return answer

if __name__ == "__main__":
    print(solution(12))