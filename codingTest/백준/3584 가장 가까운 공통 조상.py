import sys
def find(A, parent, arr):
    while parent[A] != -1:
        arr.append(parent[A])
        A = parent[A]

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    parent = [-1 for _ in range(N+1)]
    for _ in range(N-1):
        A,B = map(int,sys.stdin.readline().split())
        parent[B] = A
    A,B = map(int,sys.stdin.readline().split())
    arr1,arr2 = [A], [B]
    find(A,parent,arr1)
    find(B,parent,arr2)
    flag = False
    for i in arr1:
        for j in arr2:
            if i == j :
                print(i)
                flag = True
                break
        if flag : break
