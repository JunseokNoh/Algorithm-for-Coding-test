
def factorial(n):
    if n == 1 :
        return 1
    return n * factorial(n-1)

def bubble_sorting(arr):
    size = len(arr)
    for i in range(size-1,0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sorting(arr):
    size = len(arr)
    for i in range(0,size-1):
        target = i
        for j in range(i, size):
            if arr[target] > arr[j]:
                target = j
        arr[i], arr[target] = arr[target], arr[i]

def fibo_memoization(n, fibo):
    if n == 1 or n == 0:
        fibo[n] = 1
        return fibo[n]

    if fibo[n] != -1:
        return fibo[n]
    else:
        fibo[n] = fibo_memoization(n-1, fibo) + fibo_memoization(n-2, fibo)

    return fibo[n]

def fibo_recursive(n):
    if n == 1 or n == 0:
        return 1
    return fibo_recursive(n-1) + fibo_recursive(n-2)

import random
def find_already_num():
    arr = [False for _ in range(11)]
    for _ in range(10):
        num = random.randint(1,10)
        print(num)
        if not arr[num]:
            print("True")
            arr[num] = True
        else:
            print("False")

def binary_search_recursive(start,end,target,primes):
    mid = (start+end)//2
    if start > end:
        return -1

    if primes[mid] < target :
        return binary_search_recursive(mid+1, end, target,primes)
    elif primes[mid] > target:
        return binary_search_recursive(start, mid-1, target, primes)
    else:
        return mid

def binary_search_iteration(start, end, target, primes):
    while start <= end:
        mid = (start + end) // 2
        if primes[mid] < target:
            start = mid + 1
        elif primes[mid] > target:
            end = mid + 1
        else :
            print(mid, primes[mid])
            break

print(factorial(3))
arr = [4,3,7,8,1,2,3,4,63,8,9,322,11]
#bubble_sorting(arr)
insertion_sorting(arr)
print(arr)

fibo = [-1 for _ in range(11)]
fibo_memoization(10, fibo)
print(fibo)
print(fibo_recursive(10))
find_already_num()
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(binary_search_recursive(0, len(primes)-1, 67, primes))
binary_search_iteration(0, len(primes)-1, 67, primes)

