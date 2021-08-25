import Foundation

func DFS(_ n:Int, _ parent:Int, _ node:Int, _ roots: inout [Int], _ computers:[[Int]]){
    
    for i in 0..<n{
        if  i != node && computers[node][i] == 1 && roots[i] == -1{
            roots[i] = parent
            //print(parent, node, i, roots)
            DFS(n, parent, i, &roots, computers)
        }
    }
}

func solution(_ n:Int, _ computers:[[Int]]) -> Int {
    var roots = [Int](repeating: -1, count:n)

    var result = 0
    
    for i in 0..<n{
        if roots[i] == -1{
            result += 1
            //roots[i] = i
            DFS(n, i, i, &roots, computers)
        }
    }
    //print()
    

    return result
}


print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

print(solution(3,[[1, 0, 0], [0, 1, 0], [0, 0, 1]]))