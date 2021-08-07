import sys
import math
n = int(sys.stdin.readline())

result = []

def cal(n):

    while n % 2 == 0:
        result.append(2)
        n = n//2

    i = 3
    while 1 :
        while n % i == 0 :
            result.append(i)
            n = n//i
        i += 2
        if i > math.sqrt(n): break

    if n > 2 :
        result.append(n)

cal(n)

if len(result) == 1 :
    print(-1)
elif len(result) == 3:
    val = 1
    for i in result:
        val *= i
    print(val)
else:
    printval = []
    val = 1
    if len(result) % 2 == 0:
        for i in range(0, len(result), 2):
            printval.append(result[i] * result[i+1])
    else :
        for i in range(0, len(result)-2, 2):
            printval.append(result[i] * result[i+1])
        printval[len(printval)-1] *= result[len(result)-1]

    for i in printval:
        print(i, end=' ')