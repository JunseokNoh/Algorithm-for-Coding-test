import math

def solution(n, stations, w):
    answer = 0
    bindex, lindex, rindex = 0, 0, 0
    result = []

    for i in stations:

        if i - w < 0: lindex = 1
        else : lindex = i - w

        if i + w > n : rindex = n
        else : rindex = i+w

        #left index - before index - 1 => 전파가 도달하지 않는 아파트의 개수
        if lindex-bindex-1 > 0:
            result.append(lindex-bindex-1)

        bindex = rindex
    #rindex 이후가 전부 비어있을 때
    if rindex < n :
        result.append(n-rindex)

    print(result)

    for i in result:
        answer += math.ceil(i / (2*w+1))

    return answer

if __name__ == "__main__":
    N = 11
    stations = [4,11]
    W = 1
    print(solution(N,stations,W))
