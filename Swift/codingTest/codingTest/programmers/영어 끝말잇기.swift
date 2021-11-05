import Foundation

func solution(_ n:Int, _ words:[String]) -> [Int] {
    
    var hist_dict = [String:Bool](), turn = 0
    
    for i in 0..<words.count{
        if i % n == 0{ turn += 1 }
        
        if i > 0, words[i-1].last != words[i].first{
            return [i%n+1, turn]
        }
        
        if hist_dict[words[i]] == nil{
            hist_dict[words[i]] = true
        }else{
            return [i%n+1, turn]
        }
    }
    return [0,0]
}

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
