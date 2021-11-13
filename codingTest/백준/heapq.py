
class Heap:
    arr = [-1]
    def __init__(self):
        self.arr = [-1]

    def push(self, num):
        self.arr.append(num)
        index = len(self.arr) - 1
        while index >= 1 and self.arr[index] < self.arr[index//2]:
            self.arr[index], self.arr[index//2] = self.arr[index//2], self.arr[index]
            index //= 2

    def pop(self):
        if len(self.arr) > 1:
            item = self.arr[1]
            if len(self.arr) > 1:
                temp = self.arr.pop()
            index, size = 1, len(self.arr)
            target = 2
            while target < size:
                if target + 1 < size and self.arr[target] > self.arr[target+1]:
                    target += 1
                if temp < self.arr[target] : break
                self.arr[index] = self.arr[target]
                index = target
                target *= 2
            self.arr[index] = temp
            return item
        else:
            return -1

heap = Heap()
for i in range(9, 0, -1):
    heap.push(i)

for i in range(8):
    print(heap.pop(), heap.arr)

