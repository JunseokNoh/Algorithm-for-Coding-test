import Foundation

class Node{
    var number:Int
    var x:Int
    var y:Int
    var left:Node!
    var right:Node!
    
    init(number:Int!, x:Int!, y:Int!, left:Node!, right:Node!) {
        self.number = number
        self.x = x
        self.y = y
        self.left = left
        self.right = right
    }
}

func makeTree(_ parent:Node, _ child:Node){
    if parent.x > child.x {
        if parent.left == nil{
            parent.left = child
        }else{
            makeTree(parent.left, child)
        }
    }else{
        if parent.right == nil{
            parent.right = child
        }else{
            makeTree(parent.right, child)
        }
    }
}

func preorderTraversal(_ node:Node!, _ result:inout [Int]){
    if node == nil { return }
    result.append(node.number)
    preorderTraversal(node.left, &result)
    preorderTraversal(node.right, &result)
}

func postorderTraversal(_ node:Node!, _ result:inout [Int]){
    if node == nil { return }
    postorderTraversal(node.left, &result)
    postorderTraversal(node.right, &result)
    result.append(node.number)
}

func solution(_ nodeinfo:[[Int]]) -> [[Int]] {
    var nodes = [Node](), preorder = [Int](), postorder = [Int]()
    
    for (index, info) in nodeinfo.enumerated(){
        nodes.append(Node(number: index+1, x:info[0], y:info[1], left: nil, right: nil))
    }
    
    nodes.sort(by: { a, b in
        if a.y > b.y{
            return true
        }else if a.y == b.y{
            if a.x < b.x{
                return true
            }else{
                return false
            }
        }else{
            return false
        }
    })
    
    let root = nodes[0]
    for i in 1..<nodes.count{
        makeTree(root, nodes[i])
    }
    
    preorderTraversal(root, &preorder)
    postorderTraversal(root, &postorder)
    
    return [preorder, postorder]
}

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))

