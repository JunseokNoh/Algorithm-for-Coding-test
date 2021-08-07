
def solution(numbers):
    num = [str(i) for i in numbers]
    num.sort(key=lambda x: x * 2, reverse=True)
    return str(int(''.join(num)))

if __name__ == "__main__":
    numbers = [1,55,75,134,23,9,98,99]
    print(solution(numbers))

# 예를 들어, ‘121’과 ‘12’의 경우 ‘121121121’과 ‘121212’를 비교하게 됩니다.
# 두 문자열 중 ‘12’가 먼저 앞으로 와야되는데, str 비교 방식으로 4번째 idx에서 ‘121212’가 더 크다고 인식하게 됩니다.


#999987555231341
