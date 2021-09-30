import Foundation

func solution(_ lands:[[Int]]) -> Int{
    var size = lands.count, lands = lands
    for i in 1..<size{
        lands[i][0] += max(lands[i-1][1],lands[i-1][2],lands[i-1][3])
        lands[i][1] += max(lands[i-1][0],lands[i-1][2],lands[i-1][3])
        lands[i][2] += max(lands[i-1][0],lands[i-1][1],lands[i-1][3])
        lands[i][3] += max(lands[i-1][0],lands[i-1][1],lands[i-1][2])
    }
    
    return lands[size-1].max()!
}

func max(_ a:Int, _ b:Int, _ c:Int)->Int{
    return a > b ? (a > c ? a : c) : (b > c ? b : c)
}

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))

// dp


// 1 2 3 4
// 1 1 1 1000
// 2 2 2 100
