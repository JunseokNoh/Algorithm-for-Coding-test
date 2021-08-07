

def solution(scoville, K):
    answer = 0
    scoville.sort()
    scoville.insert(0, -1)

    while True :

        if scoville[1] < K :
            if len(scoville) == 2 :
                return -1
            first = minPop(scoville)
            second = minPop(scoville)
            scoville = addHead(first + (second * 2) , scoville)
            answer += 1
        else :
            break


    return answer


def minPop(scoville):
    scoville[1], scoville[-1] = scoville[-1], scoville[1]

    val = scoville.pop()

    parent = 1
    child = parent * 2
    if (child + 1) < len(scoville) and scoville[child] > scoville[child+1] :
        child += 1

    while child < len(scoville) and scoville[parent] > scoville[child]:
        scoville[parent], scoville[child] = scoville[child], scoville[parent]

        parent = child
        child = parent * 2
        if child + 1 < len(scoville) and scoville[child] > scoville[child + 1]:
            child += 1

    return val

def addHead(val, scoville):
    scoville.append(val)
    leng = len(scoville)

    child = leng-1
    while True:
        parent = (child // 2)
        if parent < 1 : break
        if scoville[child] < scoville[parent] :
            scoville[child], scoville[parent] = scoville[parent], scoville[child]
        child = parent
    return scoville

if __name__  == "__main__" :
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    print(solution(scoville, K))

    print(solution([0, 0, 0, 0], 7), -1)
    print(solution([0, 0, 3, 9, 10, 12], 7000), -1)
    print(solution([0, 0, 3, 9, 10, 12], 0), 0)
    print(solution([0, 0, 3, 9, 10, 12], 1), 2)
    print(solution([0, 0], 0), 0)
    print(solution([0, 0], 1), -1)
    print(solution([1, 0], 1), 1)