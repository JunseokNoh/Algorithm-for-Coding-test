//
//  위클리 챌린지 5주차.swift
//  codingTest
//
//  Created by junseok on 2021/08/31.
//

import Foundation

func DFS(_ depth: Int, _ str: String, _ targets:[String], _ result : inout[String]){
    
    if depth > 4 {
        return
    }
    
    for target in targets{
        result.append(str+target)
        DFS(depth+1,str+target, targets, &result)
    }
}
func solution(_ word:String) -> Int {
    var result = [String]()
    let targets: [String] = ["A", "E", "I", "O", "U"]
    
    DFS(0, "", targets, &result)
    
    return result.firstIndex(of: word)! + 1
}
