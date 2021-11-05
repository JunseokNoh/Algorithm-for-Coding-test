
import Foundation

func dijkstra(_ src:Int, _ dst:Int, _ fees: [[[Int]]])->Int{
    let n = fees.count
    var dist = [Int](repeating: Int.max, count: n)
    
    dist[src] = 0
    
    let pq = PriorityQueue<[Int]>{ o1 , o2 in
        if o2[0] > o1[0]{
            return true
        }else{
            return false
        }
    }
    pq.push([0, src])
    while pq.size() > 0{
        let val = pq.pop()!
        let w = val[0]
        let node = val[1]
        
        if dist[node] < w {
            continue
        }
        
        for fee in fees[node]{
            let tx = fee[0]
            var tcost = fee[1]
            
            tcost += w
            if tcost < dist[tx]{
                dist[tx] = tcost
                pq.push([tcost, tx])
            }
        }
    }

    return dist[dst]
}

func solution(_ n:Int, _ s:Int, _ a:Int, _ b:Int, _ fares:[[Int]]) -> Int {
    var fees = [[[Int]]](repeating: [[Int]](), count: n+1)

    for fare in fares{
        let a = fare[0]
        let b = fare[1]
        let cost = fare[2]
        
        fees[a].append([b, cost])
        fees[b].append([a, cost])
    }

    var cost = dijkstra(s, a, fees) + dijkstra(s, b, fees)
    
    for i in 1..<n+1{
        if s != i {
            let common = dijkstra(s, i, fees)
            let load_a = dijkstra(i, a, fees)
            let load_b = dijkstra(i, b, fees)
            
            if common == Int.max || load_a == Int.max || load_b == Int.max{
                continue
            }
            
            let result = common + load_a + load_b
            if cost > result{
                cost = result
            }
        }
    }
    
    return cost
}

class PriorityQueue<T> {
    private var heap: [T] = []
    private let comparing: (_ o1: T,_ o2: T) -> Bool
    
    init(_ comparing: @escaping (_ o1: T,_ o2: T) -> Bool) {
        self.comparing = comparing
    }
    
    func size() -> Int {
        heap.count
    }
    
    func isEmpty() -> Bool { heap.isEmpty }
    func clear() { heap.removeAll() }
    func peek() -> T? { heap.first }
    func getAll() -> [T]{ heap }
    func push(_ value: T) {
        heap.append(value)
        if heap.count == 1 { return }
        var valueIndex = heap.count - 1
        var parentIndex = (valueIndex-1) / 2
        
        while !comparing(heap[parentIndex], heap[valueIndex]) {
            heap.swapAt(valueIndex, parentIndex)
            valueIndex = parentIndex
            parentIndex = (valueIndex-1) / 2
            if valueIndex == 0 { break }
        }
    }
    
    func pop() -> T? {
        if heap.count == 0 { return nil }
        if heap.count == 1 { return heap.removeFirst() }
        
        func isChildEmpty(_ value: Int,_ left: Int,_ right: Int) -> Bool {
            if heap.count <= left { return true }
            if heap.count > right { return false }
            if comparing(heap[value], heap[left]) { return true }
            heap.swapAt(value, left)
            return true
        }
        
        heap.swapAt(0, heap.count-1)
        let answer = heap.removeLast()
        var valueIndex = 0
        var leftIndex = valueIndex * 2 + 1
        var rightIndex = valueIndex * 2 + 2
        
        if isChildEmpty(valueIndex, leftIndex, rightIndex) { return answer }
        while !comparing(heap[valueIndex], heap[leftIndex]) || !comparing(heap[valueIndex], heap[rightIndex]) {
            let index = comparing(heap[leftIndex], heap[rightIndex]) ? leftIndex : rightIndex
            heap.swapAt(valueIndex, index)
            valueIndex = index
            leftIndex = valueIndex * 2 + 1
            rightIndex = valueIndex * 2 + 2
            if isChildEmpty(valueIndex, leftIndex, rightIndex) { break }
        }
        return answer
    }
}
