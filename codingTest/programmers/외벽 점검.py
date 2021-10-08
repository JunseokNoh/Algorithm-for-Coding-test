from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1
    size = len(weak)

    for i in range(size):
        weak.append(weak[i] + n)

    for i in range(size):
        start = [weak[j] for j in range(i, i + size)]
        for perm_dist in permutations(dist, len(dist)):
            result = 1
            start_index = start[0] + perm_dist[0]
            pindex = 0
            for j in range(1, size):
                if start_index < start[j]:
                    result += 1  # 친구의 수 늘리기
                    if result > len(perm_dist):
                        break
                    pindex += 1
                    start_index = start[j] + perm_dist[pindex]
            answer = min(answer, result)

    if answer > len(dist):
        return -1

    return answer