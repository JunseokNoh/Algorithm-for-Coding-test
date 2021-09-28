import Foundation

var boards = [[Int]]()
var hist = [[[[Bool]]]]()
var size = 0

func solution(_ board:[[Int]]) -> Int {
    size = board.count
    boards = board
    hist = [[[[Bool]]]](repeating: [[[Bool]]](repeating: [[Bool]](repeating: [Bool](repeating: true, count: size), count: size), count: size), count: size)
   
    var que = [[0,0,0,1,0]]
    
    hist[0][0][0][1] = false
    hist[0][1][0][0] = false
    
    while que.count > 0{
        let head = que.removeFirst()
        let dy = head[0], dx = head[1], cy = head[2], cx = head[3], depth = head[4]
        if (dy == size - 1 && dx == size - 1) || (cy == size - 1 && cx == size - 1){
            return depth
        }
        
        let dirs = rotate(dy, dx, cy, cx)
        
        for dir in dirs {
            if hist[dir[0]][dir[1]][dir[2]][dir[3]], hist[dir[2]][dir[3]][dir[0]][dir[1]]{
                hist[dir[0]][dir[1]][dir[2]][dir[3]] = false
                hist[dir[2]][dir[3]][dir[0]][dir[1]] = false
                que.append([dir[0], dir[1], dir[2] ,dir[3], depth + 1])
            }
        }
    }
    
    return 0
}

func rotate(_ ly:Int, _ lx:Int, _ ry:Int, _ rx:Int) -> [[Int]]{
    let U = [-1,0], R = [0,1], D = [1,0], L = [0,-1]
    var result = [[Int]]()
    
    if ly - ry == 0{ //가로로 있을 때
        for dir in [U, D]{
            if check(ly + dir[0], lx + dir[1]), boards[ly + dir[0]][lx + dir[1]] == 0, boards[ry + dir[0]][rx + dir[1]] == 0{
                result.append([ry + dir[0], rx + dir[1], ry, rx])
            }
            
            if check(ry + dir[0], rx + dir[1]), boards[ry + dir[0]][rx + dir[1]] == 0, boards[ly + dir[0]][lx + dir[1]] == 0{
                result.append([ly + dir[0], lx + dir[1], ly, lx])
            }
        }
    }else{
        for dir in [R, L]{
            if check(ly + dir[0], lx + dir[1]), boards[ly + dir[0]][lx + dir[1]] == 0, boards[ry + dir[0]][rx + dir[1]] == 0{
                result.append([ry + dir[0], rx + dir[1], ry, rx])
            }
            
            if check(ry + dir[0], rx + dir[1]), boards[ry + dir[0]][rx + dir[1]] == 0, boards[ly + dir[0]][lx + dir[1]] == 0{
                result.append([ly + dir[0], lx + dir[1], ly, lx])
            }
        }
    }
    
    for dir in [U,D,L,R]{
        if check(ly + dir[0], lx + dir[1]), check(ry + dir[0], rx + dir[1]), boards[ry + dir[0]][rx + dir[1]] == 0, boards[ly + dir[0]][lx + dir[1]] == 0{
            result.append([ly+dir[0], lx+dir[1], ry+dir[0], rx+dir[1]])
        }
    }
    
    return result
}

func check(_ y:Int, _ x:Int)->Bool{
    if 0 <= y, y < size, 0 <= x, x < size{
        return true
    }else{
        return false
    }
}

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))

print(solution([[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
