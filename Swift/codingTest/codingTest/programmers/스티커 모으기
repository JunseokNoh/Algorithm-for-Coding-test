import Foundation

var linked_list = [[Int]]()
func solution(_ sticker:[Int]) -> Int{
    let size = sticker.count
    
    if size == 1{
        return sticker[0]
    }
    
    var dp1 = [Int](repeating: 0, count: size)
    var dp2 = [Int](repeating: 0, count: size)
    dp1[0] = sticker[0]; dp1[1] = sticker[0]
    dp2[0] = 0; dp2[1] = sticker[1]
    
    for i in 2..<size{
        if i != size - 1{
            dp1[i] = max(dp1[i-1], dp1[i-2]+sticker[i])
        }
        dp2[i] = max(dp2[i-1], dp2[i-2]+sticker[i])
    }
    return dp1[size-2] > dp2[size-1] ? dp1[size-2] : dp2[size-1]
}

func max(_ a:Int, _ b:Int)->Int{
    return a > b ? a : b
}

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1]))

