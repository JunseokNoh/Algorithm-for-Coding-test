import Foundation

class TrieNode{
    var key:String!
    var parent:TrieNode!
    var children: [String:TrieNode] = [:]
    var childCnt:Int = 0
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
    
    func insert(_ word: String){
        var currentNode = root
        for char in word{
            currentNode.childCnt += 1
            if currentNode.children[String(char)] == nil{
                currentNode.children[String(char)] = TrieNode(key: String(char), parent: currentNode)
            }
            currentNode = currentNode.children[String(char)]!
        }
    }
    
    func search(_ query: String)->Int{
        var currentNode = root
        for char in query{
            if char == "?" { return currentNode.childCnt }
            if currentNode.children[String(char)] == nil{
                return 0
            }
            currentNode = currentNode.children[String(char)]!
        }
        return currentNode.childCnt
    }
}

func reversed(_ str:String)->String{
    return str.reversed().reduce(into: ""){ result,i in
        result += String(i)
    }
}

func solution(_ words:[String], _ queries:[String]) -> [Int] {
    var trieDict: [Int:Trie] = [:]
    var reversedDict: [Int:Trie] = [:]
    var result = [Int]()
    
    for word in words{
        let size = word.count
        if trieDict[size] == nil{
            trieDict[size] = Trie()
            reversedDict[size] = Trie()
        }
        trieDict[size]?.insert(word)
        reversedDict[size]?.insert(reversed(word))
    }
    
    for query in queries{
        let size = query.count
        guard trieDict[size] != nil else{
            result.append(0)
            continue
        }
        
        if query[query.startIndex] != "?"{
            result.append((trieDict[size]?.search(query))!)
        }else{
            result.append((reversedDict[size]?.search(reversed(query)))!)
        }
    }
    return result
}

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
