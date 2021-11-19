
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            tmp = self.head
            while tmp.next != None:
                tmp = tmp.next
            tmp.next = node

    def printAl(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end=" ")
            tmp = tmp.next
        print()

    def delete(self, data):

        if self.head.data == data:
            self.head = self.head.next
        else:
            p = self.head
            q = self.head
            while p :
                if p.data == data:
                    q.next = p.next
                    break
                q = p
                p = p.next
            else:
                q.next = None

linkedList = LinkedList()
for i in [1,2,3,4,5,6,7,8,9]:
    linkedList.add(i)
linkedList.printAl()
linkedList.delete(5)
linkedList.printAl()
