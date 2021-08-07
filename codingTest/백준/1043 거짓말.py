n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

def find_parent(x):
    if parent[x] == x:
        return x
    p = find_parent(parent[x])
    parent[x] = p
    return p

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x != y:
        parent[y] = parent[x]

trueList = list(map(int, input().split()))

for i in range(trueList[0]):
    union(trueList[1], trueList[i + 1])

party = []

for _ in range(m):
    party.append(list(map(int, input().split())))
    party_num = party[-1][0]
    for cur in range(party_num - 1):
        union(party[-1][cur + 1], party[-1][cur + 2])

ans = 0
for i in party:
    for cur in range(i[0]):
        if (len(trueList) > 1 and find_parent(i[cur + 1]) == find_parent(true[1])):
            ans += 1
            break

print(m - ans)