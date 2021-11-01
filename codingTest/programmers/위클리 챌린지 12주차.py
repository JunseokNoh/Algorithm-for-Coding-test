answer = -1
def solution(k, dungeons):
    size = len(dungeons)
    visited = [True for _ in range(size)]

    def DFS(depth, cnt, k, visited):
        global answer
        answer = max(answer, cnt)
        for i in range(size):
            if visited[i] and k >= dungeons[i][0]:
                visited[i] = False
                DFS(depth + 1, cnt + 1, k - dungeons[i][1], visited)
                visited[i] = True

    DFS(0, 0, k, visited)
    return answer

# 일정 피로도를 사용해서 던전 탐험 가능
# 최소 필요 피로도와, 소모 피로도가 있음
#