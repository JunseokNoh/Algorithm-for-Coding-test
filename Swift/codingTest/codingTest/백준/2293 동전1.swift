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
var coins = [Int]()

for _ in 0..<N{
    let coin = Int(readLine()!)!
    coins.append(coin)
}

var dp = [Int](repeating: 0, count: K+1)

dp[0] = 1

for coin in coins{
    for j in 1...K{
        if coin <= j {
            dp[j] += dp[j-coin]
            if dp[j] > Int(pow(2.0, 31.0)){ dp[j] = 0 }
        }
    }
}

if dp[K] == 0 {
    print(-1)
}
else {
    print(dp[K])
}
