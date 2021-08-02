
def solution(answers):
    answer = []

    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]

    n1,n2,n3 = len(p1), len(p2), len(p3)
    c1,c2,c3 = 0,0,0

    for i in range(len(answers)):
        if answers[i] == p1[i % n1] : c1 += 1
        if answers[i] == p2[i % n2]: c2 += 1
        if answers[i] == p3[i % n3]: c3 += 1

    target = [c1,c2,c3]
    #print(target)
    maxval = max(target)

    for i in range(3):
        if maxval == target[i] :
            answer.append(i+1)


    return answer

if __name__ == "__main__":
    answers = [1,3,2,4,2]
    print(solution(answers))
3