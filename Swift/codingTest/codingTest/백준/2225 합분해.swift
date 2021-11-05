//
//  main.swift
//  codingTest
//
//  Created by junseok on 2021/08/25.
//

import Foundation

var input = readLine()!.split(separator: " ").map{ Int($0)! }
var N = input[0]
var K = input[1]


var dp = [[Int]](repeating: [Int](repeating: 0, count: N+1), count: K+1)

(0...N).forEach{ i in
    dp[1][i] = 1
}

for i in 1...K {
    dp[i][0] = 1
    for j in 1...N{
        for l in 0...j{
            dp[i][j] += (dp[i-1][l] % 1000000000)
        }
    }
}

print(dp[K][N] % 1000000000)


