import sys
n,m = map(int,sys.stdin.readline().split())
tree = [i for i in range(n+1)]

def find_parent(num):
    if tree[num] == num : return num
    p = find_parent(tree[num])
    tree[num] = p
    return p

def union(a,b):
    a_parent = find_parent(a)
    b_parent = find_parent(b)
    if a_parent != b_parent:
        tree[b_parent] = a_parent

for _ in range(m):
    cal, a, b = map(int,sys.stdin.readline().split())
    if cal == 0:
        union(a,b)
    else :
        a_parent = find_parent(a)
        b_parent = find_parent(b)
        if a_parent != b_parent:
            print("NO")
        else:
            print("YES")