import Foundation

var N = Int(readLine()!)!
var arr = [[Int]]()
var result = [Int](repeating: 0, count: 3)

for _ in 0..<N{
    let temp = readLine()!.split(separator: " ").map{
        Int(String($0))!
    }
    arr.append(temp)
}

func divide(_ row:Int, _ col:Int, _ arr: [[Int]], _ size : Int){
    if check(row, col, arr, size){
       return
    }else{
        let newSize = size / 3
        for i in 0..<3{
            for j in 0..<3{
                divide(row + (newSize * i), col + (newSize * j), arr, newSize)
            }
        }
    }
}

func check(_ row: Int, _ col:Int, _ arr: [[Int]], _ size : Int) -> Bool{
    let val = arr[row][col]
    for i in row..<row+size{
        for j in col..<col+size{
            if arr[i][j] != val{
                return false
            }
        }
    }
    result[val+1] += 1
    return true
}

divide(0, 0, arr, N)

result.forEach{
    print($0)
}
