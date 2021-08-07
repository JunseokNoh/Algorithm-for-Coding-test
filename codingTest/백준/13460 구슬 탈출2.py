import sys

N, M = map(int, input().split())
board_tmp = [list(input()) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if board_tmp[i][j] == 'R':
            R_index = [i, j]
        elif board_tmp[i][j] == 'B':
            B_index = [i, j]

result = 100
flag = True

def cutEdge(i, rty, rtx, bty, btx, board):
    rty, rtx, bty, btx = rty, rtx, bty, btx
    # 벽이 아니거나, 구슬이 없다면 이동
    rdy, rdx = rty + dy[i], rtx + dx[i]
    bdy, bdx = bty + dy[i], btx + dx[i]

    if rdy < 1 or rdy >= N - 1 or rdx < 1 or rdx >= M - 1 or board[rdy][rdx] == '#':
        rdy, rdx = rty, rtx

    if bdy < 1 or bdy >= N - 1 or bdx < 1 or bdx >= M - 1 or board[bdy][bdx] == '#':
        bdy, bdx = bty, btx

    if board[rdy][rdx] == board[rty][rtx] and board[bdy][bdx] == board[bty][btx]:
        return True
    else :
        return False

# depth , dir, 빨간 공위치, 파란 공위치,킵
def DFS(depth, dir, ry, rx, by, bx, board):
    global result, flag
    if depth > 10 or result < depth:
        return
    else:
        rty, rtx, bty, btx = ry, rx, by, bx
        while 1:
            # 벽이 아니거나, 구슬이 없다면 이동
            rdy, rdx = rty + dy[dir], rtx + dx[dir]
            bdy, bdx = bty + dy[dir], btx + dx[dir]

            if rdy < 1 or rdy >= N - 1 or rdx < 1 or rdx >= M-1 or board[rdy][rdx] == '#' :
                rdy, rdx = rty, rtx

            if bdy < 1 or bdy >= N - 1 or bdx < 1 or bdx >= M-1 or board[bdy][bdx] == '#' :
                bdy, bdx = bty, btx

            if rdy == bdy and rdx == bdx :
                break

            #같은 행 이나 같은 열에 있고 그 사이에 다 . 이라면 ?
            if board[rdy][rdx] == 'O':
                if rdy == bdy and (dir == 1 or dir ==3):
                    y, x = bdy,bdx
                    for i in range(abs(rdx-bdx)):
                        y, x = y + dy[dir] , x + dx[dir]
                        if board[y][x] == '#':
                            result = min(result, depth)
                            break
                    else :
                        return
                elif rdx == bdx and (dir == 0 or dir == 2):
                    y, x = bdy,bdx
                    for i in range(abs(rdy-bdy)):
                        y, x = y + dy[dir] , x + dx[dir]
                        if board[y][x] == '#':
                            result = min(result, depth)
                            break
                    else :
                        return
                else :
                    result = min(result, depth)
                    return
            elif board[bdy][bdx] == 'O':
                return

            if rdy == rty and rdx == rtx and bdy == bty and bdx == btx:
                break

            #동시에 움직이는 것을 swap으로 하면 꼬인다!!
            board[rdy][rdx] = 'R'
            board[bdy][bdx] = 'B'

            if (rdy != rty or rdx != rtx) and board[rty][rtx] == 'R' :
                board[rty][rtx] = '.'
            if (bdy != bty or bdx != btx) and board[bty][btx] == 'B':
                board[bty][btx] = '.'

            rty, rtx = rdy, rdx
            bty, btx = bdy, bdx

        for i in range(4):
            #다음 칸이 현재 칸과 같다면 스킵
            if cutEdge(i, rty, rtx, bty, btx, board):
                continue
            DFS(depth + 1, i, rty, rtx, bty, btx, copy.deepcopy(board))

import copy
for i in range(4):
    DFS(1, i, R_index[0], R_index[1], B_index[0], B_index[1], copy.deepcopy(board_tmp))

if result == 100 :
    print(-1)
else :
    print(result)