def solution(numbers, hand):
    answer = ''
    pad = {
        1 : (0,0, "L"), 2 : (0,1,"x"), 3 : (0,2, "R"),
        4 : (1,0, "L"), 5 : (1,1,"x"), 6 : (1,2, "R"),
        7 : (2,0, "L"), 8: (2,1,"x"), 9 : (2,2, "R"),
        0 : (3,1,"x")
    }

    ly, lx = 3, 0
    ry, rx = 3, 2

    for num in numbers :
        y,x,h = pad[num]
        if h == 'L' :
            ly, lx = y,x
            answer += h
        elif h == 'R' :
            ry, rx = y,x
            answer += h
        else:
            ldist = abs(y-ly) + abs(x-lx)
            rdist = abs(y-ry) + abs(x-rx)

            if (ldist == rdist and hand == "right") or ldist > rdist:
                ry,rx = y,x
                answer += "R"
            elif (ldist == rdist and hand == "left") or ldist < rdist:
                ly, lx = y,x
                answer += "L"
    return answer


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    hand = "right"
    print(solution(numbers, hand))