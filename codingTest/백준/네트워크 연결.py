import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
edges = []
for _ in range(M):
    edges.append(list(map(int,sys.stdin.readline().split())))
edges.sort(key=lambda x:(x[2]))

table = [i for i in range(N+1)]
def find_root(index):
    if table[index] == index:
        return index
    parent = find_root(table[index])
    table[index] = parent
    return parent

def union_find(a,b,edge):
    a_root = find_root(a)
    b_root = find_root(b)
    #print(a_root,b_root)
    if a_root != b_root:
        table[b_root] = a_root
        return edge
    else:
        return 0
result = 0
for a,b,edge in edges:
    result += union_find(a,b,edge)
print(result)