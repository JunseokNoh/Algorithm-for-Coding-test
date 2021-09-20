import Foundation

func transfomrm(_ str: String)->[String]{
    var head = "", number = "", tail = ""
    
    var n1 = 0, n2 = 0
    for i in 0..<str.count{
        if str[str.index(str.startIndex, offsetBy: i)].isNumber {
            if n1 == 0 {
                n1 = i
            }
        }else if !str[str.index(str.startIndex, offsetBy: i)].isNumber, n1 != 0{
            if n2 == 0{
               n2 = i-1
               break
           }
        }else if str[str.index(str.startIndex, offsetBy: i)].isNumber, n1 != 0, i == str.count-1{
            n2 = i
        }
    }
    
    head = String(str[str.index(str.startIndex, offsetBy: 0)..<str.index(str.startIndex, offsetBy: n1)])
    if n2 != 0{
        number = String(str[str.index(str.startIndex, offsetBy: n1)...str.index(str.startIndex, offsetBy: n2)])
        tail = String(str[str.index(str.startIndex, offsetBy: n2+1)..<str.endIndex])
    }else{
        number = String(str[str.index(str.startIndex, offsetBy: n1)..<str.endIndex])
        tail = ""
    }
    
    return [head,number,tail]
}

func solution(_ files:[String]) -> [String] {
    var transformed = [[String]]()
    
    for file in files{
        transformed.append(transfomrm(file))
    }
    
    transformed = transformed.sorted(by: { a,b in
        if a[0].uppercased() == b[0].uppercased(){
            if Int(a[1])! < Int(b[1])!{
                return true
            }else{
                return false
            }
        }else if a[0].uppercased() < b[0].uppercased(){
            return true
        }else{
            return false
        }
    })
    
    return transformed.reduce(into: []){ result, i in
        result.append(i[0]+i[1]+i[2])
    }
}

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
print(solution(["a2", "muzi1.png", "MUZI02.zip", "muzi2.png", "a0001"]))
