import Foundation

func min(_ a:Int, _ b:Int)->Int{
    return a > b ? b : a
}

func max(_ a:Int, _ b:Int)->Int{
    return a > b ? a : b
}

func solution(_ line:[[Int]]) -> [String] {
    let size = line.count
    var arr = [[Int]]()
    var maxx = -Int.max/2, maxy = -Int.max/2, minx = Int.max/2, miny = Int.max/2
    
    for i in 0..<size-1{
        let a = line[i][0], b = line[i][1], e = line[i][2]
        for j in i+1..<size{
            if i == j {continue}
            let c = line[j][0], d = line[j][1], f = line[j][2]
            if a*d - b*c == 0 {continue}
            let x = (Double(b*f-e*d) / Double(a*d-b*c))
            let y = (Double(e*c-a*f) / Double(a*d-b*c))
            
            if Double(Int(x)) == x, Double(Int(y)) == y{
                maxx = max(maxx,Int(x)); minx = min(minx,Int(x))
                maxy = max(maxy,Int(y)); miny = min(miny,Int(y))
                arr.append([Int(x),Int(y)])
            }
        }
    }
    
    let col = maxx-minx+1, row = maxy-miny+1

    var result = [[String]](repeating: [String](repeating: ".", count: col), count: row)
    for t in arr{
        let x = t[0]-minx, y = maxy - t[1]
        result[y][x] = "*"
    }

    return result.reduce(into: []){ t, i in
        t.append(i.joined())
    }
}


//print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
//print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
