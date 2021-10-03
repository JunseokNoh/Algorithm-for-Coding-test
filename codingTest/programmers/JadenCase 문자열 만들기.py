
def solution(s):
    answer = ''
    for word in s.split(" ") :
        for i in range(len(word)):
            if i == 0 and word[i].isalpha():
                answer += word[i].upper()
            elif i != 0 and word[i].isalpha():
                answer += word[i].lower()
            else :
                answer += word[i]
        answer += " "
    return answer[0:len(answer)-1]


if __name__ == "__main__":
    print(solution("3people unFollowed me"))
    print(solution("for the last week"))