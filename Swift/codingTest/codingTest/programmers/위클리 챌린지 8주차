import Foundation

func solution(_ sizes:[[Int]]) -> Int {
    var newSize = [[Int]]()
    
    for size in sizes{
        if size[0] > size[1]{
            newSize.append(size)
        }else{
            newSize.append([size[1], size[0]])
        }
    }
    var maxWidth = newSize[0][0], maxHeight = newSize[0][1]
    
    for size in newSize{
        maxWidth = max(maxWidth, size[0])
        maxHeight = max(maxHeight, size[1])
    }
    
    return maxHeight * maxWidth
}

func max(_ a:Int, _ b:Int)->Int{
    if a > b {
        return a
    }else{
        return b
    }
}

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
