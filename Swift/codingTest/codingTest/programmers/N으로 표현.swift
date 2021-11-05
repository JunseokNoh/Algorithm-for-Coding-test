//
//  N으로 표현.swift
//  codingTest
//
//  Created by junseok on 2021/09/01.
//

import Foundation

func solution(_ N:Int, _ number:Int) -> Int {
    
    if N == number {
        return 1
    }
    
    var numbers = [Set<Int>](repeating: Set(), count: 9)
    var num = N
    for i in 1..<9{
        numbers[i].insert(num)
        num = num * 10 + N
    }
    
    for i in 1..<9{
        for j in 1..<i{
            for op1 in numbers[j]{
                for op2 in numbers[i-j]{
                    numbers[i].insert(op1+op2)
                    numbers[i].insert(op1-op2)
                    numbers[i].insert(op1*op2)
                    if op2 != 0{
                        numbers[i].insert(op1/op2)
                    }
                }
            }
        }
        
        if numbers[i].contains(number){
            return i
        }
    }
    return -1
}

