
arr = [1,7,16,6,4,2,5,8]

def merge(l, r):
    result = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    result += l[i:]
    result += r[j:]
    return result

def merge_sort(arr, size):
    if size == 1 :
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    l_arr = merge_sort(left, len(left))
    r_arr = merge_sort(right, len(right))
    return merge(l_arr, r_arr)

print(merge_sort(arr, len(arr)))