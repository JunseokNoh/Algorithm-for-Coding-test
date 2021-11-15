
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,data):
        if self.head == None:
            self.head = linkedListNode(data)
        else:
            tmp = self.head
            while True:
                if tmp.next == None:
                    tmp.next = linkedListNode(data)
                    break
                tmp = tmp.next

class linkedListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:

    def __init__(self):
        self.root = None
        self.linkedlist = []

    def add(self,data):
        node = Node(data)
        if self.root == None:
            self.root = node
        else:
            temp = self.root
            while True:
                if temp.data > node.data:
                    if temp.left == None:
                        temp.left = node
                        break
                    else:
                        temp = temp.left
                else:
                    if temp.right == None:
                        temp.right = node
                        break
                    else:
                        temp = temp.right

    def traversal(self, depth, node):
        if node:
            if len(self.linkedlist) < depth+1:
                self.linkedlist.append(LinkedList())
            self.linkedlist[depth].add(node.data)

            self.traversal(depth+1,node.left)
            self.traversal(depth+1,node.right)

    def getHeight(self, node):
        if node == None : return -1
        return max(self.getHeight(node.left), self.getHeight(node.right)) + 1

tree = Tree()
for i in [5,4,2,1,7,9,6]:
    tree.add(i)

tree.traversal(0, tree.root)

for i in tree.linkedlist:
    temp = i.head
    while temp:
        print(temp.data, end = " ")
        temp = temp.next
    print()

print(tree.getHeight(tree.root))
