import sys
import copy
answer = 0

def DFS(index,depth, n, queens, before_row):
    global answer
    if depth == n :
        answer += 1
        return

    while index < n**2:
        i = index // n
        j = index % n
        if j not in queens:
            for r, c in enumerate(queens):
                if c == -1 : continue
                if abs(r-i) == abs(c-j) : break
            else :
                queens[i] = j
                DFS((i+1)*n,depth+1, n, copy.deepcopy(queens), i)
        if i > before_row + 1: break
        index += 1

def solution(n):
    queens = [-1 for _ in range(n)]
    DFS(0,0,n,queens,-1)
    return answer

if __name__ == "__main__":
    print(solution(11))