def transform(num):
    val = []
    while num > 0:
        val.append(str(num % 3))
        num //= 3

    return ''.join(val)


def solution(n):
    return int(transform(n), 3)