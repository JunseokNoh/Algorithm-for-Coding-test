
import Foundation

func solution(_ lines:[String]) -> Int {
    var times = [(Double, Double)]()
    for line in lines{
        let date = line.split(separator: " ").map{
            String($0)
        }
        times.append(cal(date[1], date[2]))
    }
    
    var result = 0
    for i in 0..<times.count {
        //시작점 기준
        let start = times[i].0
        var cnt = 0
        for j in 0..<times.count{
            if i != j, (start <= times[j].0) && (times[j].0 < (start + 1)) || (start <= times[j].1) && (times[j].1 < (start + 1)){
                cnt += 1
            }else if i != j, (times[j].0 < start) && (start + 1) < times[j].1{
                cnt += 1
            }
        }
        
        if result < cnt {
            result = cnt
        }
        
        //끝점 기준
        let end = times[i].1
        cnt = 0
        for j in 0..<times.count{
            if i != j, (end <= times[j].0) && (times[j].0 < (end + 1)) || (end <= times[j].1) && (times[j].1 < (end + 1)){
                cnt += 1
            }else if i != j, (times[j].0 < end) && (end + 1) < times[j].1{
                cnt += 1
            }
        }
        if result < cnt {
            result = cnt
        }
    }
    //print(times)
    return result + 1
}

func cal(_ time:String, _ diff:String)->(Double, Double){
    let time = time.split(separator: ":").map{
        Double($0)!
    }
    let start = (time[0] * 3600) + (time[1] * 60) + time[2] -  Double(diff.replacingOccurrences(of: "s", with: ""))! + 0.001
    let end =  (time[0] * 3600) + (time[1] * 60) + time[2]
    return (start, end)
}
