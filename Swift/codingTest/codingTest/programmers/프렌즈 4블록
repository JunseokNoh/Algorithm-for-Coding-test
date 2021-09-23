import Foundation

func init_array(_ boards:[[String]], _ row:Int, _ col:Int)->[[Int]]{
    var life = [[Int]](repeating: [Int](repeating: 0, count: col), count: row)
    let U = (-1,0), R = (0,1), D = (1,0), L = (0,-1), UR = (-1,1), DR = (1,1), DL = (1,-1), UL = (-1,-1), C = (0,0)
    let dirs = [[L, UL, U, C], [U, UR, R, C], [C, R, D, DR], [C, L, DL, D]]
    
    for i in 0..<row{
        for j in 0..<col{
            let target = boards[i][j]
            if target == "."{
                life[i][j] = 0
            }else{
                for dir in dirs{
                    var flag = true
                    for d in dir{
                        let dy = i + d.0, dx = j + d.1
                        if 0 <= dy, dy < row, 0 <= dx, dx < col{
                            if target != boards[dy][dx]{
                                flag = false
                                break
                            }
                        }else{
                            flag = false
                            break
                        }
                    }
                    if flag{
                        life[i][j] += 1
                    }
                }
            }
        }
    }
    return life
}

func solution(_ m:Int, _ n:Int, _ board:[String]) -> Int {
    var boards = [[String]](), result = 0
    board.forEach{ b in
        boards.append(b.map{ return String($0) })
    }
    
    while true{
        //step1 겹치는거 다 찾기
        var life = init_array(boards, m, n)
        
        //step2 다 지우기
        var flag = true
        for i in 0..<m-1{
            for j in 0..<n-1{
                if life[i][j] > 0{
                    for item in [(0,0),(0,1), (1,0), (1,1)]{
                        let dy = i+item.0, dx = j+item.1
                        life[dy][dx] -= 1
                        flag = false
                        if life[i+item.0][j+item.1] == 0 {
                            result += 1
                            boards[dy][dx] = "."
                        }
                    }
                }
            }
        }
        
        if flag { break }
        
        //step3 내리기
        for j in 0..<n{
            var dot_cnt = 0, temp = [String](), row = 0
            for i in 0..<m{
                if boards[i][j] != "."{
                    temp.append(boards[i][j])
                }else{
                    dot_cnt += 1
                }
            }
        
            for _ in 0..<dot_cnt{
                boards[row][j] = "."
                row += 1
            }
            
            if dot_cnt > 0{
                for t in temp{
                    boards[row][j] = t
                    row += 1
                }
            }
        }
    }
    return result
}

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
