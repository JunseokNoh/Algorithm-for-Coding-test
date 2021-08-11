import sys

while True:
    try :
        size = int(sys.stdin.readline()) * 10000000
        n = int(sys.stdin.readline())
        lego = [int(sys.stdin.readline()) for _ in range(n)]
        lego.sort()
        i,j = 0, n-1
        while i < j :
            if lego[i] + lego[j] == size :
                print("yes %d %d" %(lego[i],lego[j]))
                break
            elif lego[i] + lego[j] > size :
                j -= 1
            elif lego[i] + lego[j] < size :
                i += 1
        else:
            print("danger")
    except:
        break