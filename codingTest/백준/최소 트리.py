
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

a = [1,2,3,4,5,6,7,8,9]
tree = Tree()

def make_Tree(left, right):
    if left <= right:
        mid = (left+right)//2
        node = Node(a[mid])
        node.left = make_Tree(left,mid-1)
        node.right = make_Tree(mid+1, right)
        return node

def traversal(node):
    if node :
        print(node.data)
        traversal(node.left)
        traversal(node.right)

tree.root = make_Tree(0,len(a)-1)
traversal(tree.root)



