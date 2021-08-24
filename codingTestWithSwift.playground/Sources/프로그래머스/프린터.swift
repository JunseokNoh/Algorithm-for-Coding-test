
import Foundation

func solution(_ priorities:[Int], _ location:Int) -> Int {
    var priorities = priorities
    var priority = priorities.sorted(by: {$0 > $1})
    var location = location
    var result = 0
    
    while true{
        
        if priorities[0] == priority[0]{
            priorities.removeFirst()
            priority.removeFirst()
            result += 1
            
            if location == 0{
                break
            }else{
                location -= 1
            }
        }else{
            priorities.append(priorities.removeFirst())
            
            if location == 0 {
                location = priorities.count - 1
            }else{
                location -= 1
            }
        }
    }
    return result
}
