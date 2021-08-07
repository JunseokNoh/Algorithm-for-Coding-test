import sys
from collections import deque

N, K = map(int,sys.stdin.readline().split())
A = deque(list(map(int,sys.stdin.readline().split())))

def rotate():
    A.rotate(1)
    robots.rotate(1)

def move():
    global cnt
    for index in range(N-2,-1,-1):#가장 먼저 벨트에 올라칸 로봇 부
        if robots[index] > 0 :
            target = index+1
            if A[target] > 0 and robots[target] == 0 :#이동하려는 칸에 로봇이 없으며 칸의 내구도가 1이상 남아있음
                A[target] -= 1
                robots[target],robots[index] = 1, 0
                if A[target] == 0 : cnt += 1

stage = 1
robots = deque([0] * 2 * N)
cnt = 0
while 1 :

    rotate()
    robots[N - 1] = 0
    move()
    robots[N - 1] = 0

    if A[0] > 0 and robots[0] == 0 :
        robots[0] = 1
        A[0] -= 1
        if A[0] == 0 : cnt += 1

    if cnt >= K :
        print(stage)
        break
    stage += 1