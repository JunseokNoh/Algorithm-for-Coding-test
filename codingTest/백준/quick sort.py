
def change(left, right, arr):
    pivot = arr[left]
    i, j = left+1, right
    while i < j:
        while i <= right and arr[i] < pivot:
            i += 1
        while j >= left and arr[j] > pivot:
            j -= 1
        if i < j :
            arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left]
    
def quick_sort(left, right, arr):
    if left < right :
        change(left,right,arr)

        mid = (left+right) // 2
        quick_sort(left,mid-1,arr)
        quick_sort(mid+1,right,arr)

arr = [9,2,3,1,4,6,7,2]
quick_sort(0, len(arr)-1, arr)
print(arr)
