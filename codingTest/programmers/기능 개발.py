
def solution(progresses, speeds):
    answer = []

    while progresses:
        progresses = [progresses[i] + speeds[i] for i in range(len(speeds))]
        cnt = 0
        index = 0
        for i in range(len(progresses)):
            if progresses[i] >= 100 :
                cnt += 1
                index = i
            else :
                break

        if cnt > 0 :
            progresses = progresses[index+1 :]
            speeds = speeds[index+1 :]
            answer.append(cnt)

    return answer

if __name__ == "__main__" :
    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    print(solution(progresses, speeds))