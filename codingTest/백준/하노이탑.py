

a = [1,2,3]
b = []
c = []

def move(a,b,n):
    b.append(a.pop())

def hanoi(n,a,b,c):
    if n == 1:
        move(a,c,n)
    else:
        hanoi(n-1,a,c,b)
        move(a,c,n)
        hanoi(n-1,b,a,c)

hanoi(3,a,b,c)
print(a,b,c)


