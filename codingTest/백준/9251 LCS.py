A = input()
B = input()
if len(A) > len(B) :
    A, B = B, A

len_a = len(A) + 1
len_b = len(B) + 1

arr = [[0] * (len_b) for _ in range(len_a)]

for i in range(1,len_a):
    for j in range(1,len_b):
        if A[i-1] == B[j-1]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])

result_len = arr[len_a-1][len_b-1]
print(result_len)
j = len_a - 1
result = []
#ACAYKP -> A, 세로, len_a
#CAPCAK -> B 가로, len_b

if result_len > 0:
    for i in range(len_b-1,1, -1):
        temp_j = j
        while j >= 1 :
            #print(i,j, A[i-1], B[j-1])
            if B[i-1] == A[j-1]:
                result.insert(0, B[i-1])
                break
            j -= 1
        else:
            j = temp_j

    print(''.join(result))