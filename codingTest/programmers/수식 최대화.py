from collections import deque
from itertools import permutations
def transform(strr):
    tt = list(map(str,strr))
    result = []
    temp = ''
    calex = []
    for i in tt:
        if i.isnumeric():
            temp += i
        else :
            result.append(temp)
            result.append(i)
            if i not in calex:
                calex.append(i)
            temp = ''
    result.append(temp)
    return result, calex

def opcal(a,op,b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b

def cal(elist, op):
    temp = []
    while elist:
        tt = elist.popleft()
        if tt == op :
            a = int(temp.pop())
            b = int(elist.popleft())
            temp.append(opcal(a,tt,b))
        else :
            temp.append(tt)
    return temp

def solution(expression):
    answer = 0
    elist,calex = transform(expression)
    for i in permutations(calex, len(calex)):
        templist = elist
        for j in i:
            templist = cal(deque(templist), j)
        answer = max(answer, abs(int(templist.pop())))
    return answer

if __name__ == "__main__":
    expression = "50*6-3*2"
    print(solution(expression))