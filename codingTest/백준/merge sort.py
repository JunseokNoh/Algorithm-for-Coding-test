

def merge_sort(result1, result2):
    temp = []
    i, j = 0, 0
    size1, size2 = len(result1), len(result2)

    while i < size1 and j < size2:
        if result1[i] < result2[j]:
            temp.append(result1[i])
            i += 1
        else:
            temp.append(result2[j])
            j += 1

    temp += result1[i:]
    temp += result2[j:]

    return temp

def merge(arr, size):
    if size == 1 :
        return arr

    mid = size//2
    result1 = merge(arr[:mid], len(arr[:mid]))
    result2 = merge(arr[mid:], len(arr[mid:]))

    return merge_sort(result1, result2)


arr = [9,8,6,3,2,1,5,6]

print(merge(arr, len(arr)))

#0,1,2,3,4,5,6,7