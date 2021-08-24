import Foundation

func DFS(_ depth:Int, _ sum:Int, _ numbers:[Int], _ target:Int, _ count:inout Int){
    if depth >= numbers.count{

        if sum == target {count += 1}
        return 
    }

    DFS(depth+1, sum + numbers[depth], numbers, target, &count)
    DFS(depth+1, sum - numbers[depth], numbers, target, &count)

}

func solution(_ numbers:[Int], _ target:Int) -> Int {
    var count = 0

    DFS(0,0,numbers,target,&count)
    return count
}

print(solution([1,1,1,1,1], 3))