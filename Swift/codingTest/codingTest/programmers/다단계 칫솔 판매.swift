import Foundation

var parents = [Int]()
var result = [Int]()

func solution(_ enroll:[String], _ referral:[String], _ seller:[String], _ amount:[Int]) -> [Int] {
    let number = enroll.count
    var index_dict = [String:Int]()
    parents = [Int](repeating: -1, count: number)
    result = [Int](repeating: 0, count: number)
    
    for (i, name) in enroll.enumerated(){
        let parent = referral[i]
        index_dict[name] = i
        if index_dict[parent] != nil{
            parents[i] = index_dict[parent]!
        }
    }
    
    for (person, money) in zip(seller, amount){
        traversal(index_dict[person]!, money * 100)
    }
    
    return result
}

func traversal(_ index:Int, _ money:Int){
    if index == -1 {
        return
    }
    if Double(money) * 0.1 < 1{
        result[index] += money
    }else{
        let remain = Int(Double(money) * 0.1)
        result[index] += money - remain
        traversal(parents[index], remain)
    }
}

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
