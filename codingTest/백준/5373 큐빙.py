import sys
import copy

T = int(sys.stdin.readline())
dir_dict = {
    'U' : 0,'D':1,'F':2,'B':3,'L':4,'R':5
}
U,D,F,B,L,R = 0,1,2,3,4,5
temp_CUBE = [[] for _ in range(6)]
result_dict = {
    0:'w',1:'y',2:'r',3:'o',4:'g',5:'b'
}
def return_color(dir):
    return [[result_dict[dir]] * 3 for _ in range(3)]

for i in range(6):
    temp_CUBE[i].extend(return_color(i))

def rotate_v1(side, dir, cnt):
    for _ in range(cnt):
        #바라보고있는 면을 시계방향 or 반시계방향으로 회전
        if dir == '-' :#반시계 방향
            CUBE[side] = list(map(list, zip(*CUBE[side])))
            CUBE[side] = list(reversed(CUBE[side]))
        elif dir == '+':#시계 방향
            CUBE[side] = list(map(list, zip(*CUBE[side])))
            CUBE[side] = [list(reversed(i)) for i in CUBE[side]]

def rotate_v3(rotate_target, col, dir):

    tmp = []
    if dir == '+':#시계방향일때
        for i in rotate_target:
            tmp.append(CUBE[i][col])
        tmp  = [tmp[-1]] + tmp[:-1]
    elif dir == '-':#반시계방

        for i in rotate_target:
            tmp.append(CUBE[i][col])
        tmp = tmp[1:]+[tmp[0]]
    return tmp

def reverser_dir(dir):
    if dir == '-': return '+'
    else: return '-'
def rotate_v2(side, dir):
    target = []
    if side == U :
        col = 0
        #L -> -, R-> + ,F-> X, B->++
        target = [L,F,R,B]
        rotate_v1(L,'-',1);rotate_v1(R,'+',1);rotate_v1(B,'+',2)
        dir = reverser_dir(dir)
    elif side == D :
        col = 2
        #L -> -, R-> + F-> X, B->++
        target = [L, F, R, B]
        rotate_v1(L, '-', 1);rotate_v1(R, '+', 1);rotate_v1(B, '+', 2)
    elif side == L:
        col = 0
        #U,F,D,B -> 모두 +
        rotate_v1(U, '+', 1);rotate_v1(F, '+', 1);rotate_v1(D, '+', 1);rotate_v1(B, '+', 1)
        target = [U,F,D,B]
    elif side == R:
        col = 2
        #U,F,D,B -> +
        target = [U, F, D, B]
        rotate_v1(U, '+', 1);rotate_v1(F, '+', 1);rotate_v1(D, '+', 1);rotate_v1(B, '+', 1)
        dir = reverser_dir(dir)
    elif side == F:
        #D -> ++
        col = 2
        rotate_v1(D,"+",2)
        target =[L,U,R,D]
    elif side == B:
        #D ->++
        col = 0
        rotate_v1(D, "+", 2)
        target = [L, U, R, D]
        dir = reverser_dir(dir)

    tt = rotate_v3(target, col, dir)

    for i in range(4):
        CUBE[target[i]][col] = tt[i]

    if side == U or side == D:
        # L -> -, R-> + F-> X, B->++
        rotate_v1(L, '+', 1);rotate_v1(R, '-', 1);rotate_v1(B, '-', 2)
    elif side == L or side == R:
        # U,F,D,B -> +
        rotate_v1(U, '-', 1);rotate_v1(F, '-', 1);rotate_v1(D, '-', 1);rotate_v1(B, '-', 1)
    elif side == F or side == B:
        # D ->++
        rotate_v1(D, "-", 2)

for _ in range(T):
    N = int(sys.stdin.readline())
    temp = list(map(str, sys.stdin.readline().rstrip("\n")))
    temp = ' '.join(temp).split()
    CUBE = copy.deepcopy(temp_CUBE)
    for i in range(0, len(temp), 2):
        rotate_v1(dir_dict[temp[i]], temp[i + 1],1)
        rotate_v2(dir_dict[temp[i]], temp[i + 1])

    for i in CUBE[U]:
        print(''.join(i))