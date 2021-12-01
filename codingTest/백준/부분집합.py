
arr = [1,2,3]
result = []

import copy
def find(a, depth, size):
    if depth == size:
        return

    for i in range(depth, size):
        a.append(arr[i])
        result.append(copy.deepcopy(a))
        find(a,i+1,size)
        a.pop()

find([], 0, len(arr))
print(result)