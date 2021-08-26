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

var dp = [Int](repeating: Int.max, count: K+1)
dp[0] = 0

for coin in coins{
    if coin > K {
        continue
    }
    for j in coin...K{
        if dp[j - coin] < Int.max && dp[j] > (dp[j - coin] + 1){
            dp[j] = dp[j - coin] + 1
        }
    }
}

if dp[K] == Int.max {
    print(-1)
}
else {
    print(dp[K])
}
