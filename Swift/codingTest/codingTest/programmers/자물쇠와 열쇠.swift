//
//  자물쇠와 열쇠.swift
//  codingTest
//
//  Created by junseok on 2021/08/31.
//

import Foundation

func rotate(_ table:[[Int]], _ size:Int)->[[Int]]{
    var rtable = table
    for i in 0..<size{
        for j in 0..<size{
            rtable[j][size-i-1] = table[i][j]
        }
    }
    return rtable
}

func put_key(_ row:Int, _ col:Int, _ lock:[[Int]], _ key:[[Int]], _ lsize:Int)->Bool{
    let key_count = key.count
    var plock = lock

    for n in 0..<key_count{
        for m in 0..<key_count{
            plock[n + row][m + col] += key[n][m]
        }
    }

    let l = key_count - 1
    let r = key_count - 1

    for i in l..<l+lsize{
        for j in r..<r+lsize{
            if plock[i][j] == 0 || plock[i][j] == 2{
                return false
            }
        }
    }
    
    return true
}

func solution(_ key:[[Int]], _ lock:[[Int]]) -> Bool {
    var key = key
    let key_size = key.count
    let lock_size = lock.count + (key_size - 1) * 2
    var new_lock = [[Int]](repeating: [Int](repeating: 0, count: lock_size), count: lock_size)
    
    for i in 0..<lock.count{
        for j in 0..<lock.count{
            new_lock[i+key_size-1][j+key_size-1] = lock[i][j]
        }
    }
    
    for _ in 0..<4{
        let size = key.count + lock.count - 1
        for i in 0..<size{
            for j in 0..<size{
                if put_key(i,j,new_lock,key,lock.count){
                    return true
                }
            }
        }
        key = rotate(key, key_size)
    }
    
    return false
}
