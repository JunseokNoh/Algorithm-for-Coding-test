
def solution(s):
    answer = -1
    slist = list(map(str, s))
    target = []

    for i in slist:
        if target and target[-1] == i :
            target.pop()
        else:
            target.append(i)

    if len(target) == 0 :
        return 1
    else :
        return 0

if __name__ == "__main__":
    s = "aaaaaaaabb"
    print(solution(s))