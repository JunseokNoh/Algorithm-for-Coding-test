import Foundation

func solution(_ dirs:String) -> Int {
    let dict = ["L" : (0,-1), "U":(-1,0), "R":(0,1), "D":(1,0)]
    let dirs = dirs.map({return String($0)})
    var cy = 5, cx = 5, totaldist = 0
    var hist = [[[[Bool]]]](repeating: [[[Bool]]](repeating: [[Bool]](repeating: [Bool](repeating: true, count: 11), count: 11), count: 11), count: 11)
    
    for dir in dirs{
        let dy = cy + dict[dir]!.0
        let dx = cx + dict[dir]!.1
        
        if 0 <= dy, dy <= 10, 0 <= dx, dx <= 10{
            if hist[cy][cx][dy][dx]{
                totaldist += 1
                hist[cy][cx][dy][dx] = false
                hist[dy][dx][cy][cx] = false
            }
            cy = dy
            cx = dx
        }else{
            continue
        }
    }
    
    return totaldist
}

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
print(solution("UD"))
