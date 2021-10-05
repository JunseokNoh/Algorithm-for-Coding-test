def cal(num, ch):
    op = {"S":1, "D":2, "T":3}
    return num**op[ch]

def solution(dartResult):
    dartResult = dartResult.replace('10', 'K')
    dartResult = ['10' if i == "K" else i for i in dartResult]
    size = len(dartResult)
    arr = []
    for index, ch in enumerate(dartResult):
        if dartResult[index].isdecimal() and not dartResult[index+1].isdecimal():
            arr.append(cal(int(dartResult[index]), dartResult[index+1]))
            if index+2 < size:
                if dartResult[index+2] == "*":
                    if len(arr) == 1 :
                        arr[-1] *= 2
                    else:
                        arr[-1] *= 2
                        arr[-2] *= 2
                elif dartResult[index+2] == "#":
                    arr[-1] *= -1
    return sum(arr)


if __name__ == "__main__":
    print(solution("1S2D*3T"))
    print(solution("1D2S#10S"))
    print(solution("1S*2T*3S"))