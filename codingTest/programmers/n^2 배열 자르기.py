def solution(n, left, right):
    start, end = left // n, right // n
    arr = []
    for i in range(start, end + 1):
        for _ in range(i + 1): arr.append(i + 1)
        for k in range(i + 2, n + 1): arr.append(k)

    return arr[left - start * n:right + 1 - start * n]

# n이 6일때
# 123456 -> 0번째 행은 1이 1개 , 2~6까지 1개씩
# 223456 -> 1번째 행은 2가 2개 , 3~6까지 1개씩
# 333456 -> 2번째 행은 3이 3개 , 4~6까지 1개씩
# 444456 -> 3번째 행은 4이 4개 , 5~6까지 1개씩
# 555556 -> 3번째 행은 5이 5개 , 6~6까지 1개씩
# 666666 -> 3번째 행은 6이 6개
