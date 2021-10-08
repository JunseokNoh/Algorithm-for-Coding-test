from collections import deque


def BFS(row, col, place):
    que = deque([[row, col, 0]])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[True for _ in range(5)] for _ in range(5)]
    visited[row][col] = False

    while que:
        y, x, depth = que.popleft()
        for dy, dx in dirs:
            yy = y + dy
            xx = x + dx
            if 0 <= yy < 5 and 0 <= xx < 5 and visited[yy][xx]:
                visited[yy][xx] = False
                if place[yy][xx] == 'O':
                    que.append([yy, xx, depth + 1])
                elif place[yy][xx] == 'P' and depth + 1 <= 2:
                    return False
                elif place[yy][xx] == 'P' and depth + 1 > 2:
                    que.append([yy, xx, depth + 1])
    return True


def solution(places):
    answer = []

    for place in places:
        persons = []
        flag = False
        for row in range(5):
            for col in range(5):
                if place[row][col] == 'P':
                    persons.append((row, col))

        for row, col in persons:
            if not BFS(row, col, place):
                answer.append(0)
                break
        else:
            answer.append(1)

    return answer