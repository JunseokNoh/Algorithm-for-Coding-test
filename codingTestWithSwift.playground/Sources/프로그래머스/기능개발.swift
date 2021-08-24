import Foundation

func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
    var result = [Int]()
    
    var time = (0..<progresses.count).reduce(into: [Int](), { target, i in
        var rest = 100 - progresses[i]
        var day = rest / speeds[i]
        if day > 0 && rest % speeds[i] != 0 {
            day += 1
        }
        
        target.append(day)
    })
    
    
    while !time.isEmpty{
        let firstDay = time.removeFirst()
        
        var index = 0
        while index < time.count{
            if firstDay < time[index]{
                break
            }
            index += 1
        }
        
        if index > 0{
            time.removeFirst(index)
            result.append(index+1)
        }else{
            result.append(1)
        }
    }
    
    return result
}
