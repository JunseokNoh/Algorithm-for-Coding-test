//
//  위클리챌린지 3주차.swift
//  codingTest
//
//  Created by junseok on 2021/08/30.
//
////
//import Foundation
//
//enum Mode{
//    case zero_space
//    case puzzle
//}
//
//func BFS(_ y:Int,_ x:Int,_ hist:inout [[Int]], _ size:Int,_ mode:Mode)-> [(Int,Int)]{
//    let dirs:[(Int, Int)] = [(-1,0), (0,1), (1,0), (0,-1)]
//    var que:[(Int, Int)] = []
//    var result:[(Int, Int)] = []
//    que.append((y,x))
//    result.append((y,x))
//
//    var target:Int = -1
//    var noneTarget:Int = -1
//
//    switch mode{
//        case .zero_space:
//            target = 0
//            noneTarget = 1
//        case .puzzle:
//            target = 1
//            noneTarget = 0
//    }
//    hist[y][x] = noneTarget
//    while que.count > 0{
//        let val = que.removeFirst()
//        let yy = val.0
//        let xx = val.1
//
//        for dir in dirs{
//            let dy = yy + dir.0
//            let dx = xx + dir.1
//            if 0<=dy && dy < size && 0<=dx && dx<size && (hist[dy][dx]) == target{
//                hist[dy][dx] = noneTarget
//                que.append((dy,dx))
//                result.append((dy,dx))
//            }
//        }
//    }
//
//    return result
//}
//
//func rotate(_ table:[[Int]], _ size:Int)->[[Int]]{
//    var rtable = table
//    for i in 0..<size{
//        for j in 0..<size{
//            rtable[j][size-i-1] = table[i][j]
//        }
//    }
//    return rtable
//}
//
//func solution(_ game_board:[[Int]], _ table:[[Int]]) -> Int {
//    var hist:[[Int]] = game_board
//    let size = game_board.count
//    var puzle_hist:[[Int]] = table
//    var zero_spaces = [[(Int,Int)]]()
//    var result = 0
//
//    for i in 0..<size{
//        for j in 0..<size{
//            if hist[i][j] == 0 {
//                let zero_space = BFS(i,j,&hist,size,.zero_space)
//                zero_spaces.append(zero_space)
//            }
//        }
//    }
//
//    var zero_hist = [Bool](repeating: true, count: zero_spaces.count)
//
//    for index in 0..<zero_spaces.count{
//        let zero_space = zero_spaces[index]
//        if zero_space.count>6{
//            continue
//        }
//        for _ in 0..<4{
//            for n in 0..<size{
//                for m in 0..<size{
//                    if puzle_hist[n][m] == 1{
//                        var temp_hist = puzle_hist
//                        let puzzle = BFS(n,m,&temp_hist,size,.puzzle)
//                        let puzzle_count = puzzle.count
//                        if (zero_space.count == puzzle_count) && zero_hist[index]{
//                            let dify = zero_space[0].0 - puzzle[0].0
//                            let difx = zero_space[0].1 - puzzle[0].1
//                            var flag = true
//
//                            for l in 0..<puzzle_count{
//                                if (zero_space[l].0 != (puzzle[l].0 + dify)) || (zero_space[l].1 != (puzzle[l].1 + difx)){
//                                    flag = false
//                                    break
//                                }
//                            }
//
//                            if flag{
//                                result += puzzle.count
//                                puzle_hist = temp_hist
//                                zero_hist[index] = false
//                            }
//                        }
//                    }
//                }
//            }
//            puzle_hist = rotate(puzle_hist, size)
//        }
//    }
//
//    return result
//}
//
//
//
//print(solution([[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]], [[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]]))
