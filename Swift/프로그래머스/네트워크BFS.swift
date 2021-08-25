import Foundation


func BFS(_ start:Int, _ n: Int, _ computers:[[Int]], _ visited:inout [Bool]){
    var que:[Int] = [start]
    
    while !que.isEmpty{
        var node = que.removeFirst()
        
        (0..<n).forEach{ i in
            if !visited[i] && node != i && computers[node][i] == 1{
                visited[i] = true
                que.append(i)
            }
        }
    }
}

func solution(_ n:Int, _ computers:[[Int]]) -> Int {
    var result = 0
    var visited = [Bool](repeating:false, count:n)

    (0..<n).forEach{ i in 
        if !visited[i]{
            result += 1

            BFS(i, n, computers, &visited)
        }
    }
    return result
}

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(solution(3,[[1, 0, 0], [0, 1, 0], [0, 0, 1]]))