import sys
N = int(sys.stdin.readline())
man = list(map(int, sys.stdin.readline().split()))
woman = list(map(int,sys.stdin.readline().split()))

m_plus = sorted([i for i in man if i > 0])
m_minus = sorted([i for i in man if i < 0], reverse=True)
w_plus = sorted([i for i in woman if i > 0])
w_minus = sorted([i for i in woman if i < 0], reverse=True)

def calForResult(plus, minus):
    i,j = 0,0
    cnt = 0
    while i < len(plus):
        while j < len(minus):
            if plus[i] + minus[j] < 0 :
                j += 1
                cnt += 1
                break
            else :
                j += 1
        if j == len(minus) :
            break
        i += 1
    return cnt

cnt = calForResult(m_plus,w_minus)
cnt += calForResult(w_plus,m_minus)
print(cnt)