import sys

def solution(s):
    answer = sys.maxsize

    s_len = len(s)
    for i in range(1, s_len // 2 + 1):
        temp = [s[0:i]]
        temp_len = 0
        flag = True
        for j in range(i, s_len, i):
            if temp[-1] == s[j:j+i] and flag:
                temp_len += 1
                flag = False
            elif temp[-1] != s[j:j+i]:
                temp.append(s[j:j+i])
                flag = True
        print(temp, temp_len)
        for xx in temp:
            temp_len += len(xx)

        answer = min(answer, temp_len)
    print(answer)
    return answer

if __name__ == "__main__":
    # s = sys.stdin.readline()
    s = 'axaxxaxaaxaxxaxa' #2a2ba3c
    solution(s)
