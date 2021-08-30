//
//  위클리챌린지 3주차.swift
//  codingTest
//
//  Created by junseok on 2021/08/30.
//

import Foundation

enum Mode{
    case wite_space
    case puzzle
}

func BFS(_ y:Int,_ x:Int,_ hist:inout [[Int]], _ size:Int,_ mode:Mode)-> [(Int,Int)]{
    var dirs:[(Int, Int)] = [(-1,0), (0,1), (1,0), (0,-1)]
    var que:[(Int, Int)] = []
    var result:[(Int, Int)] = []
    que.append((y,x))
    result.append((y,x))
    
    var target:Int = -1
    var noneTarget:Int = -1
    
    switch mode{
        case .wite_space:
            target = 0
            noneTarget = 1
        case .puzzle:
            target = 1
            noneTarget = 0
        default:
        break
    }
    
    while que.count > 0{
        let val = que.removeFirst()
        let yy = val.0
        let xx = val.1
        hist[yy][xx] = noneTarget
        for dir in dirs{
            let dy = yy + dir.0
            let dx = xx + dir.1
            if 0<=dy && dy < size && 0<=dx && dx<size && (hist[dy][dx]) == target{
                que.append((dy,dx))
                result.append((dy,dx))
            }
        }
    }
    
    return result
}

func solution(_ game_board:[[Int]], _ table:[[Int]]) -> Int {
    var hist:[[Int]] = game_board
    let size = game_board.count
    var table = table
    for i in 0..<size{
        for j in 0..<size{
            if hist[i][j] == 0 {
                let white_space = BFS(i,j,&hist,size,.wite_space)
                let space_count = white_space.count
                var puzle_hist:[[Int]] = table
                
                for n in 0..<size{
                    for m in 0..<size{
                        if puzle_hist[n][m] == 1{
                            let puzzle = BFS(n,m,&puzle_hist,size,.puzzle)
                            let puzzle_count = puzzle.count
                            
                            if space_count == puzzle_count{
                                for k in 0..<puzzle_count{
                                    let dify = white_space[0].0 - puzzle[k].0
                                    let difx = white_space[0].1 - puzzle[k].1
                                    var flag = true
                                    
                                    for l in 0..<puzzle_count{
                                        if white_space[l].0 != (puzzle[l].0 - dify) || white_space[l].1 != (puzzle[l].1 - difx){
                                            flag = false
                                            break
                                        }
                                    }
                                    
                                    if flag{
                                        print(puzzle)
                                    }
                                }
                            }
                            //print(puzzle, puzzle_count)
                        }
                    }
                }
            }
        }
    }
    
    for i in 0..<4{
        table = rotate(table, size)
    }
    return -1
}

func rotate(_ table:[[Int]], _ size:Int)->[[Int]]{
    var rtable = table
    for i in 0..<size{
        for j in 0..<size{
            rtable[j][size-i-1] = table[i][j]
        }
    }
    return rtable
}
