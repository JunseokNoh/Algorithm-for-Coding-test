
import Foundation

class TrieNode{
    var key:String!
    var parent:TrieNode!
    var children: [String:TrieNode] = [:]
    var isLeaf: Bool{
        return children.isEmpty
    }
    
    init(key: String!, parent: TrieNode! = nil) {
        self.key = key
        self.parent = parent
    }
}

class Trie{
    var root:TrieNode = TrieNode(key: nil, parent: nil)
    
    init(){
        
    }
    
    func insert(_ words: [String]){
        var currentNode = root
        let n = Int(words[0])!
        
        for word in words[1...n]{
            if let childNode = currentNode.children[word] {
                currentNode = childNode
            }else{
                let newNode = TrieNode(key: word, parent: currentNode)
                currentNode.children[word] = newNode
                currentNode = newNode
            }
        }
    }
    
    func printAll(_ node: TrieNode, _ depth:Int){
        for child in node.children.keys.sorted(){
            var printVal = ""
            for _ in 0..<depth{
                printVal += "--"
            }
            printVal += child
            print(printVal)
            printAll(node.children[child]!, depth+1)
        }
        
    }
}

let n = Int(readLine()!)!
let trie = Trie()
(1...n).forEach{ _ in
    let words = (readLine()!).split(separator: " ").map{String($0)}
    trie.insert(words)
}
trie.printAll(trie.root, 0)


