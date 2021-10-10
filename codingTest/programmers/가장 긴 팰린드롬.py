def solution(s):
    answer = 0
    size = len(s)
    for i in range(0, size):
        l, r = i - 1, i + 1
        cnt = 1
        while True:
            if l < 0 or r >= size:
                break
            if s[l] == s[r]:
                cnt += 2
            elif s[l] != s[r]:
                break
            l -= 1
            r += 1
        answer = max(cnt, answer)

        l, r = i, i + 1
        cnt = 0
        while True:
            if l < 0 or r >= size:
                break
            if s[l] == s[r]:
                cnt += 2
            else:
                break
            l -= 1
            r += 1
        answer = max(cnt, answer)

    return answer