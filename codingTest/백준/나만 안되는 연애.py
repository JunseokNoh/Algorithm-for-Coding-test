import sys

N,M = map(int,sys.stdin.readline().split())
college = list(map(str,sys.stdin.readline().split()))
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
    if a_root != b_root:
        table[b_root] = a_root
        return edge, 1
    else:
        return 0, 0
result = 0
edge_cnt = 0
for a,b,edge in edges:
    if college[a-1] != college[b-1]:
        dist, cnt = union_find(a,b,edge)
        result += dist
        edge_cnt += cnt
        if edge_cnt == N-1: break
if edge_cnt != N-1:
    print(-1)
else:
    print(result)