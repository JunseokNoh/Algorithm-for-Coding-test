import Foundation

func solution(_ n:Int) -> [Int] {
    var arr = [[Int]]()
    var n = n
    
    for i in 0..<n{
        arr.append([Int](repeating: 0, count: i+1))
    }
    
    var num = 0, row = -1, col = 0
    
    while n > 0 {
        for _ in 0..<n{
            num += 1
            row += 1
            arr[row][col] = num
        }
        
        for _ in 0..<n-1{
            num += 1
            col += 1
            arr[row][col] = num
        }
        
        if n - 2 < 0 { break }
        for _ in 0..<n-2{
            num += 1
            row -= 1
            col -= 1
            arr[row][col] = num
        }
        
        n -= 3
    }
    
    return arr.reduce(into: [Int]()){ result, values in
        for val in values{
            result.append(val)
        }
    }
}

func printAll(_ arr:[[Int]]){
    for tmp in arr{
        print(tmp)
    }
}

print(solution(1))
print(solution(6))

