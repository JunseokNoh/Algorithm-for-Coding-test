import Foundation

func solution(_ s:String) -> [Int] {
    var zero_cnt = 0, turn_cnt = 0
    var str = s.map{
        String($0)
    }
    
    while true{
        if str.count == 1, str[0] == "1"{ break }
        turn_cnt += 1
        str = str.filter{ item -> Bool in
            if item != "0"{
                return true
            }else{
                zero_cnt += 1
                return false
            }
        }
        str = String(str.count, radix: 2).map{
            return String($0)
        }
    }
    return [turn_cnt, zero_cnt]
}

print(solution("01110"))
