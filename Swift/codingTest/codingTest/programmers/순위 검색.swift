
import Foundation

func getKeys(_ depth: Int, _ key:String, _ key_list: [String], _ keys:inout [String]){
    if depth == 4 {
        keys.append(key)
        return
    }
    getKeys(depth+1, key+key_list[depth], key_list, &keys)
    getKeys(depth+1, key+"-", key_list, &keys)
}

func solution(_ info:[String], _ query:[String]) -> [Int] {
    var info_dict = [String:[Int]](), result = [Int]()
    
    for i in info{
        let temp = i.split(separator: " ")
        let key_list = temp[0...3].reduce(into: []){ target, i in
            target.append(String(i))
        }
        let value = Int(temp[4])!
        var keys = [String]()
        
        getKeys(0, "", key_list, &keys)
        print(keys)
        for key in keys {
            if info_dict[key] == nil{
                info_dict[key] = [value]
            }else{
                info_dict[key]?.append(value)
            }
        }
    }
    
    for key in info_dict.keys{
        info_dict[key]?.sort()
    }
    
    _ = info_dict.sorted(by: {
        $0.key > $1.key
    })
    
    for q in query{
        var find_key = ""
        let temp = q.split(separator: " ")
        let score = Int(temp[7])!
        
        for t in temp[0...6]{
            if t != "and"{
                find_key += t
            }
        }
        
        if let values = info_dict[find_key]{
            var start = 0, end = values.count, mid = 0
            while start <= end{
                mid = (start + end) / 2
                
                if mid == values.count{ break }
                
                if values[mid] >= score{
                    end = mid - 1
                }else{
                    start = mid + 1
                }
            }
            result.append(values.count - start)
        }else{
            result.append(0)
        }
    }
    return result
}

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150","- and - and - and - 0"]))
,11
