import Foundation

func trsnsform(_ result: inout [String], _ n: Int, _ num: Int){
    String(num,radix: n).forEach{ i in
        result.append(String(i).uppercased())
    }
}

func solution(_ n:Int, _ t:Int, _ m:Int, _ p:Int) -> String {
    var val = "", num = 0, result = [String]()
    
    while true{
        trsnsform(&result, n, num)
        if result.count >= t * m {
            break
        }
        num += 1
    }
    
    for i in 0..<result.count{
        if i % m + 1 == p{
            val += result[i]
        }
        if val.count == t {
            break
        }
    }
    return val
}

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))

