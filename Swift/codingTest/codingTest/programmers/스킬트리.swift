import Foundation

func solution(_ skill:String, _ skill_trees:[String]) -> Int {
    var result = 0
    for tree in skill_trees{
        var skill = skill.map({String($0)}), tree_list = tree.map({String($0)})
        for item in tree_list{
            if skill.contains(item), skill.first! == item{
                skill.removeFirst()
                if skill.count == 0{
                    result += 1
                    break
                }
            }else if skill.contains(item), skill.first! != item{
                break
            }
            
            if tree_list.last! == item{
                result += 1
            }
        }
    }
    return result
}

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))
