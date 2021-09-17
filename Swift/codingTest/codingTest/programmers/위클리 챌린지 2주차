
import Foundation

func solution(_ scores:[[Int]]) -> String {
    let size = scores.count
    var result = [String]()
    // i는 열 j는 행
    for i in 0..<size {
        // 최고점 찾기
        var maxVal = [Int](repeating: 0, count: 2)
        var minVal = [101, 0]
        
        for j in 0..<size{
            if scores[j][i] > maxVal[0]{
                maxVal[0] = scores[j][i]
                maxVal[1] = 1
            }else if scores[j][i] == maxVal[0]{
                maxVal[1] += 1
            }
            
            if scores[j][i] < minVal[0]{
                minVal[0] = scores[j][i]
                minVal[1] = 1
            }else if scores[j][i] == minVal[1]{
                minVal[1] += 1
            }
        }
        
        var sum = 0
        var count = 0
        for j in 0..<size{
            if i == j, maxVal[0] == scores[j][i], maxVal[1] == 1{
                    
            }else if i == j,minVal[0] == scores[j][i], minVal[1] == 1{
                
            }else{
                sum += scores[j][i]
                count += 1
            }
        }
        
        let avg = Double(sum) / Double(count)
        if avg >= 90{
            result.append("A")
        }else if avg >= 80{
            result.append("B")
        }else if avg >= 70{
            result.append("C")
        }else if avg >= 50{
            result.append("D")
        }else{
            result.append("F")
        }
    }
        
    return result.joined()
}


print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
