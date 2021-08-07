import sys

answer = 0

def DFS(depth, sumval,numbers,  target):
    global answer
    if depth == len(numbers) and sumval == target:
        answer += 1

    if depth == len(numbers):
        return

    DFS(depth + 1, sumval + numbers[depth], numbers, target)
    DFS(depth + 1, sumval - numbers[depth], numbers, target)


def solution(numbers, target):
    global answer

    DFS(1, numbers[0], numbers, target)
    DFS(1, -numbers[0], numbers,  target)
    return answer




print(solution([1, 1, 1, 1, 1], 3))
