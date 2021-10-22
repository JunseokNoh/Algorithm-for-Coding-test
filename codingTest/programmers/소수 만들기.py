from itertools import combinations
import math


def isPrime(num):
    if num % 2 == 0:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False

    return True


def solution(nums):
    answer = 0

    for i in combinations(nums, 3):
        if len(set(i)) != 3:
            continue

        if isPrime(sum(i)):
            answer += 1

    return answer