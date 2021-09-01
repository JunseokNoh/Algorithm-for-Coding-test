
import Foundation

func check(_ id: String, _ banid: String)->Bool{
    if id.count != banid.count{
        return false
    }
    let size = id.count
    for i in 0..<size{
        let index = banid.index(banid.startIndex, offsetBy: i)
        if banid[index] == "*"{
            continue
        }else if id[index] != banid[index]{
            return false
        }
    }
    return true
}

func DFS(_ depth:Int, _ user_id:[String], _ banned_id:[String], _ answer: inout Int, _ visited_userid:[Bool], _ result : inout Set<[String]>){
    if depth == banned_id.count{
        var temp = [String]()
        for i in 0..<visited_userid.count{
            if !visited_userid[i]{
                temp.append(user_id[i])
            }
        }
        result.insert(temp)
        return
    }
    var visited_userid = visited_userid
    for i in 0..<user_id.count{
        if check(user_id[i], banned_id[depth]) && visited_userid[i]{
            visited_userid[i] = false
            DFS(depth+1, user_id, banned_id, &answer, visited_userid, &result)
            visited_userid[i] = true
        }
    }
}

func solution(_ user_id:[String], _ banned_id:[String]) -> Int {
    var answer = 0
    var result : Set<[String]> = Set([])
    let visited_userid = [Bool](repeating: true, count: user_id.count)
    
    DFS(0, user_id, banned_id, &answer, visited_userid, &result)
    
    return result.count
}

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))

