
def insertion_sort1(arr):
    size = len(arr)
    for i in range(1, size):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    print(arr)

def insertion_sort2(arr):
    size = len(arr)
    for i in range(1, size):
        j = i
        num = arr[i]
        while j >= 0 and arr[j-1] > num:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = num
    print(arr)

arr = [1,4,6,8,2,9]
insertion_sort1(arr)
arr = [1,4,6,8,2,9]
insertion_sort2(arr)


