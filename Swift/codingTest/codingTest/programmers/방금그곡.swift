import Foundation

func solution(_ m:String, _ musicinfos:[String]) -> String {
    let m = m.split()
    var answer:(Int, String)!
    
    for musicinfo in musicinfos{
        let list = musicinfo.split(separator: ",").map({return String($0)})
        let startTime = list[0].split(separator: ":").map({return Int($0)!})
        let endTime = list[1].split(separator: ":").map({return Int($0)!})
        let title = list[2], melody = list[3].split()
        let duration = getDuration(startTime, endTime), runningTime = melody.count
        
        if m.count > duration {continue}
        //duration보다 runningTime가 클 경우 -> 반복 재생
        var temp = [String]()
        for i in 0..<duration{
            temp.append(melody[i%runningTime])
        }
        for i in 0...temp.count-m.count{
            var flag = true
            for j in 0..<m.count{
                if temp[i+j] != m[j]{
                    flag = false
                    break
                }
            }
            if flag{
                if answer == nil{
                    answer = (duration, title)
                }else if answer != nil, answer.0 < duration{
                    answer = (duration, title)
                }
                break
            }
        }
    }

    return answer != nil ? answer.1 : "(None)"
}

extension String{
    func split()->[String]{
        let str = self.map({return String($0)})
        var result = [String]()
        for (index, s) in str.enumerated(){
            if s == "#"{ continue }
            if index == self.count - 1 {
                result.append(String(s))
            }else{
                if str[index+1] == "#"{
                    result.append("\(str[index])\(str[index+1])")
                }else{
                    result.append(String(s))
                }
            }
        }
        return result
    }
}

func getDuration(_ start:[Int], _ end:[Int])->Int{
    if start[0] == end[0] {
        return end[1] - start[1]
    }else{
        return end[1] + 60 * (end[0] - start[0]) - start[1]
    }
}

//print(solution("ABC#", ["12:50,13:00,HELLO,ABC#AAAA", "13:00,13:05,WORLD,ABCDEF"]))
//print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B", "12:00,12:14,HELLO,CDEFGAB"]))
//print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("ABC", ["13:00,13:05,WORLD1,ABCDEF", "13:00,13:05,WORLD2,ABCDEF", "13:00,13:07,WORLD3,ABCDEF"]))
