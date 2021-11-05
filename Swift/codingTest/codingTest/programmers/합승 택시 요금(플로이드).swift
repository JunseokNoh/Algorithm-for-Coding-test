import Foundation

func min(_ a:Int, _ b:Int)->Int{
    if a > b {
        return b
    }else{
        return a
    }
}

func Floyd(_ n:Int, _ fees:inout [[Int]]){
    for mid in 1...n{
        for to in 1...n{
            for from in 1...n{
                //Max 값이면 해당 간선은 존재하지 않는 것임, to~from 까지는 mid를 거쳤다가 갈 수 도 있으니까 MAx가 될 수 있음
                if fees[to][mid] == Int.max || fees[mid][from] == Int.max{
                    continue
                }
                fees[to][from] = min(fees[to][from], fees[to][mid] + fees[mid][from])
            }
        }
    }
}

func solution(_ n:Int, _ s:Int, _ a:Int, _ b:Int, _ fares:[[Int]]) -> Int {
    var fees = [[Int]](repeating: [Int](repeating: Int.max, count: n+1), count: n+1)
    (1...n).forEach{fees[$0][$0] = 0}
    fares.forEach{
        fees[$0[0]][$0[1]] = $0[2]
        fees[$0[1]][$0[0]] = $0[2]
    }
    
    Floyd(n, &fees)
    
    var result = fees[s][a] + fees[s][b]
    for i in 1...n{
        if s == i || fees[s][i] == Int.max || fees[i][a] == Int.max || fees[i][b] == Int.max{
            continue
        }
        result = min(result, fees[s][i] + fees[i][a] + fees[i][b])
    }
    return result
}
