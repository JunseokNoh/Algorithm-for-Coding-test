def solution(v):
    xList = list(map(lambda x: x[0], v))
    yList = list(map(lambda y: y[1], v))

    result = [xList[0]^xList[1]^xList[2], yList[0]^yList[1]^yList[2]]

    return result


if __name__ == "__main__":
    v = [[1, 4], [3, 4], [3, 10]]
    print(solution(v))