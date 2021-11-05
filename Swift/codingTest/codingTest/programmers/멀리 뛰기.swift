import Foundation

func solution(_ n:Int) -> Int {
    var arr = [Int](repeating: 0, count: n+1)
    arr[1] = 1
    
    if n > 1{
        arr[2] = 1
    }
    
    for i in 1...n{
        if i - 1 >= 0 {
            arr[i] += arr[i-1]
        }
        
        if i - 2 >= 0{
            arr[i] += arr[i-2]
        }
        arr[i] = arr[i] % 1234567
    }
    
    return arr[n] % 1234567
}


//print(solution(4))
print(solution(2000))
print(solution(1))
print(solution(1997))
