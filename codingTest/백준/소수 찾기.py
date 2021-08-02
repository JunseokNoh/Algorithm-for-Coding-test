import math

def solution(numbers):
    answer = 0
    numbers = list(map(str, numbers))
    n = len(numbers)

    visited = [True]*n
    result = set()
    for i in range(n):
        if visited[i]:
            visited[i] = False
            DFS(numbers[i], 1, n, numbers, visited, result)
            visited[i] = True

    resultList = list(result)

    resultList.sort()
    #print(resultList)
    for i in range(len(resultList)):
        if isPrime(resultList[i]):
            #print(resultList[i])
            answer += 1

    return answer

def isPrime(num):
    if (num > 2 and num % 2 == 0) or num <= 1:
        return False

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False

    return True

def DFS(num, depth, n, numbers, visited, result):
    result.add(int(num))

    if depth == n :
        return

    for i in range(n):
        if visited[i]:
            visited[i] = False
            DFS(num + numbers[i], depth+1, n, numbers, visited, result)
            visited[i] = True

if __name__ == "__main__":
    numbers = "2"
    numList = list(map(str,numbers))
    print(solution(numbers))

# 맨 앞에 0일 경우 예외처리
# 중복되는 숫자 처리
# result에 다 때려 박고 최종적으로 소수의 개수 구하기