
n = 10

arr = [0 for _ in range(n+1)]
arr[0] = 1

steps = [1,2,3]
for j in range(1,n+1):
    for i in steps:
        if i <= j:
            arr[j] += arr[j-i]

print(arr[1:])