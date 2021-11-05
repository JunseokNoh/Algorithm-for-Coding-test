
def quick_sort(left, right, arr):
    if left < right:
        pivot = arr[left]
        i, j = left+1, right
        while i <= j:
            while i <= right and pivot >= arr[i]:
                i += 1
            while j >= left+1 and pivot <= arr[j]:
                j -= 1
            if i <= j :
                arr[i], arr[j] = arr[j], arr[i]
            else:
                arr[left], arr[j] = arr[j], arr[left]

        quick_sort(left, j-1, arr)
        quick_sort(j+1, right, arr)

arr = [4, 8, 9, 3, 2, 1, 5, 6]

quick_sort(0, len(arr)-1, arr)
print(arr)