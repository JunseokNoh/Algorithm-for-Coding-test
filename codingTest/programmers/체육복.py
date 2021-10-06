def solution(n, lost, reserve):
    answer = 0
    arr = [1 for _ in range(n)]

    for l in lost:
        arr[l - 1] = 0

    for r in reserve:
        if r not in lost:
            arr[r - 1] = 2
        elif r in lost:
            arr[r - 1] = 1

    for i in range(n):
        if i - 1 >= 0 and arr[i - 1] == 0 and arr[i] == 2:
            arr[i] -= 1
            arr[i - 1] += 1

        if i + 1 < n and arr[i + 1] == 0 and arr[i] == 2:
            arr[i] -= 1
            arr[i + 1] += 1

    for i in arr:
        if i > 0: answer += 1

    print(arr)
    return answer