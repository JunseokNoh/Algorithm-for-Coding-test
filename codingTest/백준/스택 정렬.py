stack = []
buffer = []

for i in [3,4,6,8]:
    stack.append(i)

def stack_sort():
    while stack:
        temp = stack.pop()
        cnt = 0
        while buffer and buffer[-1] > temp:
            stack.append(buffer.pop())
            cnt += 1
        buffer.append(temp)
        for _ in range(cnt):
            buffer.append(stack.pop())

    while buffer:
        stack.append(buffer.pop())

stack_sort()
print(stack, buffer)