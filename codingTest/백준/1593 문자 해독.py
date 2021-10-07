import sys

ws, gs = map(int,sys.stdin.readline().split())
S = str(sys.stdin.readline().rstrip("\n"))
W = str(sys.stdin.readline().rstrip("\n"))
arrs = [0 for _ in range(52)]
arrw = [0 for _ in range(52)]
start, cnt, result = 0,0,0

for s in S:
    if ord('A') <= ord(s) <= ord('Z'):
        arrs[ord(s)-65] += 1
    else:
        arrs[ord(s)-71] += 1

for w in W:
    if 'A' <= w <= 'Z':
        arrw[ord(w) - 65] += 1
    else:
        arrw[ord(w) - 71] += 1
    cnt += 1

    if cnt == ws:
        if arrs == arrw:
            result += 1
        if 'A' <= W[start] <= 'Z':
            arrw[ord(W[start]) - 65] -= 1
        else:
            arrw[ord(W[start]) - 71] -= 1
        start += 1
        cnt -= 1

print(result)