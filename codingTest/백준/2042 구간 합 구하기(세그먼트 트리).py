import sys
import math

N,M,K = map(int,sys.stdin.readline().split())
#arr는 0~N-1 까지
arr = [int(sys.stdin.readline().rstrip("\n")) for _ in range(N)]
#tree는 가장 크면서 가까운 2^k 사이즈를 가짐
height = int(math.log2(N))+2
#tree는 1부터 index가 시작!!
tree = [0 for _ in range(2**height)]

def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = init(start, mid, index*2) + init(mid+1, end, index*2+1)
    return tree[index]

def sum(start, end, index, left, right):
    if left > end or right < start : return 0
    if left <= start and end <= right : return tree[index]
    mid = (start + end) // 2
    return sum(start,mid,index*2,left,right) + sum(mid+1,end,index*2+1,left,right)

def update(start,end,index,targetindex, diff):
    if targetindex < start or targetindex > end : return
    tree[index] += diff
    if start == end : return
    mid = (start + end) // 2
    update(start, mid, index * 2, targetindex, diff)
    update(mid+1, end, index * 2 + 1, targetindex, diff)

init(0,N-1,1)

for _ in range(M+K):
    a,b,c = map(int,sys.stdin.readline().split())
    if a == 1 :
        diff = c - arr[b-1]
        arr[b - 1] = c
        update(0,N-1,1,b-1,diff)

    if a == 2 :
        print(sum(0,N-1,1,b-1,c-1))
