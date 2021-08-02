import sys

N, M = map(int, sys.stdin.readline().split())
personList = [False] * (N+1)
person = list(map(int,sys.stdin.readline().split()))[1:]
for p in person:
    personList[p] = True

partyList = []
for _ in range(M):
    tmp = list(map(int, sys.stdin.readline().split()))[1:]
    partyList.append(tmp)

def trueCheck():
    for party in partyList:
        for i in party:
            if personList[i]:
                for j in party : personList[j] = True
                break

def personCount():
    cnt = 0
    for party in partyList:
        for p in party:
            if personList[p]: break
        else:
            cnt += 1
    return cnt

before = 50
while True:
    trueCheck()
    cnt = personCount()
    if cnt == before : break
    before = cnt

print(cnt)


# 파티에 진실을 아는 사람이 있으면 과장을 할 수 없다.
# 파티에 진실을 모르면 과장을 해도 된다는 뜻
# 파티에 한명이라도 진실을 알고잇으면 연관된 사람을 다 personList를 True로 바꿈